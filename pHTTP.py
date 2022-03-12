def setDebutHTTP(deb):
    global debut
    debut = deb

def hex_to_ascii(onetrame):
    list_ascii = []
    new_list = []
    res = ""

    for i in range(debut,len(onetrame)):
        if onetrame[i] == "20":
            var_test = bytes.fromhex(res).decode('utf-8')
            new_list.append(var_test)
            res = ""
        elif onetrame[i]  == "0d":
            if onetrame[i+1] == "0a":
                if onetrame[i+2] == "0d":
                    if onetrame[i+3] == "0a":
                        var_test = bytes.fromhex(res).decode('utf-8')
                        new_list.append(var_test)
                        if new_list[0][0] == '\n':
                            new_list[0] = new_list[0][1:]
                        list_ascii.append(new_list)
                        break
                else:
                    var_test =  bytes.fromhex(res).decode('utf-8')
                    new_list.append(var_test)
                    if new_list[0][0] == '\n':
                        new_list[0] = new_list[0][1:]
                    list_ascii.append(new_list)
                    new_list = []
                    res = ""
        else:
            res += onetrame[i]
    return list_ascii
