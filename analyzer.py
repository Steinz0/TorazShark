from trame import trace_to_trames
from Ethernet_IP import *
from Tcp import *
from pHTTP import *

def answer(trame):
    protocol = protocol_IP(trame)
    fragmentIP = fRagmentation(trame)
    reservedIP = fragmentIP[0]
    df = fragmentIP[1]
    mf = fragmentIP[2]
    fragmentOffset = fragmentIP[3]
    hexaFlagIP = fragmentIP[4]

    debut = 14 + header_lenght(trame)

    setDebutTcp(debut)
    setDebutHTTP(debut+thl(trame))


    s = '' #String final contenant l'analyse de la trame

    s += "Entete Ethernet" + "\n\n"
    s += '\t' + "Adresse MAC Destination : " + mac(trame,0) + '\n'
    s += '\t' + "Adresse MAC Source : " + mac(trame,1) + '\n'
    s += '\t' + "Champ Internet Type : " + champs_Internet_Type(trame) + "\n\n"
    
    if champs_Internet_Type(trame) == "Protocol IPV4 0x0800":

        s += "Entete IP" + "\n\n"
        s += '\t' + "Version : " + str(version(trame)) + '\n'
        s += '\t' + "Adresse IP Destination : " + ip(trame,0) + '\n'
        s += '\t' + "Adresse IP Source : " + ip(trame,1) + '\n'
        s += '\t' + "Type of service : " + "0x" + type_of_service(trame) + '\n'
        s += '\t' + "Total Length : " + str(ihl(trame)) + '\n'
        s += '\t' + "Identification : " + "0x" + identification(trame) + '\n'
        s += '\t' + "Flag, Fragment Offset " + "0x" + hexaFlagIP + ' : \n'
        s += "\t\t" + "Reserved : " + reservedIP + '\n'
        s += "\t\t" + "Don't fragment : " + df + '\n'
        s += "\t\t" + "More fragment : " + mf + '\n'
        s += "\t\t" + "Fragment Offset : " + fragmentOffset + '\n'
        s += '\t' + "TTL (Time to live) : " + str(ttl(trame)) + '\n'
        s += '\t' + "Protocole IP : " + protocol + '\n'
        s += '\t' + "Header Length : " + str(header_lenght(trame)) + '\n'
        s += '\t' + "Checksum : " + "0x" + affiche_checksum(trame) + "\n"
        s += '\t' + "Checksum Verify : " + str(checksum_verify(trame)) + "\n\n" 

        if header_lenght(trame) > 20:
            s += '\t' + "Option : " + '\n'
            for o in option_IP(trame):
                s += "\t\t" + o + '\n'

    if protocol == "0x06 TCP":

        flagsTCP = flag_tcp(trame)
        reservedTCP = flagsTCP[0]
        nonce = flagsTCP[1]
        cwr = flagsTCP[2]
        ecnEcho = flagsTCP[3]
        urg = flagsTCP[4]
        ack = flagsTCP[5]
        psh = flagsTCP[6]
        rst = flagsTCP[7]
        syn = flagsTCP[8]
        fin = flagsTCP[9]
        hexaFlagTCP = flagsTCP[10]

        s += "Protocol TCP" + "\n\n"
        s += '\t' + "Port Number Source : " + str(port_number(trame,0)) + '\n'
        s += '\t' + "Port Number Destination : " + str(port_number(trame,1)) + '\n'
        s += '\t' + "Sequence Number : " + str(sequence_number(trame)) + '\n'
        s += '\t' + "Acknowledgment Number : " + str(acknowledgment_number(trame)) + '\n'
        s += '\t' + "Windows : " + str(window(trame)) + '\n'
        s += '\t' + "Checksum TCP : " + cheksum_tcp(trame) + '\n'
        s += '\t' + "Urgent Pointer : " + urgent_pointer(trame) + '\n'
        s += '\t' + "THL : " + str(thl(trame)) + '\n'
        s += '\t' + "Flag TCP : " + hexaFlagTCP + '\n'
        s += "\t\t" + "Reversed : " + reservedTCP + '\n'
        s += "\t\t" + "Nonce : " + nonce + '\n'
        s += "\t\t" + "CWR (Congestion Window Reduced) : " + cwr + '\n'
        s += "\t\t" + "ECN-Echo : " + ecnEcho + '\n'
        s += "\t\t" + "URG (Urgent) : " + urg + '\n'
        s += "\t\t" + "ACK (Acknowledgment) : " + ack + '\n'
        s += "\t\t" + "PSH (Push) : " + psh + '\n'
        s += "\t\t" + "RST (Reset) : " + rst + '\n'
        s += "\t\t" + "SYN : " + syn + '\n'
        s += "\t\t" + "FIN : " + fin + '\n'


        if (port_number(trame,0) == 80 or port_number(trame,1) == 80) and thl(trame)+debut < len(trame):

            s += "HTTP " + "\n\n"
            for line in hex_to_ascii(trame):
                s += '\t'
                for oct in line:
                    s += oct   
                    s += ' '
                s += '\n'

    return s