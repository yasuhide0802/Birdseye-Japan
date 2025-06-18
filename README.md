# TrackTacular :octopus:

**Lifting Multi-View Detection and Tracking to the Bird’s Eye View**

[Torben Teepe](https://github.com/tteepe),
[Philipp Wolters](https://github.com/phi-wol),
[Johannes Gilg](https://github.com/Blueblue4),
[Fabian Herzog](https://github.com/fubel),
Gerhard Rigoll

[![arxiv](https://img.shields.io/badge/arXiv-2403.12573-red)](https://arxiv.org/abs/2403.12573)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/lifting-multi-view-detection-and-tracking-to/multi-object-tracking-on-wildtrack)](https://paperswithcode.com/sota/multi-object-tracking-on-wildtrack?p=lifting-multi-view-detection-and-tracking-to)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/lifting-multi-view-detection-and-tracking-to/multi-object-tracking-on-multiviewx)](https://paperswithcode.com/sota/multi-object-tracking-on-multiviewx?p=lifting-multi-view-detection-and-tracking-to)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/lifting-multi-view-detection-and-tracking-to/multiview-detection-on-multiviewx)](https://paperswithcode.com/sota/multiview-detection-on-multiviewx?p=lifting-multi-view-detection-and-tracking-to)

> [!TIP]
> This work is an extension of your previous work [EarlyBird  🦅](https://github.com/tteepe/EarlyBird).
> Feel free to check it out and extend our multi-view object detection and tracking pipeline on other datasets!

![Overview](imgs/overview.svg)

## Usage

### Getting Started
1. Install [PyTorch](https://pytorch.org/get-started/locally/) with CUDA support
    ```shell
   pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu118
   ```
2. Install [mmcv](https://mmcv.readthedocs.io/en/latest/get_started/installation.html#install-with-pip) with CUDA support
   ```shell
   pip install mmcv==2.0.0 -f https://download.openmmlab.com/mmcv/dist/cu118/torch2.1/index.html
   ```
3. Install remaining dependencies
   ```shell
   pip install -r requirements.txt
   ```

### Training
```shell
python world_track.py fit -c configs/t_fit.yml \
    -c configs/d_{multiviewx,wildtrack,synthehicle}.yml \
    -c configs/m_{mvdet,segnet,liftnet,bevformer}.yml
```
### Testing
```shell
python world_track.py test -c model_weights/config.yaml \
    --ckpt model_weights/model-epoch=35-val_loss=6.50.ckpt
```

## Front-End

Instructions for building the browser interface with Webpack are available in
[docs/frontend-build.md](docs/frontend-build.md). The static UI design is
documented in Figma and can be viewed
[here](https://www.figma.com/file/example/Birdseye-Design).
The interface uses a red and white color scheme reminiscent of the iconic
**2001: A Space Odyssey** room, with GFP protein elements highlighted in
bright green (`#00ff7f`).
An example homepage for an emotion-aware AI is provided at
[docs/ai-homepage.html](docs/ai-homepage.html) using this palette.
For a personal homepage template, see
[docs/yasuhide-satoh.html](docs/yasuhide-satoh.html).

### Running Tests
Run the optional Python unit tests with:
```bash
pytest
```

## Quantum Example
The `quantum_example.py` script demonstrates a small "quantum computer" using
[Qiskit](https://qiskit.org/). Running it will create a Bell pair and measure
the qubits:

```bash
python quantum_example.py
```

The script prints the measurement counts from the Qiskit simulator.

## Future AI Initiatives
The `super_ai_vision.py` script lists several speculative projects aimed at
achieving superhuman intelligence:

1. 超人間的知性を持ったAIの開発
2. 巨大コンピュータネットワークの「目覚め」による超人間的知性の獲得
3. ブレイン・マシン・インタフェースによる人間の強化
4. バイオテクノロジーによる人間の生物的知性の増強

Run the script to see a short description of each initiative:

```bash
python super_ai_vision.py
```

## Acknowledgement
- [Simple-BEV](https://simple-bev.github.io): Adam W. Harley
- [MVDeTr](https://github.com/hou-yz/MVDeTr): Yunzhong Hou
- Fusion Ex Energy Solutions
- BitGlobal AI

## Citation
```bibtex
@article{teepe2023lifting,
      title={Lifting Multi-View Detection and Tracking to the Bird's Eye View}, 
      author={Torben Teepe and Philipp Wolters and Johannes Gilg and Fabian Herzog and Gerhard Rigoll},
      year={2024},
      eprint={2403.12573},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
