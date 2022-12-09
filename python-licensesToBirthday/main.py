results = {}
inputData = ""

def read_new_data():
    f = open("inputData.txt", encoding="utf8")
    lines = f.readlines()
    for a in lines:
        if not a:
            break
        b = a.split()
        if len(b) != 2 or "/" not in b[0]:
            continue
        b[1] = convert_data(b[1])
        if not b[1]:
            continue
        global inputData
        inputData += b[0] + " " + b[1] + "\n"
        if b[0] in results:
            if b[1] in results[b[0]]:
                results[b[0]][b[1]] += 1
            else:
                results[b[0]][b[1]] = 1
        else:
            results[b[0]] = {b[1]: 1}
    f.close()


def convert_data(data):
    dataSplit = data.split(".")
    if len(dataSplit) != 3:
        return False
    if len(dataSplit[0]) < 2:
        dataSplit[0] = '0' + dataSplit[0]
    elif len(dataSplit[0]) > 2:
        return False

    if len(dataSplit[1]) < 2:
        dataSplit[0] = '0' + dataSplit[0]
    elif len(dataSplit[1]) > 2:
        return False

    if len(dataSplit[2]) != 4:
        return False
    return dataSplit[0] + '.' + dataSplit[1] + '.' + dataSplit[2]


def create_raport():
    for key, value in results.items():
        if len(value) > 1:
            print(key, value)

def save_data_to_file():
    f = open("birthdate.txt", "w")
    for license, date in results.items():
        date = dict(sorted(date.items(), key=lambda item: -item[1]))
        f.write(license + " " + list(date.keys())[0] + "\n")
    f.close()
    f = open("historicaInputData.txt", "w")
    f.write(inputData)
    f.close()
    print(results)


if __name__ == '__main__':
    read_new_data()
    create_raport()
    save_data_to_file()

