import tkinter
import math

pi = math.pi

# Tkクラス生成
root = tkinter.Tk()

# 画面サイズ
root.geometry('700x630')

# 画面タイトル
root.title('面積計算')

# 面積計算の関数群
def san_kei_click():
    und = float(san_tei.get())
    high = float(san_taka.get())
    ara = und * high / 2
    san_men.delete(0, tkinter.END)
    san_men.insert(0, ara)

def sei_kei_click():
    hen = float(sei_hen.get())
    ara = hen * hen
    sei_men.delete(0, tkinter.END)
    sei_men.insert(0, ara)

def chou_kei_click():
    tate = float(chou_tate.get())
    yoko = float(chou_yoko.get())
    ara = tate * yoko
    chou_men.delete(0, tkinter.END)
    chou_men.insert(0, ara)

def hei_kei_click():
    und = float(hei_tei.get())
    high = float(hei_taka.get())
    ara = und * high
    hei_men.delete(0, tkinter.END)
    hei_men.insert(0, ara)

def dai_kei_click():
    up_und = float(dai_jyou.get())
    dn_und = float(dai_ka.get())
    high = float(dai_taka.get())
    ara = ( up_und + dn_und ) * high / 2
    dai_men.delete(0, tkinter.END)
    dai_men.insert(0, ara)

def hishi_kei_click():
    tai1 = float(hishi_tai1.get())
    tai2 = float(hishi_tai2.get())
    ara = tai1 * tai2 / 2
    hishi_men.delete(0, tkinter.END)
    hishi_men.insert(0, ara)

def en_kei_click():
    han = float(en_han.get())
    ara = han * han * pi
    en_men.delete(0, tkinter.END)
    en_men.insert(0, ara)

def sein_kei_click():
    hen = float(sein_hen.get())
    n = int(sei_n.get())
    upside = n * ( hen ** 2)
    dnside = 4 * ( math.tan ( pi / n))
    ara = upside / dnside
    sein_men.delete(0, tkinter.END)
    sein_men.insert(0, ara)

# 案内
com_1 =tkinter.Label(text='三角形')
com_1.place(x=100, y=40)

# 三角形の底辺と高さ
lbl_1 = tkinter.Label(text='底辺')
lbl_1.place(x=60, y=70)
san_tei = tkinter.Entry(width=20)
san_tei.place(x=90, y=70)

lbl_2 = tkinter.Label(text='高さ')
lbl_2.place(x=60, y=110)
san_taka = tkinter.Entry(width=20)
san_taka.place(x=90, y=110)

# 三角形面積出力欄
lbl_3 = tkinter.Label(text='面積:')
lbl_3.place(x=60, y=150)
san_men = tkinter.Entry(width=20)
san_men.place(x=90, y=150)

# 三角形計算ボタン
san_kei = tkinter.Button(root, text='計算', command=san_kei_click)
san_kei.place(x=90, y=190)


# 案内
com_2 =tkinter.Label(text='正方形')
com_2.place(x=300, y=40)

# 正方形の一辺
lbl_4 = tkinter.Label(text='一辺')
lbl_4.place(x=260, y=70)
sei_hen = tkinter.Entry(width=20)
sei_hen.place(x=290, y=70)

# 正方形面積出力欄
lbl_5 = tkinter.Label(text='面積:')
lbl_5.place(x=260, y=150)
sei_men = tkinter.Entry(width=20)
sei_men.place(x=290, y=150)

# 正方形計算ボタン
sei_kei = tkinter.Button(root, text='計算', command=sei_kei_click)
sei_kei.place(x=290, y=190)


# 案内
com_3 =tkinter.Label(text='長方形')
com_3.place(x=500, y=40)

# 長方形の縦
lbl_6 = tkinter.Label(text='縦')
lbl_6.place(x=460, y=70)
chou_tate = tkinter.Entry(width=20)
chou_tate.place(x=490, y=70)

# 長方形の横
lbl_7 = tkinter.Label(text='横')
lbl_7.place(x=460, y=110)
chou_yoko= tkinter.Entry(width=20)
chou_yoko.place(x=490, y=110)

# 長方形面積出力欄
lbl_8 = tkinter.Label(text='面積:')
lbl_8.place(x=460, y=150)
chou_men = tkinter.Entry(width=20)
chou_men.place(x=490, y=150)

# 長方形計算ボタン
chou_kei = tkinter.Button(root, text='計算', command=chou_kei_click)
chou_kei.place(x=490, y=190)


