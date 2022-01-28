import decimal
from decimal import Decimal

def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]
    for wi in weather_information:
        a=Decimal(wi['temperature'])
        sum(a)

if __name__ == "__main__":
    main()

# 複数の辞書から、特定のKeyから値を取り出し、さらに合計を出す。ここがわからない。
# 出た結果をSumにすると、folat扱いになる。よって、intにしてもエラーになる。この先がわからない。
# sumが小数点を正確に計算できないため、decimalをつかう、ということはわかった。この先がわからん、、、、。

