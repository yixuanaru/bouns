import csv

def load_singer_data(csvfile):
    singer_data = {}
    reader = csv.reader(csvfile)
    header = next(reader)  # 跳過標頭列

    for row in reader:
        name = row[0]
        popularity = int(row[1].split('(')[0])
        guests = row[2].split('|')
        debut_year = int(row[3])
        singer_data[name] = {'popularity': popularity, 'guests': guests, 'debut': debut_year}
    return singer_data

def sort_recent_singers(singer_data):
    recent_singers = {name: data for name, data in singer_data.items() if data['debut'] >= 2000}
    sorted_singers = sorted(recent_singers.items(), key=lambda x: x[1]['popularity'], reverse=True)
    for name, data in sorted_singers:
        print(f"{name}: {data['popularity']} 萬粉絲, 出道年份: {data['debut']}")

def find_most_frequent_guest(singer_data):
    guest_counts = {}
    for singer, data in singer_data.items():
        for guest in data['guests']:
            guest_counts[guest] = guest_counts.get(guest, 0) + 1
    most_frequent_guest, count = max(guest_counts.items(), key=lambda x: x[1])
    print(f"最常被邀請的客座歌手是: {most_frequent_guest}, 被邀請次數: {count}")

def list_mutual_guests(singer_data):
    mutual_guests = {}
    for singer1, data1 in singer_data.items():
        for singer2, data2 in singer_data.items():
            if singer1 != singer2 and singer1 in data2['guests'] and singer2 in data1['guests']:
                pair = tuple(sorted([singer1, singer2]))
                mutual_guests[pair] = True
    for pair in mutual_guests:
        print(f"{pair[0]} 和 {pair[1]} 曾經互相在對方的演唱會中擔任過客座")

# 讀取 CSV 檔案
with open('taiwan_popular_singer.csv', 'r') as csvfile:
    singer_data = load_singer_data(csvfile)

# 回答問題
print("問題 1: 根據人氣排序 2000 年後出道的歌手")
sort_recent_singers(singer_data)
print("\n問題 2: 最常被邀請的客座歌手")
find_most_frequent_guest(singer_data)
print("\n問題 3: 列出互相擔任過客座的歌手組合")
list_mutual_guests(singer_data)
