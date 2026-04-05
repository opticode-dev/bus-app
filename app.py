#① python3 -m venv myenv
#② source myenv/bin/activate
#③ 同じ環境なら１回やればOK　違う環境ならもう一回　pip install matplotlib
#④ python main.py
#streamlit run app.py

import streamlit as st
import pandas as pd

st.title("バス時刻検索")

bus = pd.read_csv("bus.csv")
one = pd.read_csv("one_days.csv")
two = pd.read_csv("two_days.csv")

# 日付入力
日付 = st.date_input("日付を選択")
日付 = str(日付)

# 判定
if 日付 in one["日付"].values:
    便タイプ = 1
elif 日付 in two["日付"].values:
    便タイプ = 2
else:
    st.error("本日は運行していません")
    st.stop()

st.write(f"今日は {便タイプ} 便")

# 出発地点
出発地点 = st.selectbox("出発地点", bus["出発地点"].unique())

# フィルタ
filtered = bus[
    (bus["出発地点"] == 出発地点) &
    (bus["便タイプ"] == 便タイプ)
]

st.write("時刻表")

if filtered.empty:
    st.warning("該当するバスがありません")
else:
    st.dataframe(filtered)