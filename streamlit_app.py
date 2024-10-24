# Streamlitライブラリをインポート
import streamlit as st
import random
for i in range(1,100):
    x=random.randint(1,10000)
    print(str(i)+"回目："+str(x))

#おやつの決定
if x%3==0:
    print("今日のおやつはポッキー！"):
elif x%3==1:
    print("今日のおやつはグミ！"):
else print("今日のおやつはクッキー！"):

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('今日のおやつ')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 やっほー、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示

#数字の入力
write_number= st.text_input("10進数の数字を入力してください")
if st.button("クリック"):
    st.write("ボタンがクリックされました!")


# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")

#　奇数と偶数の仕分け
