import matplotlib.pyplot as plt

def parse_file(file_name):
    with open(file_name, 'r') as results:

        dct = dict()

        for line in results:
            name, result = line.split(",")
            name = name.casefold()
            result = int(result)
            if name not in dct:
                dct[name] = dict()
                if result == 2:
                    dct[name]["wins"] = 1
                    dct[name]["loses"] = 0
                    dct[name]["ties"] = 0
                    dct[name]["points"] = result
                elif result == 1:
                    dct[name]["wins"] = 0
                    dct[name]["loses"] = 0
                    dct[name]["ties"] = 1
                    dct[name]["points"] = result
                else:
                    dct[name]["wins"] = 0
                    dct[name]["loses"] = 1
                    dct[name]["ties"] = 0
                    dct[name]["points"] = result
            else:
                if result == 2:
                    dct[name]["wins"] += 1
                    dct[name]["points"] += result
                elif result == 1:
                    dct[name]["ties"] += 1
                    dct[name]["points"] += result
                else:
                    dct[name]["loses"] += 1

        return dct


def plot_bar(data):
    sorted_data1 = []

    for names in data:
        sorted_data1.append([(data[names]["points"]), names])
    sorted_data = sorted(sorted_data1, reverse=True)

    X = []
    Y = []

    for value_1 in sorted_data:
        X.append(value_1[1])
        Y.append(value_1[0])

    plt.bar(X, Y)
    plt.title('Results')
    plt.xlabel('Names')
    plt.ylabel('Points')
    plt.show()

try:
    loaded_data = parse_file('test3.txt')
except FileNotFoundError:
    print("Play the game to check results.")
    exit(0)

plot_bar(loaded_data)