hours = [1.2, 2.5, 4.9, 5.8]
for hour in hours:
    minutes = int(hour * 60)
    seconds = int(minutes * 60)
    print(f"{hour} год = {minutes} хв = {seconds} сек")
