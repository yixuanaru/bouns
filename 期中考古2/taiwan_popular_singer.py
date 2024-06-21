singer=['Jay Chou','Jam Hsiao','JJ Lin','Mayday','A-mei','Jolin Tsai','Hebe Tien']
fans=[105,101,99,150,135,90,140]

jay=['Jolin Tsai','Jam Hsiao','Mayday','A-mei']
jam=['Mayday','A-mei','Jay Chou','JJ Lin']
jj=['Jam Hsiao','Jolin Tsai','Jay Chou','A-mei']
mayday=['Jam Hsiao','A-mei','Hebe Tien','JJ Lin']
amei=['Jay Chou','Jam Hsiao','Mayday']
jolin=['JJ Lin','Jam Hsiao','Jay Chou']
hebe=['Jam Hsiao','Jay Chou','Jolin Hsai','Mayday']
guests=[jay,jam,jj,mayday,amei,jolin,hebe]
debut=[2000,2007,2003,1999,1996,1999,2001]


# 將歌手資訊儲存在字典中
singer_data = {}
for i in range(len(singer)):
    singer_data[singer[i]] = {
        'popularity': fans[i],
        'guests': guests[i],
        'debut_year': debut[i]
    }

# 對2000年及之後出道的歌手按人氣排序
def sort_recent_singers(singer_data):
    recent_singers = {singer: data for singer, data in singer_data.items() if data['debut_year'] >= 2000}
    sorted_singers = sorted(recent_singers.items(), key=lambda x: x[1]['popularity'], reverse=True)
    print("(1) popular singers after 2000:")
    for singer, data in sorted_singers:
        print(f"{singer}: {data['popularity']}")

# 找出作為嘉賓最常出現的歌手
def most_frequent_guest(singer_data):
    guest_counts = {}
    for singer, data in singer_data.items():
        for guest in data['guests']:
            guest_counts[guest] = guest_counts.get(guest, 0) + 1
    most_frequent_guest, count = max(guest_counts.items(), key=lambda x: x[1])
    print(f"\n(2) frequently-appeared guest:")
    print(f"{most_frequent_guest}: {count}")

# 列出曾在彼此演唱會中作為嘉賓的歌手對
def mutual_guests(singer_data):
    singer_pairs = []
    for singer1, data1 in singer_data.items():
        for singer2, data2 in singer_data.items():
            if singer1 != singer2 and singer1 in data2['guests'] and singer2 in data1['guests']:
                singer_pairs.append((singer1, singer2))
    print("\n(3) list of co-guest singer pairs:")
    for pair in singer_pairs:
        print(f"{pair[0]} = {pair[1]}")

# 主程序
sort_recent_singers(singer_data)
most_frequent_guest(singer_data)
mutual_guests(singer_data)