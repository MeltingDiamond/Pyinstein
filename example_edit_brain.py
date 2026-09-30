# Import functions used when saving
from save_bb import Node, new_conn, save_to_version, get_bibite_data, save_genes, save_nodes, write # Do not remove this line

# new_conn is structured like this
'''
new_conn(Inov, NodeIn, NodeOut, WEIGHT, En):
    {"Inov": Inov,
    "NodeIn": NodeIn,
    "NodeOut": NodeOut,
    "Weight": WEIGHT,
    "En": En}
'''

version = '0.6.3.1' # The version of the bibites the brain is extracted from
save_to_version('0.6.3.1') # The version you want to save to

# Each line below is used when saving the brain.
# Line starting with new_conn is a synapse connection and can safely be added/removed
get_bibite_data() # Do not remove this line

# Here you edit genes
genes = {
    "LayTime": 15.5148859,
    "BroodTime": 35.0,
    "HatchTime": 19.0,
    "SizeRatio": 1.27901471,
    "SpeedRatio": 1.26616788,
    "ColorR": 0.753119051,
    "ColorG": 0.104958311,
    "ColorB": 0.256386817,
    "MutationAmountSigma": 0.121800646,
    "AverageMutationNumber": 1.0,
    "BrainMutationSigma": 0.15,
    "BrainAverageMutation": 0.9880969,
    "ViewAngle": 256.934265,
    "ViewRadius": 50.87593,
    "ClockSpeed": 1.0,
    "PheroSense": 150.0,
    "Diet": 0.9102195,
    "HerdSeparationWeight": 0.0557917356,
    "HerdAlignmentWeight": 0.0895292461,
    "HerdCohesionWeight": 1.75,
    "HerdVelocityWeight": 0.15,
    "HerdSeparationDistance": 35.0,
    "GrowthScale": 0.75543,
    "GrowthMaturityFactor": 3.43867,
    "GrowthMaturityExponent": 2.0,
    "EyeOffset": 0.5,
    "StomachWAG": 5.0,
    "WombWAG": 2.5,
    "FatWAG": 2.5,
    "ArmorWAG": 0.249004,
    "ThroatWAG": 1.2201196,
    "MouthMusclesWAG": 0.122011952,
    "MoveMusclesWAG": 0.6100598,
    "FatStorageThreshold": 0.5,
    "FatStorageDeadband": 0.25
}

