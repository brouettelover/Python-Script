import telnetlib
import configparser

cp_host = configparser.ConfigParser()
cp_vlan = configparser.ConfigParser()

cp_host.read('Host.ini')
cp_vlan.read('Vlan.ini')


def login_switch_cp(switch,tn):
    tn.read_until(b"Username:")
    tn.write(cp_host[switch]['username'].encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(cp_host[switch]['password'].encode('ascii') + b"\n")

def go_to_enable_cp(switch,tn):
    tn.write(b"enable" + b"\n")
    tn.read_until(b"Password: ")
    tn.write(cp_host[switch]['password'].encode('ascii') + b"\n")

def change_hostname_cp(switch, tn):
    tn.write(b"conf t" + b"\n")
    tn.write(b"hostname " + cp_host[switch]['hostname'].encode('ascii') + b"\n")
    tn.write(b"end" + b"\n")

def create_vlan_cp(tn):
    tn.write(b"conf t" + b"\n")
    x = cp_vlan.sections()
    for i in x:
        vlan_name = cp_vlan[i]['name']
        vlan_id = cp_vlan[i]['id']
        tn.write(b"vlan " + vlan_id.encode('ascii') + b"\n")
        tn.write(b"name " + vlan_name.encode('ascii') + b"\n")    
    tn.write(b"end" + b"\n")

def show_run(tn):
    tn.write(b"terminal length 0" + b"\n")
    tn.write(b"show run" + b"\n")

def save(tn):
    tn.write(b"wr" + b"\n")

def end(tn):
    tn.write(b"exit\n")
    #print(tn.read_all().decode('ascii'))

def backup_telnet_cp(switch, tn):
    backup_content = tn.read_all().decode('ascii')
    fichier = open("./backup/" + cp_host[switch]['hostname'] + "_" + cp_host[switch]['ip'] +".txt", "x")
    fichier.write(backup_content)
    fichier.close()

#def clean_backup_cp(switch, tn):
#    with open("./backup/" + cp_host[switch]['hostname'] + "_" + cp_host[switch]['ip'] +".txt", "r+") as f:
#        d = f.readlines()
#        f.seek(0)
#        for i in d:
#            if i != 

def loop_switch():
    x = cp_host.sections() #Récupère la liste des hosts
    for i in x:
        tn = telnetlib.Telnet(cp_host[i]['ip'])
        login_switch_cp(i,tn)
        go_to_enable_cp(i,tn)
        #change_hostname_cp(i,tn)
        #create_vlan_cp(tn)
        show_run(tn)
        save(tn)
        end(tn)
        backup_telnet_cp(i, tn)
        #clean_backup_cp(i, tn)
        




        

def main():
    loop_switch()
#    login_switch_cp()
#    go_to_enable_cp()
#    create_vlan_cp()
##    login_switch()
##    go_to_enable()
##    #no_domain_lookup()
##    #change_hostname()
##    #show_run()
##    create_vlan()
#    end_save() #garder à la fin
    



main()

########################################################### ANCIENNE FONCTION
#
#HOST = "10.10.20.101"
#username = "cisco"
#password = "cisco"
#hostname = "SW1"
#def login_switch():
#    tn.read_until(b"Username:")
#    tn.write(username.encode('ascii') + b"\n")
#    tn.read_until(b"Password:")
#    tn.write(password.encode('ascii') + b"\n")
#
#def go_to_enable():
#    tn.write(b"enable" + b"\n")
#    tn.read_until(b"Password:")
#    tn.write(password.encode('ascii') + b"\n")
#
#
#def no_domain_lookup():
#    tn.write(b"conf t" + b"\n")
#    tn.write(b"no ip domain lookup" + b"\n")
#    tn.write(b"end" + b"\n")
#
#def change_hostname():
#    tn.write(b"conf t" + b"\n")
#    tn.write(b"hostname " + hostname.encode('ascii') + b"\n")
#    tn.write(b"end" + b"\n")
#

#def create_vlan():
#    vlan_sortie = "O"
#    tn.write(b"conf t" + b"\n")
#
#    while vlan_sortie == "O":
#        vlan_name = input("Entrez le nom du vlan : ")
#        vlan_id = input("Entrez le vlan id pour le vlan "  + vlan_name + ": ")
#        tn.write(b"vlan " + vlan_id.encode('ascii') + b"\n")
#        tn.write(b"name " + vlan_name.encode('ascii') + b"\n")
#        vlan_sortie = input("Veux tu continué de créer des vlan ? O/N ")
#    
#    tn.write(b"end" + b"\n")
    