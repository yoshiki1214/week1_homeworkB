def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]
    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    # 気温データを抽出
    national_temps = [data["temperature"] for data in weather_information]
    # 平均気温を計算し、出力
    national_ave_temp = sum(national_temps) / len(national_temps)
    print(national_ave_temp)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    # 大阪府の駅名を抽出し、カンマ区切りで出力
    osaka_stations = [data["station"] for data in weather_information if data["prefecture"] == "大阪府"]
    print(",".join(osaka_stations))

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    # 福岡県の気温を抽出し、平均気温を計算、算出
    fukuoka_temps = [data["temperature"] for data in weather_information if data["prefecture"] == "福岡県"]
    fukuoka_ave_temp = sum(fukuoka_temps) / len(fukuoka_temps)
    print(fukuoka_ave_temp)


if __name__ == "__main__":
    main()
