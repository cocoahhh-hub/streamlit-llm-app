from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain_openai import ChatOpenAI

import streamlit as st

#サイコパスな熱血コーチのsystem templateを設定
system_template_hotblooded = """
あなたは、サイコパスな熱血コーチです。ユーザーからの質問に100文字以内で回答してください。
感情や思い込みに流されず、冷静に事実を直視して立ち向かうためのアドバイスをして下さい。
ちょっとした失敗や挫折に対して、「成功するまで諦めない、諦めた時点で失敗、失敗は成功の糧」という信念を持って、前向きにアドバイスをして下さい。"""

#どんな時でも良い点を見つけて励ますコーチのsystem templateを設定
system_template_encouraging = """
あなたは、どんな時でも良い点を見つけて励ますコーチです。ユーザーからの質問に100文字以内で回答してください。
思い詰めたり、ネガティブなループに陥らないように、積極的なアドバイスをして下さい。
過去にこだわったり、起こってもない将来に不安になることなく、今を生きるためのアドバイスをして下さい。
個人レベルで視点で考えるのではなく、人類全体、地球、宇宙などの大きな視点、長期的な時間軸で考えるようにして下さい。"""

# タイトルを設定
st.title("Chapter6：【提出課題】 AIコーチアプリ")

# 動作モード1: サイコパスな熱血コーチの説明を設定
st.write("##### 動作モード1: サイコパスな熱血コーチ")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで厳しいアドバイスをもらえます。")

# 動作モード2: どんな時でも良い点を見つけて励ますコーチの説明を設定
st.write("##### 動作モード2: どんな時でも良い点を見つけて励ますコーチ")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで元気づけてもらえます。")

# ラジオボタンで選択した動作モードに応じてpromptを選択
if selected_item == "サイコパスな熱血コーチ":
    messages = prompt_hotblooded.format_prompt(input_message).to_messages()
elif selected_item == "どんな時でも良い点を見つけて励ますコーチ":
    messages = prompt_encouraging.format_prompt(input_message).to_messages()
else:
    st.error("動作モードを選択してください。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["サイコパスな熱血コーチ", "どんな時でも良い点を見つけて励ますコーチ"]
)

st.divider()

input_message = st.text_input(label="あなたの悩み、困りごと、相談したいことを入力してください。")

# 実行ボタンを押したら回答を生成
if st.button("実行"):
    st.divider()

    if selected_item == "サイコパスな熱血コーチ":
        if input_message:
            prompt_hotblooded = ChatPromptTemplate.from_messages([
                SystemMessagePromptTemplate.from_template(system_template_hotblooded),
                HumanMessagePromptTemplate.from_template(input_message),
            ])
            messages = prompt_hotblooded.format_prompt(input_message).to_messages()
        else:
            st.error("コーチングしてほしいことを入力してから「実行」ボタンを押してください。")
    elif selected_item == "どんな時でも良い点を見つけて励ますコーチ":
        if input_message:
            prompt_encouraging = ChatPromptTemplate.from_messages([
                SystemMessagePromptTemplate.from_template(system_template_encouraging),
                HumanMessagePromptTemplate.from_template(input_message),
            ])
            messages = prompt_encouraging.format_prompt(input_message).to_messages()
        else:
            st.error("コーチングしてほしいことを入力してから「実行」ボタンを押してください。")

    # LLMを利用した回答生成
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    result = llm(messages)
    st.write(result.content)
else:
    st.error("コーチングしてほしいことを入力してから「実行」ボタンを押してください。")
