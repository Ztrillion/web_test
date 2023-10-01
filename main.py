import streamlit as st
import requests
import pandas as pd
import time

BINANCE_API = 'https://api.binance.com'
TIMETICKER = '/api/v3/ticker/24hr'
BTCUSDT = {'symbol': 'BTCUSDT'}

def get_btc_data():
    btc_response = requests.get(BINANCE_API + TIMETICKER, params=BTCUSDT)
    return btc_response.json()

def get_all_data():
    all_response = requests.get(BINANCE_API + TIMETICKER)
    return all_response.json()

def main():

    st.title('비트코인 투자정보')
    btc_data = get_btc_data()
    st.markdown(
        f"<div style='display: flex; justify-content: start;'>"
        f"<p style='margin: 0; margin-right: 50px'>최근 거래 가격: <strong>{float(btc_data['lastPrice']):.2f} USDT</strong></p>"
        f"<p style='margin: 0;'>24시간 거래량: <strong>{float(btc_data['volume']):.2f} BTC</strong></p>"
        f"</div>", 
        unsafe_allow_html=True
    )

    tradingview_embed_url = "https://www.tradingview.com/widgetembed/?frameElementId=tradingview_7ed12&symbol=BINANCE:BTCUSDT&interval=D&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=%5B%5D&theme=light&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en&utm_source=www.tradingview.com&utm_medium=widget_new&utm_campaign=chart&utm_term=BINANCE:BTCUSDT"
    st.markdown(f'<iframe src="{tradingview_embed_url}" style="width: 100%; height: 500px;"></iframe>', unsafe_allow_html=True)

    st.subheader('BINANCE 등락률 TOP10')
    
    all_tickers = get_all_data()

    usdt_tickers = [ticker for ticker in all_tickers if 'USDT' in ticker['symbol']]

    top_usdt_tickers = sorted(usdt_tickers, key=lambda x: float(x['priceChangePercent']), reverse=True)[:10]

    data = [
        [
            ticker['symbol'],
            f"$ {float(ticker['lastPrice']):,.8f} USDT" if float(ticker['lastPrice']) < 0.0001 else f"$ {float(ticker['lastPrice']):,.4f} USDT",
            f"{int(round(float(ticker['priceChangePercent'])))}%",
            f"$ {float(ticker['quoteVolume']):,.2f} USDT"
        ] for ticker in top_usdt_tickers
    ]
    df = pd.DataFrame(data, columns=['종목', '가격(USDT)', '등락률(%)', '거래량(USDT)'])

    st.table(df)

    time.sleep(5)
    st.experimental_rerun()

if __name__ == "__main__":
    main()
