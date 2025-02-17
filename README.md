My version of Pyinstein a code-based Bibite creator and Editor.<br>
Write python code to modify a bibites brain.

This tool is free to use and you are allowed to modify any file to your liking.

### How to use the tool?
Before you start make sure you have a standard installation of python 3.x and make sure the libraries json, os and pathlib are installed

1. Download load_bb.py and save_bb.py and place them in the same folder
2. Run load_bb.py in a terminal and follow printed instructions
3. Open the generated edit_brain.py in any text/code editor you wish to use. There you will already see some new_conn() lines, this is the brain you loaded. 
4. Now you edit the brain by adding/removing new_conn(Inov, NodeIn, NodeOut, WEIGHT, En) functions one line per function. (new_conn will be turned into a synapse connecting NodeIn to NodeOut with a weight of WEIGHT. This is described in the edit_brain.py file)
5. When you are finished run the edit_brain.py file you just edited in a terminal and follow what is printed

You have now edited a bibite brain by writing/modifying a couple of python lines

Known missing features:
* Outputs with biases can't bee seen/edited for 0.6.0.1 and newer
* No gene viewing/editing support
