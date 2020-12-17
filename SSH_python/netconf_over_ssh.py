#from device_info import ios_ex1
from ncclient import manager
import xmltodict
from xml.dom import minidom

netconf_filter = open("filter-ietf-interfaces.xml").read()

with manager.connect(
    host="172.16.30.56",
    port=830,
    username="cisco",
    password="cisco",
    hostkey_verify=False ) as m:

    print("COOL TO DO THAT : ")
    # for capability in m.server_capabilities:
    #     print(capability)

#m.close_sessions()



# Get Confi and sate info for intaface
    #netconf_reply = m.get_config(source='running')
    netconf_reply = m.get_config(source='running').data_xml
    with open("%s.xml" , 'w') as f:
        f.write(netconf_reply)

    #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    print(netconf_reply)
    intf_details = xmltodict.parse(netconf_reply)["data"]
    #with open('./netconf_reply.xml') as fd:
    #    intf_details = xmltodict.parse(fd.read())

    #print(intf_details)
    intf_config = intf_details["interfaces"]
    intf_info = intf_details["interfaces-state"]["interface"]

    print("")
    print("Interface Details:")
    print("  Name:{}".format(intf_config["name"]))
    print("  Description:{}".format(intf_config["Description"]))
    print("  Type:{}".format(intf_config["Type"]["#text"]))
    print("  MAC Address:{}".format(intf_config["phys-address"]))
    print("  Packets Input:{}".format(intf_config["statistics"]["in-unicast-pkts"]))
    print("  Packets Output:{}".format(intf_config["statistics"]["out-unicast-pkts"]))