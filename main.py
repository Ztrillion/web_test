import streamlit as st
import requests

BINANCE_API='https://api.binance.com'
PING='/api/v1/ping'
TIMETICKER='/api/v1/ticker/24hr'
BTCUSDT = {'symbol': 'BTCUSDT'}

btc_re = requests.get(BINANCE_API+TIMETICKER)

st.title('Front 테스트')
title = st.text_input('종목을 입력해 주세요',)

if st.button('정보 확인'):
    with st.spinner('Wait for it...'):
        if btc_re.json()[0]["symbol"] == "BNBBTC":
            st.write(f'{title}종목의 정보입니다. : ', btc_re.json()[0]["symbol"])
        else : 
            st.write(f'{title}종목의 정보입니다. : ', btc_re.json()[3])

    
