# -*-coding:utf8-*-

# (c)Lalaso2000
from pylab import *
import numpy as np

data = loadtxt("data.csv", delimiter=",", skiprows = 1)
# csvの中身は
# 0列目→時間
# 1列目→解析したい波形
# を想定
# 1行目はスキップ


#入力波形をプロット
plot(data[:,0]*1000, data[:,1], label = "input", lw=2, color="#ff0000")
#0列目＝時間を1000倍 → 横軸の単位を[ms]に
xlim(0,100)	#横軸の範囲を指定
ylim(-15,15)	#縦軸の範囲を指定
xlabel("time [ms]")
ylabel("amplitude")
legend() #凡例の出力
grid(which='major', color='#bababa', linestyle='--')    # グリッド線


show()