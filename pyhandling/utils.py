import requests
import io
import pandas as pd

desired_width = 320
pd.set_option("display.max_columns", 10)

alpha_vantage_url = "https://www.alphavantage.co/query"
my_api_key = "78HSPMNPH3DD3OPD"
my_symbol = "AAPL"
my_symbol_2 = "MSFT"


class RequestsApi(object):
    def __init__(self, base_url, time_series, symbol, interval, outputsize, datatype, apikey):
        self.base_url = base_url
        self.time_series = time_series
        self.symbol = symbol
        self.interval = interval
        self.outputsize = outputsize
        self.datatype = datatype
        self.apikey = apikey

    def intraday(self):
        payload = {
            "function": 'TIME_SERIES_INTRADAY',
            "symbol": self.symbol,
            "interval": self.interval,
            "outputsize": self.outputsize,
            "datatype": self.datatype,
            "apikey": self.apikey
        }

        query_results = requests.get(alpha_vantage_url, payload)
        local_list = pd.read_csv(io.StringIO(query_results.text))
        print("Intraday", local_list.head(n=5))
        return local_list

    def try_print(self):
        print("this is try print", self.head(n=5))
        return self

    def add_symbol(self):
        answer = input("Please enter the stock symbol exactly: ")
        self.insert(1, 'symbol', answer)
        print("add_symbol", self.head(n=5))
        return self

    def pickle_save(self):
        answer = input("Please enter a save name for the new pandas dataframe: ")
        self.to_pickle("./{0}.pkl".format(answer))

    @staticmethod
    def pickle_load():
        answer = input("Please enter the filename you want to load : ")
        loaded_df = pd.read_pickle("./" + answer + ".pkl")
        print("I'm a pickle!!!")
        print("pickle_load", loaded_df.head(n=5))
        return loaded_df


def main():

    new_df = RequestsApi(alpha_vantage_url, "TIME_SERIES_INTRADAY", my_symbol_2, "1min", "compact", "csv", my_api_key)

    df_data0 = RequestsApi.intraday(new_df)
    df_data1 = RequestsApi.try_print(df_data0)
    df_data2 = RequestsApi.add_symbol(df_data1)
    RequestsApi.pickle_save(df_data2)
    df_data3 = RequestsApi.pickle_load()
    RequestsApi.try_print(df_data3)


if __name__ == "__main__":
    main()
