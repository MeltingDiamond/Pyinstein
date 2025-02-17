import json, os
from pathlib import Path

script_dir = Path(__file__).parent.absolute()

data = {}

save_functions_str = """from save_bb import new_conn, get_bibite_data, write
from pathlib import Path

script_dir = Path(__file__).parent.absolute()

# new_conn is structured like this
\'\'\'
new_conn(Inov, NodeIn, NodeOut, WEIGHT, En):
    {"Inov": Inov,
    "NodeIn": NodeIn,
    "NodeOut": NodeOut,
    "Weight": WEIGHT,
    "En": En}
\'\'\'

"""

def printlogo():
    Logo = [   
 "         _  __          ____                   _               _    _                            ",
 "        | |/ /  ___    |  _ \  _ __  ___    __| | _   _   ___ | |_ (_)  ___   _ __   ___         ",
 " _____  | ' /  / _ \   | |_) || '__// _ \  / _` || | | | / __|| _ || | / _ \ | '_ \ / __|  _____ ",
 "|_____| | . \ | (_) |  |  __/ | |  | (_) || (_| || |_| || (__ | |_ | || (_) || | | |\__ \ |_____|",
 "        |_|\_(_)___(_) |_|    |_|   \___/  \____| \____| \___| \__||_| \___/ |_| |_||___/        ",
 "                                                                                                 ",
 "                                                                                                 ",
 "                      --------------- made by Kellerossel, updated by MeltingDiamond ---------------                      \n"
        ]
    for line in Logo:
        print(line)
printlogo()

def read(bibname='basic0.5.1.bb8'):
    with open(bibname, 'r') as file:
        ddict = json.load(file)
    return dict(ddict)

def write(data_to_write, json_write, name = f'{script_dir}/Pyinstein.bb8'):
    if json_write == True:
        with open(name, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        with open(name, 'w') as file:
            file.write(data_to_write)

def get_version():
    global data
    return data["version"]

def get_bibite_node_names():
    global data
    Node_names = []
    for Node in data["brain"]["Nodes"]:
        desc = Node["Desc"]
        Node_names.append(f"{desc}")

    return Node_names

def convert_bibite_brain():
    global data

    node_lookup = {node["Index"]: node["Desc"] for node in data["brain"]["Nodes"]}

    converted_brain = data["brain"]
    for idx, Synapse in enumerate(data["brain"]["Synapses"]):
        
        NodeIn = node_lookup.get(Synapse["NodeIn"], Synapse["NodeIn"])
        NodeOut = node_lookup.get(Synapse["NodeOut"], Synapse["NodeOut"])
        Weight = Synapse["Weight"]
        En = Synapse["En"]
        Inov = Synapse['Inov']
        Synapse = f"new_conn({Inov}, \'{NodeIn}\', \'{NodeOut}\', {Weight}, {En})"
        converted_brain["Synapses"][idx] = Synapse
    
    return converted_brain

bibites = []
for bibite in os.listdir(f'C:/Users/{os.getlogin()}/AppData/LocalLow/The Bibites/The Bibites/bibites'):
    if bibite.endswith(".bb8"):
        bibites.append(f'C:/Users/{os.getlogin()}/AppData/LocalLow/The Bibites/The Bibites/bibites/{bibite}')

print("Number: Bibite:")
bb8_number = None
while bb8_number is None:
    try:
        for idx, bibite in enumerate(bibites):
            print(f"{idx}       {os.path.basename(bibite)}")
        user_input = input("\nType number for the bibite you want to edit\n\n")
        bb8_number = int(user_input)
        # Check if the number is in the valid range of bibites
        if bb8_number < 0 or bb8_number >= len(bibites):
            print(f"Please enter a number between 0 and {len(bibites) - 1}")
            bb8_number = None  # Reset if out of range
    except ValueError:
        print("Please enter a valid integer.\n")

bibite_to_load = bibites[bb8_number]

data = read(bibite_to_load)
write(data, True)
print("Original unmodified bibite saved to Pyinstein.bb8")

converted_brain = convert_bibite_brain()
if not os.path.isfile(f'{script_dir}/edit_brain.py'):
   open(f'{script_dir}/edit_brain.py', 'a').close()

version = get_version()
node_names = get_bibite_node_names()
node_names_string = ', '.join(f"\n'{name}'" for name in node_names)
converted_brain_string = "# Import functions used when saving\n" + f"{save_functions_str}Names_of_nodes = [{node_names_string}]\n\nversion = '{version}' # The version of the bibite the brain is extracted from\n# Each line below starting with new_conn is a synapse connection. Only stuff written here is in the brain\nget_bibite_data()\n"
for Synapse in converted_brain["Synapses"]:
    converted_brain_string = f'{converted_brain_string}{Synapse}\n'
converted_brain_string = converted_brain_string + '\nwrite() # Write the brain into the bibite file\nprint("I haven\'t had that much sex")'

write(converted_brain_string, False, f'{script_dir}/edit_brain.py')

bibite_name = (os.path.basename(bibite_to_load)).replace(".bb8", "")
print(f"\n{bibite_name} loaded\nYou can now edit the bibite by editing \"edit_brain.py\"")
