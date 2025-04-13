# Import functions used when saving
from save_bb import new_conn, get_bibite_data, save_genes, write # Do not remove this line

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
'Want2Attack', 
'Hidden0', 
'Hidden1', 
'Hidden2']

version = '0.6.0.1' # The version of the bibite the brain is extracted from

# Each line below is used when saving the brain.
# Line starting with new_conn is a synapse connection and can safely be added/removed
get_bibite_data() # Do not remove this line

# Here you edit genes
genes = {
    "LayTime": 26.9825573,
    "BroodTime": 26.17411,
    "HatchTime": 13.6014757,
    "SizeRatio": 1.051581,
    "SpeedRatio": 0.974236667,
    "ColorR": 0.7132759,
    "ColorG": 0.7179152,
    "ColorB": 0.171787515,
    "MutationAmountSigma": 0.004333486,
    "AverageMutationNumber": 1.74831951,
    "BrainMutationSigma": 0.143025443,
    "BrainAverageMutation": 0.0760994256,
    "ViewAngle": 227.7185,
    "ViewRadius": 200.0,
    "ClockSpeed": 0.388975918,
    "PheroSense": 153.804382,
    "Diet": 0.5,
    "HerdSeparationWeight": 0.110408947,
    "HerdAlignmentWeight": 2.616617,
    "HerdCohesionWeight": 0.5664832,
    "HerdVelocityWeight": 0.0199187789,
    "HerdSeparationDistance": 75.06252,
    "GrowthScale": 0.3378411,
    "GrowthMaturityFactor": 2.91788387,
    "GrowthMaturityExponent": 0.326139331,
    "EyeOffset": 0.308237761,
    "StomachWAG": 3.01193285,
    "WombWAG": 2.50836968,
    "FatWAG": 2.8164134,
    "ArmorWAG": 1.22840238,
    "ThroatWAG": 2.394422,
    "MouthMusclesWAG": 1.44758451,
    "MoveMusclesWAG": 1.56330657,
    "FatStorageThreshold": 0.6923864,
    "FatStorageDeadband": 0.172810227
}

# Here you edit the brain
new_conn(4, 'MeatAngle', 'Rotate', 0.8730221, True)
new_conn(29, 'PlantAngle', 'Rotate', -0.2, True)
new_conn(5, 'NMeats', 'PhereOut3', -0.12781474, True)
new_conn(6, 'AttackedDamage', 'Grab', -0.1470481, True)
new_conn(7, 'Maturity', 'Want2Attack', 1.00656378, True)
new_conn(8, 'AttackedDamage', 'Accelerate', 0.209885091, False)
new_conn(9, 'Fullness', 'Accelerate', -1.01169658, True)
new_conn(10, 'Phero3Angle', 'Accelerate', -0.5216525, True)
new_conn(11, 'MeatCloseness', 'Want2Grow', 1.25412524, True)
new_conn(12, 'RedBibite', 'EggProduction', 0.374998361, True)
new_conn(13, 'NBibites', 'PhereOut2', -0.522816539, True)
new_conn(14, 'PlantCloseness', 'Want2Grow', -0.164204746, True)
new_conn(15, 'Speed', 'EggProduction', -0.23829475, True)
new_conn(16, 'PheroSense3', 'Want2Eat', -0.184197873, False)
new_conn(17, 'LifeRatio', 'Want2Grow', 0.163160533, True)
new_conn(18, 'MeatCloseness', 'Hidden0', 0.210803315, True)
new_conn(19, 'Hidden0', 'EggProduction', 0.946124, True)
new_conn(20, 'EggStored', 'Hidden0', -0.6268739, True)
new_conn(21, 'EnergyRatio', 'Want2Attack', 1.63698912, True)
new_conn(22, 'AttackedDamage', 'Hidden1', 0.28378737, True)
new_conn(23, 'Hidden1', 'Accelerate', 1.0, True)
new_conn(24, 'Hidden1', 'Want2Attack', 0.514022946, True)
new_conn(25, 'MeatCloseness', 'Grab', 0.2181158, True)
new_conn(26, 'PheroSense3', 'Hidden2', -0.184197873, True)
new_conn(27, 'Hidden2', 'Want2Eat', 1.0, True)
new_conn(28, 'Phero2Heading', 'Want2Heal', -0.0524244, True)

save_genes(genes) # Used to save genes

write() # Writes the brain into the bibite file
print("Bibite saved, you can now load the bibite into the game")
