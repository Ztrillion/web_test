import streamlit as st

st.title('Front 테스트')
title = st.text_input('종목을 입력해 주세요',)

if st.button('정보 확인'):
    with st.spinner('Wait for it...'):

        st.success('Done!')
        st.write('The current movie title is : ', title)

    
