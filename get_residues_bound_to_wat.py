import numpy as np
import pandas as pd 
import sys
from MDAnalysis import Universe 

class LookForResidues():
    
    def __init__(self, u, water_ids,  cutoff = 5.0):
        self.u = u
        self.water_ids = water_ids
        self.cutoff = cutoff
        self.selected_waters = []

    def make_selections(self):
        self.selections = []
        for water_id in self.water_ids: #water_id is one-based index 
            water_id_zero_based = int(water_id) - 1
            #self.selections.append(f'protein and shpzone {cutoff} (name OW and {water_id})') 
            water = self.u.atoms[water_id_zero_based]
            self.selected_waters.append([f'{water.name}{water.resid}'])            
            #umm, how can i select an oxygen by atom id via mdanalysis?? 31.12.2020

    def run(self):
        dict_residues = {}
        for frame in u.trajectory():
            pass
    
        #return dict_residues

def main():
    filename_of_water_ids = sys.argv[1]
    filename_of_traj      = sys.argv[2]
    water_ids = pd.read_csv(filename_of_water_ids)
    u = Universe(filename_of_traj)
    lr = LookForResidues(u, water_ids)
    lr.make_selections()
    print(lr.selected_waters)
    

if __name__ == '__main__':
    main()