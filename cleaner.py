from csv import reader,writer
# open file in read mode
with open('items.csv', 'r', encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = list(reader(read_obj))
    # Iterate over each row in the csv using reader object

items=[]

for i in csv_reader:
    row=[]
    row.append(i[1])
    row.append(0.0 if i[2]=='None' else float(i[2].replace('$', '').strip()))
    row.append(0.0 if i[3]=='None' else float(i[3]))
    row.append(0.0 if i[4]=='None' else int(i[4]))
    row.append(1 if " ".join(i).lower().find("parabens") > -1 else 0)
    row.append(1 if " ".join(i).lower().find("retinol") > -1 else 0)
    row.append(1 if " ".join(i).lower().find("phthalates") > -1 else 0)
    row.append(1 if " ".join(i).lower().find("hyaluronic acid") > -1 else 0)
    row.append(1 if " ".join(i).lower().find("ceramides") > -1 else 0)
    row.append(1 if " ".join(i).lower().find("argan") > -1 else 0)
    row.append(i[len(i)-2])

    items.append(row)

with open('data.csv', 'w') as f:
    write = writer(f)
    write.writerows(items)