import requests
from settings import project_settings


class CryptorankCoinTracker:
    def __init__(self):
        self.token = project_settings.get("CRYPTORANK_TOKEN")
        if not self.token:
            raise Exception("Failed to get CRYPTORANK_TOKEN from settings")
        self.coin_id = project_settings.get("COIN_ID")
        self.starting_coin_balance = project_settings.get("STARTING_COIN_BALANCE")
        self.starting_price_usd = project_settings.get("STARTING_PRICE_USD")
        if not self.coin_id or not self.starting_coin_balance or not self.starting_price_usd:
            raise Exception("Coin settings not configured")

    def get_coin_info(self):
        try:
            response = requests.get(
                f"https://api.cryptorank.io/v1/currencies/{self.coin_id}?api_key={self.token}"
            ).json()
        except:
            response = None
        if response is None or not len(response) or not response["status"]["success"]:
            raise Exception("Bad response received")
        return {
            "name": response["data"]["name"],
            "symbol": response["data"]["symbol"],
            "price": response["data"]["values"]["USD"]["price"]
        }

    def compare_prices(self):
        coin_info = self.get_coin_info()
        message_list = [
            f"Монета: {coin_info['name']} ({coin_info['symbol']})",
            f"Начальная цена: {self.starting_price_usd} USD",
            f"Текущая цена: {coin_info['price']} USD",
            "",
            f"Прирост: {((coin_info['price'] / self.starting_price_usd) - 1) * 100} %",
            "",
            f"Начальный баланс: {self.starting_coin_balance * self.starting_price_usd} USD",
            f"Текущий баланс: {self.starting_coin_balance * coin_info['price']} USD",
        ]
        return "\n".join(message_list)
