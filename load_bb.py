import json, os
from pathlib import Path

script_dir = Path(__file__).parent.absolute()

data = {}

save_functions_str = """from save_bb import new_conn, get_bibite_data, save_genes, write # Do not remove this line

# new_conn is structured like this
\'\'\'
new_conn(Inov, NodeIn, NodeOut, WEIGHT, En):
    {"Inov": Inov,
    "NodeIn": NodeIn,
    "NodeOut": NodeOut,
    "Weight": WEIGHT,
    "En": En}
\'\'\'"""

def printlogo():
    Logo = [   
 "         _  __          ____                   _               _    _                            ",
 "        | |/ /  ___    |  _ \  _ __  ___    __| | _   _   ___ | |_ (_)  ___   _ __   ___         ",
 " _____  | ' /  / _ \   | |_) || '__// _ \  / _` || | | | / __|| _ || | / _ \ | '_ \ / __|  _____ ",
 "|_____| | . \ | (_) |  |  __/ | |  | (_) || (_| || |_| || (__ | |_ | || (_) || | | |\__ \ |_____|",
 "        |_|\_(_)___(_) |_|    |_|   \___/  \____| \____| \___| \__||_| \___/ |_| |_||___/        ",
 "                                                                                                 ",
 "                                                                                                 ",
 "          --------------- made by Kellerossel, updated by MeltingDiamond ---------------                      \n"
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

def get_bibite_genes():
    global data
    genes = data["genes"]["genes"]

    return genes

def convert_bibite_brain(): # Converts the brain into a format that you can edit
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

def generate_edit_brain_py():
    version = get_version()

    node_names = get_bibite_node_names()
    node_names_string = ', '.join(f"\n'{name}'" for name in node_names)

    genes = get_bibite_genes()
    genes_string = ',\n    '.join(f'"{key}": {value}' for key, value in genes.items())

    converted_brain_string = ("# Import functions used when saving\n"
                              f"{save_functions_str}\n\n"
                              f"Names_of_nodes = [{node_names_string}]\n\n"
                              f"version = '{version}' # The version of the bibite the brain is extracted from\n\n"
                              "# Each line below is used when saving the brain.\n# Line starting with new_conn is a synapse connection and can safely be added/removed\n"
                              "get_bibite_data() # Do not remove this line\n\n"
                              f"# Here you edit genes\ngenes = {{\n    {genes_string}\n}}\n\n"
                              "# Here you edit the brain\n")
    
    for Synapse in converted_brain["Synapses"]:
        converted_brain_string = f'{converted_brain_string}{Synapse}\n'

    converted_brain_string = converted_brain_string + '\nsave_genes(genes) # Used to save genes\n\nwrite() # Writes the brain into the bibite file\nprint("Bibite saved, you can now load the bibite into the game")'

    return converted_brain_string

bibites = []
for bibite in os.listdir(f'C:/Users/{os.getlogin()}/AppData/LocalLow/The Bibites/The Bibites/bibites'):
    if bibite.endswith(".bb8"):
        bibites.append(f'C:/Users/{os.getlogin()}/AppData/LocalLow/The Bibites/The Bibites/bibites/{bibite}')

bb8_number = None
error = False # used to display error at the bottom of the bibites list
while bb8_number is None:
    try:
        print("Number:  Bibite:")
        for idx, bibite in enumerate(bibites):
            print(f"{idx}        {os.path.basename(bibite)}")
        if error:
            print("\nPlease enter a valid integer.")
        user_input = input(f"\nType a number between 0 and {len(bibites) - 1} for the bibite you want to edit:\n\n")
        bb8_number = int(user_input)
        # Check if the number is in the valid range of bibites
        if bb8_number < 0 or bb8_number >= len(bibites):
            print(f"Please enter a number between 0 and {len(bibites) - 1}")
            bb8_number = None  # Reset if out of range
        error = False
    except ValueError:
        error = True

bibite_to_load = bibites[bb8_number]

data = read(bibite_to_load)
write(data, True)
print("Original unmodified bibite saved to Pyinstein.bb8")

converted_brain = convert_bibite_brain()
if not os.path.isfile(f'{script_dir}/edit_brain.py'):
   open(f'{script_dir}/edit_brain.py', 'a').close()

converted_brain_string = generate_edit_brain_py()

write(converted_brain_string, False, f'{script_dir}/edit_brain.py')

bibite_name = (os.path.basename(bibite_to_load)).replace(".bb8", "")
print(f"\n{bibite_name} loaded\nYou can now edit the bibite by editing \"edit_brain.py\"")