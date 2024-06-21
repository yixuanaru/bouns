import csv

singers = {}

with open('taiwan_popular_singer.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

        
    for row in reader:
        singer_name = row['singer']
        singers[singer_name] = {
            'popularity': int(row['popularity(millions)']),
            'guests': row['guests'].split('|'),
            'debut': int(row['debut'])}

# 1. 將出道年份在2000年（包括2000年）之後的歌手，按照受歡迎程度排序
singers_after_2000 = {singer: data for singer, data in singers.items() if data['debut'] >= 2000}
sorted_singers_after_2000 = sorted(singers_after_2000.items(), key=lambda x: x[1]['popularity'], reverse=True)

print("(i) popular singers after 2000:")
for singer, data in sorted_singers_after_2000:
    print(f"{singer}: {data['popularity']}")

# 2. 找出最常出現在其他歌手演唱會的來賓
guest_count = {}
for singer, data in singers.items():
    for guest in data['guests']:
        guest_count[guest] = guest_count.get(guest, 0) + 1

most_frequent_guest = max(guest_count.items(), key=lambda x: x[1])
print("\n(ii) frequently-appeared guest:")
print(f"{most_frequent_guest[0]}: {most_frequent_guest[1]}")

# 3. 列出曾經互相出現在彼此演唱會上的歌手對
def get_guest_pairs(singers):
    guest_dict = {}
    for singer, data in singers.items():
        guests = data['guests']
        for guest in guests:
            if singer not in guest_dict:
                guest_dict[singer] = set()
            if guest not in guest_dict:
                guest_dict[guest] = set()
            guest_dict[singer].add(guest)
            guest_dict[guest].add(singer)

    pairs = set()
    for singer, guests in guest_dict.items():
        for guest in guests:
            if singer < guest:
                pairs.add(frozenset([singer, guest]))

    return pairs

co_guest_pairs = get_guest_pairs(singers)
print("\nList of co-guest singer pairs:")
print('\n'.join([f"{pair[0]} = {pair[1]}" for pair in sorted(co_guest_pairs)]))