- [ ] 日本の九九表
- 要件
下記のような出力が得られる kuku_1.py を実装してください。

$ python kuku_1.py
1 2 3 4 5 6 7 8 9 
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36 
5 10 15 20 25 30 35 40 45 
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81 

- [ ] 九九表の拡張
- 要件
- 下記のような出力が得られる kuku_2.py を実装してください
- 任意の行数および任意の列数での掛け算の結果が得られます 
- 出力例1
- 
$ python kuku_2.py
行数を入力してください: 4
列数を入力してください: 6
1 2 3 4 5 6 
2 4 6 8 10 12 
3 6 9 12 15 18 
4 8 12 16 20 24 

-出力例2
$ python kuku_2.py
行数を入力してください: 12
列数を入力してください: 12
1 2 3 4 5 6 7 8 9 10 11 12 
2 4 6 8 10 12 14 16 18 20 22 24 
3 6 9 12 15 18 21 24 27 30 33 36 
4 8 12 16 20 24 28 32 36 40 44 48 
5 10 15 20 25 30 35 40 45 50 55 60 
6 12 18 24 30 36 42 48 54 60 66 72 
7 14 21 28 35 42 49 56 63 70 77 84 
8 16 24 32 40 48 56 64 72 80 88 96 
9 18 27 36 45 54 63 72 81 90 99 108 
10 20 30 40 50 60 70 80 90 100 110 120 
11 22 33 44 55 66 77 88 99 110 121 132 
12 24 36 48 60 72 84 96 108 120 132 144 

- [ ] きれいな九九表
- 要件
- 下記のような出力が得られる beautiful_kuku.py を実装してください 
- きれいに整っているので見やすくなっています 
- ①式が表示されている 
- ②結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい 
- ③※結果が3桁の場合は崩れてもOKです

- 出力例 
- 行数を入力してください: 9 
- 列数を入力してください: 9
- 
1 x 1 =  1 | 2 x 1 =  2 | 3 x 1 =  3 | 4 x 1 =  4 | 5 x 1 =  5 | 6 x 1 =  6 | 7 x 1 =  7 | 8 x 1 =  8 | 9 x 1 =  9 | 
1 x 2 =  2 | 2 x 2 =  4 | 3 x 2 =  6 | 4 x 2 =  8 | 5 x 2 = 10 | 6 x 2 = 12 | 7 x 2 = 14 | 8 x 2 = 16 | 9 x 2 = 18 | 
1 x 3 =  3 | 2 x 3 =  6 | 3 x 3 =  9 | 4 x 3 = 12 | 5 x 3 = 15 | 6 x 3 = 18 | 7 x 3 = 21 | 8 x 3 = 24 | 9 x 3 = 27 | 
1 x 4 =  4 | 2 x 4 =  8 | 3 x 4 = 12 | 4 x 4 = 16 | 5 x 4 = 20 | 6 x 4 = 24 | 7 x 4 = 28 | 8 x 4 = 32 | 9 x 4 = 36 | 
1 x 5 =  5 | 2 x 5 = 10 | 3 x 5 = 15 | 4 x 5 = 20 | 5 x 5 = 25 | 6 x 5 = 30 | 7 x 5 = 35 | 8 x 5 = 40 | 9 x 5 = 45 | 
1 x 6 =  6 | 2 x 6 = 12 | 3 x 6 = 18 | 4 x 6 = 24 | 5 x 6 = 30 | 6 x 6 = 36 | 7 x 6 = 42 | 8 x 6 = 48 | 9 x 6 = 54 | 
1 x 7 =  7 | 2 x 7 = 14 | 3 x 7 = 21 | 4 x 7 = 28 | 5 x 7 = 35 | 6 x 7 = 42 | 7 x 7 = 49 | 8 x 7 = 56 | 9 x 7 = 63 | 
1 x 8 =  8 | 2 x 8 = 16 | 3 x 8 = 24 | 4 x 8 = 32 | 5 x 8 = 40 | 6 x 8 = 48 | 7 x 8 = 56 | 8 x 8 = 64 | 9 x 8 = 72 | 
1 x 9 =  9 | 2 x 9 = 18 | 3 x 9 = 27 | 4 x 9 = 36 | 5 x 9 = 45 | 6 x 9 = 54 | 7 x 9 = 63 | 8 x 9 = 72 | 9 x 9 = 81 | 


- [ ] 天気情報の分析
- 要件 
- 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています 
- このデータを使って3つの問を満たす実装をしてください

def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
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

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


if __name__ == '__main__':
    main()