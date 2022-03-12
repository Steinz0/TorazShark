def setDebutTcp(deb):
    global debut
    debut=deb

def port_number(oneTrame,machine):
    res = oneTrame[debut + 2*machine]+ oneTrame[debut + 1 + 2*machine]
    return int(res,16)

def sequence_number(oneTrame):
    res = ""
    first_byte_s=debut+4

    for i in range(first_byte_s,first_byte_s+4):
        res=res+oneTrame[i]
    return int(res,16)

def acknowledgment_number(oneTrame):
    first_byte_a = debut+8
    res = ""
    for i in range(first_byte_a,first_byte_a+4):
        res=res+oneTrame[i]
    return int(res,16)

def window(oneTrame):
    first_byte_w = debut+14
    res = ""
    for i in range(first_byte_w,first_byte_w+2):
        res = res + oneTrame[i]
    return int(res,16)

def cheksum_tcp(oneTrame):
    first_byte_ctp = debut+16
    res = ""

    for i in range(first_byte_ctp,first_byte_ctp+2):
        res = res + oneTrame[i]
    return res

def urgent_pointer(oneTrame):
    first_byte_up = debut+18
    res = ""
    for i in range(first_byte_up,first_byte_up+2):
        res = res + oneTrame[i]
    return res

def thl(oneTrame):
    #extraction des 4 premier bit de l'hexa
    hexa = oneTrame[debut+12][0]
    scale = 16
    num_of_bits = 8
    res = 0
    res = bin(int(hexa,scale))[2:].zfill(num_of_bits)
    thl= int(res,2)*4
    return thl

def flag_tcp(oneTrame):
    Listres = []
    hexa = oneTrame[debut+12] + oneTrame[debut+13]

    scale = 16
    num_of_bits = 16
    res = 0
    res = bin(int(hexa,scale))[2:].zfill(num_of_bits)
    #Listres.append(res[4:7])
    #[Listres for i in res[7:]]
    Listres.append(res[4:7])
    Listres = Listres + [i for i in res[7:]] + [hexa]
    
    return Listres