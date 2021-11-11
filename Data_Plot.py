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


def draw_plot_bar(data):
    sorted_data = []

    for name in data:
        sorted_data.append([(data[name]["points"]), name.strip()])
    sorted_data = sorted(sorted_data, reverse=True)

    sorted_data = sorted_data[:5]

    X = []
    Y = []

    for value in sorted_data:
        X.append(value[1])
        Y.append(value[0])


    plt.bar(X, Y)
    plt.title('Results')
    plt.xlabel('Names')
    plt.ylabel('Points')
    plt.show()

try:
    loaded_data = parse_file('results.txt')
except FileNotFoundError:
    print("Play the game to check results.")
    exit(0)

draw_plot_bar(loaded_data)