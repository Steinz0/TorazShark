def mac(oneTrame,machine):
    #return adresseMac dest ou src
    res = ""
    for i in range (0+(machine*6),6+(machine*6)):
        res = res + "." + oneTrame[i]
    return res[1:]

def header_lenght(oneTrame):
    
    return int(((oneTrame[14][1])),16)*4

def ip(oneTrame,machine):
    res = ""

    for i in range (26+(machine*4),30+(machine*5)):
        hexa = int(oneTrame[i],16)
        convstr = str(hexa)
        res = res + "." + convstr

    return res[1:]

def version(oneTrame):

    return int(oneTrame[14][0],16)

def ttl(oneTrame):

    return int(oneTrame[22],16)

def protocol_IP(oneTrame):

    res = ""
    if(oneTrame[23] == "01"):
        res = "0x01 ICMP"
    elif(oneTrame[23] == "06"):
        res = "0x06 TCP"
    elif(oneTrame[23] == "11"):
        res = "0x11 UDP"
    else:
        res = oneTrame[23]

    return res

def champs_Internet_Type(oneTrame):
    res = ""

    if(oneTrame[12] == "08" and oneTrame[13] == "00"):
        res = "Protocol IPV4 0x0800"
    elif(oneTrame[12] == "08" and oneTrame[13] == "06"):
        res = "Protocol ARP 0x0806"
    else:
        res = oneTrame[12] + oneTrame[13]

    return res

def ihl(list):
    return int(list[16] + list[17],16) #-20 voir diapo cours

def type_of_service(oneTrame):
    return oneTrame[15]

def identification(oneTrame):
    return oneTrame[18] + oneTrame[19]

def fRagmentation(oneTrame):
    Listres = []
    flag_List = []
    fragment_off = 0
    bintodec = ""

    hexa = oneTrame[20] + oneTrame[21]
    scale = 16
    num_of_bits = 16
    res = 0
    res = bin(int(hexa,scale))[2:].zfill(num_of_bits)

    for i in res:
        Listres.append(i)
    flag_List.append(Listres[0])
    flag_List.append(Listres[1])
    flag_List.append(Listres[2])
    
    for i in Listres[4:] :
        bintodec += i
    
    fragment_off = int(bintodec,2)//8
    
    flag_List.append(str(fragment_off))
    flag_List.append(hexa)

    return flag_List

def affiche_checksum(oneTrame):

    return oneTrame[24] + oneTrame[25]


def checksum_verify(oneTrame):

    taille_entete_ip = 20
    list_a_anlyser = oneTrame[14:14+taille_entete_ip]
    list_transform = []
    i = 0

    while i < len(list_a_anlyser):
        res = list_a_anlyser[i] + list_a_anlyser[i+1]
        list_transform.append(res)
        i += 2

    scale = 16
    num_of_bits = 16
    res = []
    integer_sum = 0
    
    for i in list_transform:
        res.append(bin(int(i,scale))[2:].zfill(num_of_bits))
    
    for i in res :
        integer_sum = integer_sum + int(i,2)

    binary_sum = bin(integer_sum)
    verification = int(binary_sum[4:],2) + int(binary_sum[2:4],2)
    
    if verification == 65535:
        return True
    return False    

def option_IP(onetrame):
    debut = 34 #enteteEthernet+enteteIPv4
    listoption=[]
    option = int(onetrame[debut],16)
    taille_option = int(onetrame[debut+1],16)
    
    if option == 7:
        listoption.append("Type : " + str(option) + " Record Route")
    elif option == 1:
        listoption.append("Type : " + str(option) + "No Operation")
    elif option == 68:
        listoption.append("Type : " + str(option) + "Time Stamp")
    elif option == 131:
        listoption.append("Type " + str(option) + "Loose Rooting")
    elif option == 137:
        listoption.append("Type " + str(option) + "Strict Rounting")
    
    listoption.append("Longueur " + str(taille_option))

    if header_lenght(onetrame) != taille_option + 20:
        listoption.append("Type 0 End of Options List")
    return listoption
