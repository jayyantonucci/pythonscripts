import sys
from slippi import Game #https://py-slippi.readthedocs.io/en/latest/index.html#api-docs
Game('2021-01\Game_20210101T123020.slp') #example
original_stdout = sys.stdout
with open('output.txt', 'w') as f:
    sys.stdout = f # changes output to the txt file
    print(Game('2021-01\Game_20210101T123020.slp')) # prints to txt file
    sys.stdout = original_stdout # Reset the standard output to its original value
    
    
path = 'output.txt'
path_file = open(path, 'r')
path_file.read()
    
    
    
    
#from slippi.parse import parse
#from slippi.parse import ParseEvent
#handlers = {ParseEvent.METADATA: print}
#parse('2021-01\Game_20210101T123020.slp', handlers)
