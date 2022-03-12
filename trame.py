def trace_to_trames(file):
    trace = open(file, "r")
    nb_trames = 0
    ind_octect = 0
    ind_lines = 0
    list_trames = []

    for line in trace:
        try:
            offset = line.split()[0]
        except IndexError:
            ind_lines += 1
            continue
        try:
            int(offset, 16)
        except ValueError:
            print("Error line : ", ind_lines, " Type : Value offset\n")
            ind_lines += 1
            continue

        if int(offset, 16) == 0:
            nb_trames += 1
            list_trames.append([])
            ind_octect = 0
        elif int(offset, 16) != ind_octect:
            print("Error line : ", ind_lines, " Type : Incorrect offset, offset : ", offset, "\n")
            ind_lines += 1
            continue

        tmp = []
        for octet in line.split()[1:]:

            if len(octet) != 2:
                continue

            try:
                test = int(octet, 16)
            except ValueError:
                continue

            ind_octect += 1
            tmp.append(octet)

        list_trames[nb_trames - 1] = list_trames[nb_trames - 1] + tmp
        ind_lines += 1
        tmp.clear()

    return list_trames