# Here you edit the brain
EnergyRatio0 = Node(0, 0.0, "Input", 0, 1, "EnergyRatio", 0.9865625, 0)
Maturity1 = Node(0, 0.0, "Input", 1, 2, "Maturity", 1.43854868, 0)
LifeRatio2 = Node(0, 0.0, "Input", 2, 3, "LifeRatio", 1.0, 0)
Fullness3 = Node(0, 0.0, "Input", 3, 4, "Fullness", 0.0, 0)
Speed4 = Node(0, 0.0, "Input", 4, 5, "Speed", 0.3477938, 0)
RotationSpeed5 = Node(0, 0.0, "Input", 5, 6, "RotationSpeed", 0.007905218, 0)
IsGrabbing6 = Node(0, 0.0, "Input", 6, 7, "IsGrabbing", 0.0, 0)
AttackedDamage7 = Node(0, 0.0, "Input", 7, 8, "AttackedDamage", 0.0, 0)
EggStored8 = Node(0, 0.0, "Input", 8, 9, "EggStored", 0.0, 0)
BibiteCloseness9 = Node(0, 0.0, "Input", 9, 10, "BibiteCloseness", 0.0, 0)
BibiteAngle10 = Node(0, 0.0, "Input", 10, 11, "BibiteAngle", 0.0, 0)
NBibites11 = Node(0, 0.0, "Input", 11, 12, "NBibites", 0.0, 0)
PlantCloseness12 = Node(0, 0.0, "Input", 12, 13, "PlantCloseness", 0.0, 0)
PlantAngle13 = Node(0, 0.0, "Input", 13, 14, "PlantAngle", 0.0, 0)
NPlants14 = Node(0, 0.0, "Input", 14, 15, "NPlants", 0.0, 0)
MeatCloseness15 = Node(0, 0.0, "Input", 15, 16, "MeatCloseness", 0.0, 0)
MeatAngle16 = Node(0, 0.0, "Input", 16, 17, "MeatAngle", 0.0, 0)
NMeats17 = Node(0, 0.0, "Input", 17, 18, "NMeats", 0.0, 0)
RedBibite18 = Node(0, 0.0, "Input", 18, 19, "RedBibite", 0.0, 0)
GreenBibite19 = Node(0, 0.0, "Input", 19, 20, "GreenBibite", 0.0, 0)
BlueBibite20 = Node(0, 0.0, "Input", 20, 21, "BlueBibite", 0.0, 0)
Tic21 = Node(0, 0.0, "Input", 21, 22, "Tic", 0.0, 0)
Minute22 = Node(0, 0.0, "Input", 22, 23, "Minute", 0.00416666735, 0)
TimeAlive23 = Node(0, 0.0, "Input", 23, 24, "TimeAlive", 0.00416666735, 0)
PheroSense124 = Node(0, 0.0, "Input", 24, 25, "PheroSense1", 0.0, 0)
PheroSense225 = Node(0, 0.0, "Input", 25, 26, "PheroSense2", 0.0, 0)
PheroSense326 = Node(0, 0.0, "Input", 26, 27, "PheroSense3", 0.0, 0)
Phero1Angle27 = Node(0, 0.0, "Input", 27, 28, "Phero1Angle", 0.0, 0)
Phero2Angle28 = Node(0, 0.0, "Input", 28, 29, "Phero2Angle", 0.0, 0)
Phero3Angle29 = Node(0, 0.0, "Input", 29, 30, "Phero3Angle", 0.0, 0)
Phero1Heading30 = Node(0, 0.0, "Input", 30, 31, "Phero1Heading", 0.0, 0)
Phero2Heading31 = Node(0, 0.0, "Input", 31, 32, "Phero2Heading", 0.0, 0)
Phero3Heading32 = Node(0, 0.0, "Input", 32, 33, "Phero3Heading", 0.0, 0)
Accelerate33 = Node(3, 0.03611282, "TanH", 33, 34, "Accelerate", 0.5459295, 1)
Rotate34 = Node(3, 0.07611282, "TanH", 34, 35, "Rotate", 0.07596619, 1)
Herding35 = Node(3, 0.0, "TanH", 35, 36, "Herding", 0.0, 1)
EggProduction36 = Node(3, 0.2, "TanH", 36, 37, "EggProduction", 0.197375327, 1)
Want2Lay37 = Node(1, 0.0, "Sigmoid", 37, 38, "Want2Lay", 0.5, 1)
Want2Eat38 = Node(3, -1.11538947, "TanH", 38, 39, "Want2Eat", -0.8059592, 1)
Digestion39 = Node(1, 0.0, "Sigmoid", 39, 40, "Digestion", 0.275819123, 1)
Grab40 = Node(3, 0.0, "TanH", 40, 41, "Grab", 0.0, 1)
ClkReset41 = Node(1, 0.0, "Sigmoid", 41, 42, "ClkReset", 0.5, 1)
PhereOut142 = Node(5, 0.0, "ReLu", 42, 43, "PhereOut1", 0.0, 1)
PhereOut243 = Node(5, 0.0, "ReLu", 43, 44, "PhereOut2", 0.0, 1)
PhereOut344 = Node(5, 0.0, "ReLu", 44, 45, "PhereOut3", 0.0, 1)
Want2Grow45 = Node(1, -1.98611271, "Sigmoid", 45, 46, "Want2Grow", 0.6960583, 1)
Want2Heal46 = Node(1, 0.0, "Sigmoid", 46, 47, "Want2Heal", 0.5, 1)
Want2Attack47 = Node(1, 0.0, "Sigmoid", 47, 48, "Want2Attack", 0.5, 1)
Hidden048 = Node(5, 0.0, "ReLu", 48, 49, "Hidden0", 0.399999976, 2)
Hidden149 = Node(6, 0.0, "Gaussian", 49, 50, "Hidden1", 1.0, 2)
Hidden350 = Node(6, 0.0, "Gaussian", 50, 52, "Hidden3", 1.0, 2)

new_conn(76, PlantAngle13.Index, Accelerate33.Index, 0.03611282, False)
new_conn(77, BibiteCloseness9.Index, Rotate34.Index, 0.07611282, False)
new_conn(78, PlantAngle13.Index, Rotate34.Index, 0.07611282, True)
new_conn(79, BibiteCloseness9.Index, Hidden048.Index, -1.21368527, True)
new_conn(80, BibiteCloseness9.Index, Want2Attack47.Index, 2.746853, True)
new_conn(81, Hidden149.Index, Hidden048.Index, 1.34611285, True)
new_conn(82, Hidden350.Index, Hidden048.Index, -0.9461129, True)
new_conn(83, Hidden048.Index, Accelerate33.Index, 1.44112825, True)
new_conn(84, MeatCloseness15.Index, Hidden048.Index, -1.1461128, True)
new_conn(85, BibiteAngle10.Index, Hidden149.Index, -2.84611273, True)
new_conn(86, NBibites11.Index, Hidden350.Index, -6.456113, True)
new_conn(87, EnergyRatio0.Index, Want2Grow45.Index, 2.84611273, True)
new_conn(88, PlantCloseness12.Index, Want2Grow45.Index, -1.98611271, False)
new_conn(89, BibiteAngle10.Index, Rotate34.Index, 1.25685859, True)
new_conn(90, MeatAngle16.Index, Rotate34.Index, 0.7568586, True)
new_conn(91, AttackedDamage7.Index, Accelerate33.Index, 2.57611275, True)
new_conn(92, PlantCloseness12.Index, Want2Eat38.Index, -2.34338951, True)
new_conn(93, MeatCloseness15.Index, Want2Eat38.Index, 3.94611287, True)
new_conn(94, Maturity1.Index, Digestion39.Index, -0.1809116, True)
new_conn(95, EnergyRatio0.Index, Digestion39.Index, -0.7129116, True)
new_conn(96, PlantAngle13.Index, Want2Eat38.Index, -2.34338951, False)
new_conn(97, PheroSense225.Index, Want2Attack47.Index, 0.800588548, True)

save_genes(genes) # Used to save genes
save_nodes() # Used to save Nodes

write() # Writes the brain into the bibite file
print("Bibite saved, you can now load the bibite into the game")
