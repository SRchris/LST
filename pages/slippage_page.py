import requests
import numpy as np
from requests.exceptions import JSONDecodeError
import streamlit as st

def get_slippage(amount, srcToken):
    url = f'https://apiv5.paraswap.io/prices?srcToken={srcToken}&srcDecimals=18&destToken=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&destDecimals=18&amount={amount}&side=SELL&network=1'
    try:
        response = requests.get(url)
        data = response.json()
        srcUSD = float(data['priceRoute']['srcUSD'])
        destUSD = float(data['priceRoute']['destUSD'])
        slippage = (srcUSD - destUSD) / destUSD
        return slippage
    except JSONDecodeError:
        print(f'Failed to get data for token {srcToken} at amount {amount}')
        return 1.0  # Set the slippage to 100% if there's an error

def show_slippage_page():
    st.title('Slippage Page')

    amounts = np.logspace(18, 22, num=50, base=10.0)
    tokens = {
    #    'swETH': '0xf951E335afb289353dc249e82926178EaC7DEd78',
     #   'wstETH': '0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0',
      #  'rETH': '0xae78736Cd615f374D3085123A210448E74Fc6393',
      #  'frxETH': '0x5E8422345238F34275888049021821E8E08CAa1f',
        'sETH2': '0xFe2e637202056d30016725477c5da089Ab0A043A',
        'ankrETH': '0xE95A203B1a91a908F9B9CE46459d101078c2c3cb'
    }

    for token_name, token_address in tokens.items():
        slippages = [get_slippage(int(amount), token_address) for amount in amounts]
        slippages = [min(s, 1) for s in slippages]  # Limit slippage to 1

        # Create the plot using streamlit's st.line_chart() function
        data = {'ETH Amount': [a / 10**18 for a in amounts[:len(slippages)]],
                'Slippage (%)': [s * 100 for s in slippages]}
        chart = st.line_chart(data, use_container_width=True)

if __name__ == "__main__":
    show_slippage_page()
