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

#1 全国の平均気温。どうしようもないので、すでに提出されている方のコードを参照
    ab = [temperature.get('temperature') for temperature in weather_information]
    # print(ab)
    count = len(weather_information)
    # print(count)
    print(sum(ab)/count)

#2　大阪府のすべての駅名をカンマ区切りで出力 ※コード参照
    oosaka = [x for x in weather_information if x['prefecture'] == '大阪府']
    # print(oosaka)
    get_oosaka_station = [station.get('station') for station in oosaka]
    print(get_oosaka_station)

# Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fuku = [x for x in weather_information if x['prefecture'] == '福岡県']
    # print(fuku)
    fuku_kion = [prefecture.get('temperature') for prefecture in fuku]
    # print(fuku_kion)
    fuku_count = len(fuku_kion)
    # print(fuku_count)
    kotae = sum(fuku_kion)/fuku_count
    print(kotae)

    # count_fuku = len([x for x in weather_information if x['prefecture'] == '福岡県'])
    # print(count_fuku)

    'temperature'


if __name__ == "__main__":
    main()

# 複数の辞書から、特定のKeyから値を取り出し、さらに合計を出す。ここがわからない。
# 出た結果をSumにすると、folat扱いになる。よって、intにしてもエラーになる。この先がわからない。
# sumが小数点を正確に計算できないため、decimalをつかう、ということはわかった。この先がわからん、、、、。

# Q1. 全国の平均気温を計算してください(9.5となればOK)
# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
# Q3. 福岡県の平均気温を計算してください(14.0となればOK)

list_=[6,6,8,9,6]
print(6,6,8,9,6)
print(*list_)
print(*list_,"\n")
