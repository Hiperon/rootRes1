import uproot

with uproot.open("../data/results1_short100_coincidences.root") as file:
    print(file.keys())
    print()
    print(file.classnames())
    print()
    print(file["Coincidences"])
    print()
    print(file["Coincidences"].all_members)
    print()
    #print(file["Coincidences"].axis().edges())
    print(file["Coincidences"].values())
    print()
    dane = file["Coincidences"].values(['time1'])
    coin = file["Coincidences"]
    print(coin.typenames())
    coin.show()
    time1 = coin["time1"].array()
    print(*time1)
    #print(file["Coincidences"].errors)