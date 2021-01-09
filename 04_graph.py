import matplotlib.pyplot as plt
from matplotlib import rcParams
import json


def main():
    rcParams["font.family"] = "sans-serif"
    rcParams["font.sans-serif"] = ["HackGen"]

    sim_result = json.load(open("./output/result.json"))
    calc_result = json.load(open("./output/calc_result.json"))

    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.plot(sim_result["x"], sim_result["y"],
            marker="o", mfc="None", label="シミュレーション値")
    ax.plot(calc_result["x"], calc_result["y"],
            color="gray", alpha=0.6, marker="|", mfc="None", label="計算値")

    ax.set_ylabel("確率")
    ax.set_xlabel("ノード数 $n$")

    ax.legend()
    ax.grid()

    plt.savefig("./output/graph.png")
    plt.show()


if __name__ == "__main__":
    main()
