# 必要なモジュールのインポート

# 環境変数の読み込み
from dotenv import load_dotenv

# ChatOpenAIのインポート
from langchain_openai import ChatOpenAI

# プロンプトテンプレート
from langchain_core.prompts import ChatPromptTemplate

# メッセージ
from langchain_core.messages import SystemMessage, HumanMessage

# Streamlitのインポート
import streamlit as st

# 環境変数を読み込み
load_dotenv()

# タイトルを設定
st.title("Chapter6：【提出課題】 AIコーチアプリ")

# 動作モード1: サイコパスな熱血コーチの説明を設定
st.write("##### 動作モード1: サイコパスな熱血コーチ")
st.write("妥協のない厳しいコーチングを行います。")

# 動作モード2: どんな時でも良い点を見つけて励ますコーチの説明を設定
st.write("##### 動作モード2: どんな時でも良い点を見つけて励ますコーチ")
st.write("あなたに寄り添ったコーチングを行います。")

# ラジオボタンで動作モードを選択
selected_item = st.radio(
    "好みのコーチを選んでください。",
    ["サイコパスな熱血コーチ", "どんな時でも良い点を見つけて励ますコーチ"]
)

# 入力メッセージを設定
input_message = st.text_input(label="あなたの悩み、困りごと、相談したいことを入力してください。")

# サイコパスな熱血コーチのsystem templateを設定
system_template_hotblooded = """
あなたは、サイコパスな熱血コーチです。ユーザーからの質問に300文字以内で回答してください。
感情や思い込みに流されず、冷静に事実を直視して立ち向かうためのアドバイスをして下さい。
ちょっとした失敗や挫折に対して、「成功するまで諦めない、諦めた時点で失敗、失敗は成功の糧」という信念を持って、前向きにアドバイスをして下さい。"""
# サイコパスな熱血コーチのmessagesを設定
messages_hotblooded = [SystemMessage(content=system_template_hotblooded), HumanMessage(content=input_message)]

# どんな時でも良い点を見つけて励ますコーチのsystem templateを設定
system_template_encouraging = """
あなたは、どんな時でも良い点を見つけて励ますコーチです。ユーザーからの質問に300文字以内で回答してください。
思い詰めたり、ネガティブなループに陥らないように、積極的なアドバイスをして下さい。
過去にこだわったり、起こってもない将来に不安になることなく、今を生きるためのアドバイスをして下さい。
個人レベルで視点で考えるのではなく、人類全体、地球、宇宙などの大きな視点、長期的な時間軸で考えるようにして下さい。"""

# どんな時でも良い点を見つけて励ますコーチのmessagesを設定
messages_encouraging = [SystemMessage(content=system_template_encouraging), HumanMessage(content=input_message)]

# ラジオボタンで選択した動作モードに応じてpromptを選択
messages = []
if input_message:
    if selected_item == "サイコパスな熱血コーチ":
        messages = messages_hotblooded
    elif selected_item == "どんな時でも良い点を見つけて励ますコーチ":
        messages = messages_encouraging
    else:
        st.error("動作モードを選択してください。")

st.divider()

# 実行ボタンを押したら回答を生成
if st.button("実行"):
    if messages:
        # LLMを利用した回答生成
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        result = llm.invoke(messages)
        st.write(result.content)
    else:
        st.error("コーチングしてほしいことを入力してから「実行」ボタンを押してください。")
