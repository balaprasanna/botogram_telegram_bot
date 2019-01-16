TOKEN = "796078392:AAFUgDfdfEy9O3I8wbC2vjsF-FI4TOVkSjI"

from util import *

import botogram
bot = botogram.create(TOKEN)

coindct = construct_coin_dct()

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Hello world")

@bot.command("price")
def price_command(chat, message, args):
    """Get current price of Crypto currencies."""
    
    usage = """
    Usage: /price <coinname>
    Example:  /price bitcoin
    Example:  /price bitcoin litecoin
    """
    if len(args) < 1: 
        chat.send(usage)
        return

    coinname  = args[0]
    price = getprice(coinname, coindct)
    chat.send(f"The price of {coinname} is $ {price}" )


if __name__ == "__main__":
    bot.run()


