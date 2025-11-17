import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

#print out dict as py string
json_string = json.dumps(servers_dict, indent=4)
print("JSON STRING")
print(json_string)

#convert python dictionary to JSON file
with open("servers.json", "w") as json_file:
    json.dump(servers_dict, json_file, indent=4)

print("\n server has been saved to servers.json")


# test by reading the file back
with open("servers.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
    print(type(loaded_data))

