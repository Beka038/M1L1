slov_dict = {
    "ДЕЕ":"шучу",
    "АГРО":"вспыльчивый",
    "СИГМА":"Крутой или такой человек"
}
word = input("Введтите непонятное слово: ").upper()
if word in slov_dict:
    print(slov_dict[word])
else:
    print("Не найдено")
