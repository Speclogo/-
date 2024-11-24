
from tkinter import *
from tkinter import messagebox as mb
import requests

def get_crypto_price():
    crypto = crypto_var.get().lower()
    currency = currency_var.get().lower()

    if crypto:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}')
            response.raise_for_status()
            data = response.json()

            if crypto in data:
                price = data[crypto][currency]
                price_label.config(text=f"Текущий курс {crypto.capitalize()} к {currency.upper()}: {price:.2f} {currency.upper()}")
            else:
                mb.showerror("Ошибка", "Криптовалюта не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите криптовалюту")


window = Tk()
window.title("Курс криптовалют")
window.geometry("600x300")

Label(window, text="Выберите валюту для расчета").pack(padx=10, pady=5)

crypto_var = StringVar(window)
crypto_var.set("Bitcoin")

crypto_options = ["Bitcoin", "Ethereum", "Ripple", "Litecoin", "Cardano"]
crypto_menu = OptionMenu(window, crypto_var, *crypto_options)
crypto_menu.pack(padx=10, pady=10)

Label(window, text="Выберите основную валюту").pack(padx=10, pady=5)

currency_var = StringVar(window)
currency_var.set("USD")

currency_options = ["USD", "RUB", "EUR"]
currency_menu = OptionMenu(window, currency_var, *currency_options)
currency_menu.pack(padx=10, pady=10)

Button(window, text="Получить курс обмена", command=get_crypto_price).pack(padx=10, pady=10)

price_label = Label(text="", font=("Arial", 14))
price_label.pack(padx=10, pady=10)

window.mainloop()

