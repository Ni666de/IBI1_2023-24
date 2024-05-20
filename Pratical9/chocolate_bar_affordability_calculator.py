def chocolate_bar_affordability(total_money, price_per_bar):
    num_bars = total_money // price_per_bar
    change = total_money % price_per_bar
    return num_bars, change

total_money = 100  
price_per_bar = 7  
bars, change = chocolate_bar_affordability(total_money, price_per_bar)
print(f"You can buy {bars} chocolate bars and you will have {change} left as change.")
