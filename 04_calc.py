from scipy.special import comb
import numpy as np
import json


def pr(n: int, k: int = 0, t: float = 100.0, d: float = 20.0):
    return comb(n+1, k) * np.sum([
        ((-1) ** (m-k)) * comb(n+1-k, m-k) * (np.maximum(0, 1-(m*d/t))**n)
        for m in range(k, (n+1)+1)
    ])


def main():
    total_distance: float = 100.0
    allowable_distance: float = 20.0
    k: int = 0

    node_num_list: List[int] = list(range(1, 57))
    result_list = [
        pr(
            n=n,
            k=k,
            t=total_distance,
            d=allowable_distance
        )
        for n in node_num_list]

    with open("./output/calc_result.json", mode="w") as f:
        json.dump({
            "param": {
                "total_distance": total_distance,
                "allowable_distance": allowable_distance,
                "k": k,
            },
            "x": node_num_list,
            "y": result_list
        }, f, indent=2)


if __name__ == "__main__":
    main()
