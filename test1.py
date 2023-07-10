#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import time

st.title('Webページ')
st.caption('これはテストアプリです')
st.subheader('自己紹介')
st.text('こんにちは！\n''よろしくお願いします！')

"""
# 章
## 節
### 構

"""

code = '''
import streamlit as st

st.title('Webアプリ')
'''
st.code(code, language='python')

df1 = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

#表
st.sidebar.dataframe(df1.style.highlight_max(axis=0), width=500, height=200)

#グラフ
st.sidebar.bar_chart(df2)

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteratin {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
'Done!!'

#画像
image = Image.open('yonedu.jpg')
st.image(image, width=200)

with st.form(key='profile_form'):
    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    #セレクトボックス
    age_category = st.selectbox('年齢層', ('こども（18歳未満）', '大人（18歳以上）'))
    
    #ラジオボタン
    sexial_category = st.radio('性別', ('男', '女'))
    
    #複数選択
    hobby = st.multiselect('趣味', ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', 'ゲーム', '料理'))

    #チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    
    #スライダー
    height =st.slider('身長', min_value=110, max_value=210)
    
    #日付
    #date = st.date_input('誕生日', datetime.date(2023, 7, 4))
    
    #カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')
    
    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書類を送りました！')
        st.text(f'年齢層: {age_category}')
        st.text(f'性別: {sexial_category}')
        st.text(f'趣味: {", ".join(hobby)}')
        #st.write(f'誕生日: {date}')


# In[ ]:




