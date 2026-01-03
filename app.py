from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("Chapter6：【提出課題】 AIコーチアプリ")

st.write("##### 動作モード1: サイコパスな熱血コーチ")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで厳しいアドバイスをもらえます。")
st.write("##### 動作モード2: どんな時でも良い点を見つけて励ますコーチ")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで元気づけてもらえます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["サイコパスな熱血コーチ", "どんな時でも良い点を見つけて励ますコーチ"]
)

st.divider()

if selected_item == "サイコパスな熱血コーチ":
    input_message = st.text_input(label="あなたの悩み、困りごと、相談したいことを入力してください。")
### ここにサイコパスな熱血コーチの回答を生成するコードを追加


else:
    input_message = st.text_input(label="あなたの悩み、困りごと、相談したいことを入力してください。")
### ここにどんな時でも良い点を見つけて励ますコーチの回答を生成するコードを追加

if st.button("実行"):
    st.divider()

    if selected_item == "サイコパスな熱血コーチ":
        if input_message:
            ### ここにサイコパスな熱血コーチの回答を生成するコードを追加


        else:
            st.error("コーチングしてほしいことを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            ### ここにどんな時でも良い点を見つけて励ますコーチの回答を生成するコードを追加


        else:
            st.error("コーチングしてほしいことを入力してから「実行」ボタンを押してください。")