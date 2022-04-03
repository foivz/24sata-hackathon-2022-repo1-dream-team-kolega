count = 0
file = open('database2.csv', 'r')
lajna = ""

while True:
    count += 1

    line = file.readline()

    if not line:
        break

    lajna = str(line).split("\"\"\",\"\"\"")
    #print(lajna)
    #allProdukt.add(new Baza("kobasa", "50 kn", "https://ferbezar.com/wp-content/uploads/2016/11/slavonska-kobasica1.jpg%22,1));
    ispis = "allProdukt.add(new Baza(\"" + lajna[1] + "\"," + lajna[2] + ",\"" + lajna[0][3:] + "\"," + str(count) + ",\"" + lajna[4][:-4] + "\",\"" + lajna[3] + "\"));"
    print(ispis)

file.close()
