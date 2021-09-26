from pycoingecko import CoinGeckoAPI 
import pandas as pd 
 
cg = CoinGeckoAPI() 
 
 
def sort_by_market_cap(a): 
    coin = cg.get_coins_markets(vs_currency='usd') 
    df_coin = pd.DataFrame(coin, columns=['id', 'market_cap', 'market_cap_rank']) 
    df_coin.set_index('id', inplace=True) 
    return df_coin['market_cap_rank'].nsmallest(a)
