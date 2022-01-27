# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

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
        if 'prefecture' == '大阪府':
            print(wi)

# やりたいことは、辞書の中から、'prefecture'かつ大阪府を取り出し、さらに、'station'を出力させる
# if 文を使えばいいのか。書き方が全くわからない。腹立たしい。

if __name__ == "__main__":
    main()
