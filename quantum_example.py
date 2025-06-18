"""Quantum computing demo with broad application goals.

このサンプルコードは、Qiskit を使って簡単なベル状態を作り、
測定するデモを行います。量子コンピュータは以下のような分野で
応用が期待されています:

- 医薬品と健康: 新薬開発の加速、遺伝子解析の高速化、個別化医療の実現
- 通信セキュリティ: より安全な暗号技術の開発と現行暗号の脆弱性評価
- 交通と物流: 渋滞緩和や配送時間短縮のための最適経路検索
- 金融業界: リスク管理の精度向上、市場予測の高度化、ポートフォリオ最適化
- エネルギー管理: 再生可能エネルギーの需給バランス最適化
- 科学研究と新素材開発: 複雑な分子構造解析や新素材開発の加速
- 人工知能と機械学習: 学習アルゴリズム高速化とパターン認識精度向上
- 気候変動対策: 高精度な気候モデリングによる環境保護策の立案
"""

from qiskit import QuantumCircuit, Aer, execute


def run_bell_pair():
    """Run a simple circuit that creates a Bell pair and measures it."""
    # 2 qubits with 2 classical bits for measurement
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    return counts


if __name__ == "__main__":
    counts = run_bell_pair()
    print("Measurement results:", counts)
