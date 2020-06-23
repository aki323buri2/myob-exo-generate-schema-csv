from pathlib import Path 
from functools import reduce 
import sys 

def fullpath(*path):
  root = Path(__file__).parent 
  full = reduce(lambda a, b: Path(a) / Path(b), path, root)
  return full.resolve().absolute()

root = str(fullpath(__file__))
if root not in sys.path: 
  sys.path.append(root)