# 案内
com_4 =tkinter.Label(text='平行四辺形')
com_4.place(x=100, y=240)

# 平行四辺形の底辺
lbl_9 = tkinter.Label(text='底辺')
lbl_9.place(x=60, y=270)
hei_tei = tkinter.Entry(width=20)
hei_tei.place(x=90, y=270)

# 平行四辺形の高さ
lbl_10 = tkinter.Label(text='高さ')
lbl_10.place(x=60, y=310)
hei_taka= tkinter.Entry(width=20)
hei_taka.place(x=90, y=310)

# 面積出力欄
lbl_11 = tkinter.Label(text='面積:')
lbl_11.place(x=60, y=350)
hei_men = tkinter.Entry(width=20)
hei_men.place(x=90, y=350)

# 平行四辺形計算ボタン
hei_kei = tkinter.Button(root, text='計算', command=hei_kei_click)
hei_kei.place(x=90, y=390)


# 案内
com_5 =tkinter.Label(text='台形')
com_5.place(x=300, y=240)

# 台形の上底
lbl_12 = tkinter.Label(text='上底')
lbl_12.place(x=260, y=270)
dai_jyou = tkinter.Entry(width=7)
dai_jyou.place(x=290, y=270)

# 台形の下底
lbl_13 = tkinter.Label(text='下底')
lbl_13.place(x=338, y=270)
dai_ka= tkinter.Entry(width=7)
dai_ka.place(x=368, y=270)

# 台形の高さ
lbl_14 = tkinter.Label(text='高さ')
lbl_14.place(x=260, y=310)
dai_taka= tkinter.Entry(width=20)
dai_taka.place(x=290, y=310)

# 台形面積出力欄
lbl_15 = tkinter.Label(text='面積:')
lbl_15.place(x=260, y=350)
dai_men = tkinter.Entry(width=20)
dai_men.place(x=290, y=350)

# 台形面積計算ボタン
hei_kei = tkinter.Button(root, text='計算', command=dai_kei_click)
hei_kei.place(x=290, y=390)


# 案内
com_6 =tkinter.Label(text='ひし形')
com_6.place(x=500, y=240)

# ひし形の対角線1
lbl_16 = tkinter.Label(text='対角線1')
lbl_16.place(x=440, y=270)
hishi_tai1 = tkinter.Entry(width=20)
hishi_tai1.place(x=490, y=270)

# ひし形の対角線2
lbl_17 = tkinter.Label(text='対角線2')
lbl_17.place(x=440, y=310)
hishi_tai2= tkinter.Entry(width=20)
hishi_tai2.place(x=490, y=310)

# ひし形面積出力欄
lbl_18 = tkinter.Label(text='面積:')
lbl_18.place(x=460, y=350)
hishi_men = tkinter.Entry(width=20)
hishi_men.place(x=490, y=350)

# ひし形面積計算ボタン
hishi_kei = tkinter.Button(root, text='計算', command=hishi_kei_click)
hishi_kei.place(x=490, y=390)


# 案内
com_7 =tkinter.Label(text='円')
com_7.place(x=100, y=440)

# 平行四辺形の底辺
lbl_19 = tkinter.Label(text='半径')
lbl_19.place(x=60, y=470)
en_han = tkinter.Entry(width=20)
en_han.place(x=90, y=470)

# 面積出力欄
lbl_20 = tkinter.Label(text='面積:')
lbl_20.place(x=60, y=550)
en_men = tkinter.Entry(width=20)
en_men.place(x=90, y=550)

# 円面積計算ボタン
en_kei = tkinter.Button(root, text='計算', command=en_kei_click)
en_kei.place(x=90, y=590)


# 案内
com_8 =tkinter.Label(text='正')
com_8.place(x=300, y=440)

com_9 =tkinter.Label(text='角形')
com_9.place(x=370, y=440)

# 正N角形
sei_n = tkinter.Entry(width=7)
sei_n.place(x=320, y=440)

# 平行四辺形の底辺
lbl_21 = tkinter.Label(text='一辺の長さ')
lbl_21.place(x=230, y=470)
sein_hen = tkinter.Entry(width=20)
sein_hen.place(x=290, y=470)

# 面積出力欄
lbl_22 = tkinter.Label(text='面積:')
lbl_22.place(x=260, y=550)
sein_men = tkinter.Entry(width=20)
sein_men.place(x=290, y=550)

# 円面積計算ボタン
sein_kei = tkinter.Button(root, text='計算', command=sein_kei_click)
sein_kei.place(x=290, y=590)

root.mainloop()
