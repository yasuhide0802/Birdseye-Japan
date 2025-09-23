"""Example script to compute a look-away angle using camera poses."""

from __future__ import annotations

import argparse
from typing import Tuple

import numpy as np
from WorldTrack.datasets.multiviewx_dataset import MultiviewX


def load_camera_pose(dataset_root: str, camera_idx: int = 0) -> Tuple[np.ndarray, np.ndarray]:
    """Return camera position and rotation matrix from the dataset."""

    dataset = MultiviewX(dataset_root)
    extrinsic = dataset.extrinsic_matrices[camera_idx]  # 3x4 matrix
    camera_pos = extrinsic[:, 3]
    rotation_mat = extrinsic[:, :3]
    return camera_pos, rotation_mat


def compute_lookaway_view(camera_pos: np.ndarray, cup_pos: np.ndarray) -> float:
    """Compute yaw angle (rad) to avert the gaze from ``cup_pos``."""

    vec_to_cup = cup_pos - camera_pos
    vec_away = -vec_to_cup
    yaw = float(np.arctan2(vec_away[1], vec_away[0]))
    return yaw


def wrap_to_pi(angle: float) -> float:
    """Wrap ``angle`` into ``[-pi, pi]`` for smooth comparisons."""

    return float((angle + np.pi) % (2 * np.pi) - np.pi)


def yaw_from_rotation(rotation_mat: np.ndarray) -> float:
    """Return yaw angle extracted from a rotation matrix."""

    return float(np.arctan2(rotation_mat[1, 0], rotation_mat[0, 0]))


def view_yaw_difference(rotation_mat: np.ndarray, target_yaw: float) -> float:
    """Return yaw difference between camera orientation and ``target_yaw``."""

    cam_yaw = yaw_from_rotation(rotation_mat)
    return wrap_to_pi(target_yaw - cam_yaw)


def compute_gentle_gaze(
    camera_pos: np.ndarray,
    rotation_mat: np.ndarray,
    cup_pos: np.ndarray,
    gentle_factor: float = 0.5,
    offset_deg: float = 8.0,
) -> Tuple[float, float]:
    """Return a softened yaw that feels calm and reassuring.

    The returned tuple contains the gentle yaw angle as well as the yaw
    difference with respect to the dataset orientation. ``gentle_factor``
    controls how far we travel from the original camera yaw toward the
    strict look-away direction (0 keeps the camera still, 1 matches the
    direct avoidance yaw). ``offset_deg`` adds a small sideways offset so
    that the gaze opens slightly instead of turning sharply away, yielding a
    kinder impression.
    """

    lookaway_yaw = compute_lookaway_view(camera_pos, cup_pos)
    cam_yaw = yaw_from_rotation(rotation_mat)
    delta = wrap_to_pi(lookaway_yaw - cam_yaw)

    gentle_factor = float(np.clip(gentle_factor, 0.0, 1.0))
    softened = cam_yaw + gentle_factor * delta
    offset = np.deg2rad(offset_deg) * np.sign(delta)
    gentle_yaw = wrap_to_pi(softened + offset)
    gentle_diff = wrap_to_pi(gentle_yaw - cam_yaw)
    return gentle_yaw, gentle_diff


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_root", help="Path to MultiviewX dataset")
    parser.add_argument(
        "--camera", type=int, default=0, help="Camera index in the dataset"
    )
    parser.add_argument(
        "--cup-pos",
        type=float,
        nargs=3,
        metavar=("X", "Y", "Z"),
        default=(0.0, 0.0, 0.0),
        help="Position of Satoh Yasuhide's coffee cup in world coordinates",
    )
    parser.add_argument(
        "--gentle-factor",
        type=float,
        default=0.5,
        help=(
            "Interpolation factor between the dataset yaw and the direct"
            " look-away yaw for the gentle gaze"
        ),
    )
    parser.add_argument(
        "--gentle-offset-deg",
        type=float,
        default=8.0,
        help=(
            "Sideways offset in degrees that slightly opens the gentle gaze"
            " away from a strict about-face"
        ),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    cup_pos = np.array(args.cup_pos, dtype=float)
    camera_pos, rot_mat = load_camera_pose(args.dataset_root, camera_idx=args.camera)

    yaw = compute_lookaway_view(camera_pos, cup_pos)
    yaw_diff = view_yaw_difference(rot_mat, yaw)
    gentle_yaw, gentle_diff = compute_gentle_gaze(
        camera_pos,
        rot_mat,
        cup_pos,
        gentle_factor=args.gentle_factor,
        offset_deg=args.gentle_offset_deg,
    )

    print(
        f"Yaw to look away from Satoh Yasuhide's cup: {yaw:.3f} radians"
    )
    print(
        f"Yaw difference from dataset orientation: {yaw_diff:.3f} radians"
    )
    print(
        "Yaw for a gentle, reassuring gaze: "
        f"{gentle_yaw:.3f} radians (difference {gentle_diff:.3f} radians)"
    )
