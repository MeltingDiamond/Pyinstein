import json, os, platform
from pathlib import Path

script_dir = Path(__file__).parent.absolute()
nodes = []
data = {}
bibite_name = ""
bibite_version = ""
# All versions can be loaded, but these are the ones I know work.
# Currently not used for anything other than showing the user which are supported
old_supported_version = ["0.5.1","0.6.0.1"] # Old list of supported versions
supported_versions = ["0.6.3.1"] # As of September 29 2026 this is the list of supported versions. Anything from the old list is no longer known if it works

def save_to_version(version):
    global bibite_version
    bibite_version = version

def get_bibite_data():
    global data, bibite_name

    os_map = {
    "Windows": "Windows",
    "Darwin": "Mac",
    "Linux": "Linux"
    }
    OS_TYPE = os_map.get(platform.system(), "Unknown")

    bibites = []
    if OS_TYPE == "Windows":
        for bibite in os.listdir(f'{os.environ['USERPROFILE']}/AppData/LocalLow/The Bibites/The Bibites/bibites'):
            if bibite.endswith(".bb8"):
               bibites.append(f'{os.environ['USERPROFILE']}/AppData/LocalLow/The Bibites/The Bibites/bibites/{bibite}')
    elif OS_TYPE == "Linux":
        for bibite in os.listdir(f'{os.environ['HOME']}/.config/unity3d/The Bibites/The Bibites/Bibites'):
            if bibite.endswith(".bb8"):
               bibites.append(f'{os.environ['HOME']}/.config/unity3d/The Bibites/The Bibites/Bibites/{bibite}')

    bb8_number = None
    while bb8_number is None:
        try:
            for idx, bibite in enumerate(bibites):
                print(f"{idx}       {os.path.basename(bibite)}")
            user_input = input("\nType number for the bibite you want to save to\n\n")
            bb8_number = int(user_input)
            # Check if the number is in the valid range of bibites
            if bb8_number < 0 or bb8_number >= len(bibites):
                print(f"Please enter a number between 0 and {len(bibites) - 1}")
                bb8_number = None  # Reset if out of range
        except ValueError:
            print("Please enter a valid integer.\n")
    
    bibite_name = bibites[bb8_number]
    with open(bibite_name, 'r') as file:
        ddict = json.load(file)
        ddict["genes"]["genes"] = []
        ddict["brain"]["Nodes"] = []
        ddict["brain"]["Synapses"] = []
    data = dict(ddict)

def write():
    global data, bibite_name
    with open(bibite_name, 'w') as file:
        json.dump(data, file, indent=4)

class Node:
    def __init__(self, Type, baseActivation, TypeName, Index, Inov, Desc, Value, archetype):
        self.Type = Type
        self.baseActivation = baseActivation
        self.TypeName = TypeName
        self.Index = Index
        self.Inov = Inov
        self.Desc = Desc
        self.Value = Value
        self.LastInput = 0.0
        self.LastOutput = 0.0
        self.archetype = archetype
        
        global nodes
        nodes.append(self)
   
    def write(self): # I don't know how to use this
        # json as above with all the hidden junk
        return {
                "Type": self.Type,
                "baseActivation": self.baseActivation,
                "TypeName": self.TypeName,
                "Index": self.Index,
                "Inov": self.Inov,
                "Desc": self.Desc,
                "Value": self.Value,
                "LastInput": 0.0,
                "LastOutput": 0.0,
                "archetype": self.archetype
            }

def new_conn(Inov, IN, OUT, WEIGHT, En):
    global data
    if type(IN) == str:
        for Node in data["brain"]["Nodes"]:
            if Node["Desc"] == IN:
                #if Node["TypeName"] in ['ReLu',"Input"]:
                IN = int(Node["Index"])
                #else:
                #    raise Exception(f'\'{IN}\' is not a type of input.')
        if type(IN) == str:
            raise Exception(f'\'{IN}\' is not in Nodes.')
    if type(OUT) == str:
        for Node in data["brain"]["Nodes"]:
            if Node["Desc"] == OUT:
                if Node["TypeName"] != "Input":
                    OUT = int(Node["Index"])
    data["brain"]["Synapses"].append({
        "Inov": Inov,
        "NodeIn": IN,
        "NodeOut": OUT,
        "Weight": WEIGHT,
        "En": En
      })

def save_genes(genes):
    data["genes"]["genes"] = genes
    
def save_nodes():
    converted_nodes = [node.write() for node in nodes]
    data["brain"]["Nodes"] = converted_nodes