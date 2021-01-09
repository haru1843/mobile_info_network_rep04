import numpy as np
import os.path as path
from typing import List
import json


class Simulator:
    def __init__(self, dist: float, node_num: int, allow_dist: float):
        """
        Params
        -----------------------------------
        dist: float
            ノードAとノードB間の距離
        node_num: int
            ノードAとノードB間に存在するノード数. (ノードAとノードBを含めない)
        allow_dist: float
            ノード間の通信可能距離
        """
        self.dist: float = dist
        self.node_num: int = node_num
        self.allow_dist: float = allow_dist

    def run(self, try_num: int = 100000):
        """
        課題のシミュレーションを実行し, 実行回数に対する通信可能であった割合を返す.

        Param
        -----------------------------------
        try_num: int (default=100000)
            シミュレーションの実行回数

        Return
        -----------------------------------
        availability_ratio: float
            実行回数に対して, 通信可能であった割合. (0~1)
        """
        node_mat = np.sort(self.dist * np.random.rand(try_num, self.node_num), axis=1)
        head = np.zeros((try_num, 1))
        tail = np.full((try_num, 1), self.dist)

        return np.sum(np.sum(
            np.diff(np.concatenate([head, node_mat, tail], axis=1), axis=1) > self.allow_dist,
            axis=1
        ) == 0) / try_num


def main():
    # 全体のパラメータの設定
    try_num: int = int(1e6)
    total_distance: float = 100.0
    allowable_distance: float = 20.0

    node_num_list: List[int] = list(range(1, 57))

    result_list: List[float] = [0] * len(node_num_list)

    # 各ノード数に対するシミュレーションの実行
    for idx, node_num in enumerate(node_num_list):
        sim = Simulator(
            dist=total_distance,
            node_num=node_num,
            allow_dist=allowable_distance
        )
        result_list[idx] = sim.run(try_num=try_num)

    # データの保存
    with open("./output/result.json", mode="w") as f:
        json.dump({
            "param": {
                "try_num": try_num,
                "total_distance": total_distance,
                "allowable_distance": allowable_distance,
            },
            "x": node_num_list,
            "y": result_list
        }, f)


if __name__ == "__main__":
    main()
