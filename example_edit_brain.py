# Import functions used when saving
from save_bb import new_conn, get_bibite_data, write
from pathlib import Path

script_dir = Path(__file__).parent.absolute()

# new_conn is structured like this
'''
new_conn(Inov, NodeIn, NodeOut, WEIGHT, En):
    {"Inov": Inov,
    "NodeIn": NodeIn,
    "NodeOut": NodeOut,
    "Weight": WEIGHT,
    "En": En}
'''

Names_of_nodes = [
'EnergyRatio', 
'Maturity', 
'LifeRatio', 
'Fullness', 
'Speed', 
'IsGrabbing', 
'AttackedDamage', 
'EggStored', 
'BibiteCloseness', 
'BibiteAngle', 
'NBibites', 
'PlantCloseness', 
'PlantAngle', 
'NPlants', 
'MeatCloseness', 
'MeatAngle', 
'NMeats', 
'RedBibite', 
'GreenBibite', 
'BlueBibite', 
'Tic', 
'Minute', 
'TimeAlive', 
'PheroSense1', 
'PheroSense2', 
'PheroSense3', 
'Phero1Angle', 
'Phero2Angle', 
'Phero3Angle', 
'Phero1Heading', 
'Phero2Heading', 
'Phero3Heading', 
'Accelerate', 
'Rotate', 
'Herding', 
'EggProduction', 
'Want2Lay', 
'Want2Eat', 
'Digestion', 
'Grab', 
'ClkReset', 
'PhereOut1', 
'PhereOut2', 
'PhereOut3', 
'Want2Grow', 
'Want2Heal', 
'Want2Attack']

version = '0.6.0.1' # The version of the bibite the brain is extracted from
# Each line below starting with new_conn is a synapse connection. Only stuff written here is in the brain
get_bibite_data()
new_conn(1, 'Fullness', 'Digestion', 4.07295752, True)
new_conn(2, 'PlantAngle', 'Rotate', 1.15925133, True)
new_conn(3, 'PlantCloseness', 'Accelerate', -0.401356, True)

write() # Write the brain into the bibite file
print("I haven't had that much sex")
