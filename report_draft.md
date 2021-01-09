---
puppeteer:
  header: "F20C004C 太田 剛史"
  displayHeaderFooter: true
  headerTemplate: '<div style="width:100%; border-bottom:0pt solid #eeeeee; margin: -12px 20px 0px 20px; font-size:6pt;"><p class="date" style="text-align:left"></p></div>'
  footerTemplate: '<div style="width:100%; text-align:right; border-bottom:0pt solid #eeeeee; margin: -18px 20px 0px 20px; font-size:6pt;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'
---

<div class='title-container'>
    <div class="title">移動情報ネットワーク特論</div>
    <div class="subtitle">レポート課題4</div>
    <div class="author">
    電気情報工学専攻 情報工学コース<br>
    F20C004C 太田剛史
    </div>
</div>

# 目次

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [目次](#目次)
- [はじめに](#はじめに)
- [シミュレーションプログラムの作成](#シミュレーションプログラムの作成)
- [理論計算のプログラムの作成](#理論計算のプログラムの作成)
- [結果](#結果)
- [考察](#考察)

<!-- /code_chunk_output -->

# はじめに

以下にシミュレーションのスクリプトを記すが, Github上にシミュレーションのスクリプトと描画のためのスクリプト, レポート作成に利用したmarkdownなどを載せてあるため, ネットワーク環境がある場合は下記のURLを参照していただきたい.

> https://github.com/haru1843/mobile_info_network_rep04

<div style="page-break-before:always"></div>


# シミュレーションプログラムの作成

ノードAとノードBの間に$n$個のノードが一様かつ独立に分布している場合に, ノードAとノードBが連結可能である確率$p_n(t)$を求めるシミュレーションプログラムを作成する. 
また今回のシミュレーションにおける各パラメータは以下の通りである.

| パラメータ |                内容                |          値           |
|:----------:|:----------------------------------:|:---------------------:|
|     t      |       ノードAとノードBの距離       |        $100.0$        |
|     d      |           電波の届く距離           |        $20.0$         |
|     n      | ノードAとノードBの間にあるノード数 | $1, 2, 3, \cdots, 56$ |
|     -      |     シミュレーションの実行回数     |         $1e6$         |


プログラムの作成に利用した言語は`Python 3.6.9`である. 下記にプログラムを記す.

@import "./04_sim.py" {class="line-numbers"}

<div style="page-break-before:always"></div>

# 理論計算のプログラムの作成

理論計算に利用したプログラムを下記に記す.
また, プログラムの作成に利用した言語は`Python 3.6.9`である.

@import "./04_calc.py" {class="line-numbers"}

<div style="page-break-before:always"></div>

# 結果

上記までのプログラムを用いて算出した結果を, 横軸をノード数$n$, 縦軸を連結可能である確率としたグラフを作成し, 以下に示す. 

@import "./output/graph.png" {width=800px}

# 考察

シミュレーション値と理論計算値がほぼ一致していることがわかる.

ノード数が少ないときに確率が0となってイルことに関して, 今回のシミュレーションではノードA/B間の距離が $100.0$ であり, 電波の届く距離が $20.0$ であるため, 最低でもノード数が5つないとノードA/B間が連結できないためこのようになる.
