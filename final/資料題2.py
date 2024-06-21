import csv
from collections import defaultdict

# 檢查CSV文件是否存在於當前目錄中
import os
print(f"Current working directory: {os.getcwd()}")
print(f"Files in current directory: {os.listdir()}")

# 讀取 CSV 檔案
singers = {}
try:
    with open('taiwan_popular_singer.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # 檢查列名
        print("CSV Headers:", reader.fieldnames)
        
        for row in reader:
            singer_name = row['singer']
            singers[singer_name] = {
                'popularity': int(row['popularity(millions)']),
                'guests': row['guests'].split('|'),
                'debut': int(row['debut'])
            }
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")


# 1. 將出道年份在2000年（包括2000年）之後的歌手，按照受歡迎程度排序
singers_after_2000 = {singer: data for singer, data in singers.items() if data['debut'] >= 2000}
sorted_singers_after_2000 = sorted(singers_after_2000.items(), key=lambda x: x[1]['popularity'], reverse=True)

print("\n(i) popular singers after 2000:")
for singer, data in sorted_singers_after_2000:
    print(f"{singer}: {data['popularity']}")

# 2. 找出最常出現在其他歌手演唱會的來賓
guest_count = defaultdict(int)
for singer, data in singers.items():
    for guest in data['guests']:
        guest_count[guest] += 1

'''# 確認來賓計數是否正確
print("\nGuest count:")
for guest, count in guest_count.items():
    print(f"{guest}: {count}")'''

# 確保 guest_count 不為空
if guest_count:
    most_frequent_guest = max(guest_count, key=guest_count.get)
    print("\n(ii) frequently-appeared guest:")
    print(f"{most_frequent_guest}: {guest_count[most_frequent_guest]}")
else:
    print("\n(ii) No guests found")

# 3. 列出曾經互相出現在彼此演唱會上的歌手對
def get_guest_pairs(singers):
    guest_dict = defaultdict(set)
    for singer in singers:
        guests = singer['guests'].split('/')
        for guest in guests:
            guest_dict[singer['singer']].add(guest)
            guest_dict[guest].add(singer['singer'])

    pairs = set()
    for singer, guests in guest_dict.items():
        for guest in guests:
            if singer < guest:
                pairs.add(frozenset([singer, guest]))

    return pairs

co_guest_pairs = get_guest_pairs(singers)
print("\nList of co-guest singer pairs:")
print('\n'.join([f"{pair[0]} = {pair[1]}" for pair in sorted(co_guest_pairs)]))