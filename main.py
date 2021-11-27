import streamlit as st
import time

st.title('Streamlit 入門')
st.sidebar.write('Interactive windows')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの好きな数字は、', text, 'です。'
'コンディション', condition
