#!/Users/siida/anaconda3/bin/python
import MDAnalysis
#from MDAnalysis.analysis.waterdynamics import SurvivalProbability as SP
from MDAnalysis.analysis.si_waterdynamics import SurvivalProbability as SP

import matplotlib.pyplot as plt
import sys
import pandas as pd

def survivalProb(univ, selection, start=0, stop=None, step=1, tau_max=30):
    #show the first frame's atoms selected to debug
    with open(f"selected_atoms_from_first_frame.txt", "w") as fout:
        for atom in univ.select_atoms(selection):   
            fout.write(f"{atom.name}{atom.id} {atom.resname}{atom.resid}\n")
 
    sp   = SP(univ, selection, verbose=True)
    sp.run(start=start, stop=stop, step=step, tau_max=tau_max)

    #for tau, sp in zip(tau_timeseries, sp_timeseries):
    #      print("{time} {sp}".format(time=tau, sp=sp))
    
    return sp.tau_timeseries, sp.sp_timeseries, sp.selected_indexes

def jotDown(taus, sps, prefix=None, nameForlog=None):
    with open(f"{prefix}_survivalProb.dat", "w") as fout:
        fout.write(f"#This output was derived from:\n")
        fout.write(f"#{nameForlog}\n")
        for tau, sp in zip(taus, sps): 
            fout.write(f"{tau} {sp}\n")
    

def parser():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('-r' ,'--ref'      , required=True, help='Reference for traj files')
    p.add_argument('-t' ,'--trj'      , nargs='+')    
    p.add_argument('-rd','--radius'   , type=float, default=6.0, help='default = 6.0 A')
    p.add_argument('-s' ,'--selection', nargs='+')
    p.add_argument('-b' ,'--begin'    , type=int, default=0, help='zero-based index. Frame no.') 
    p.add_argument('-wf' ,'--wfocus'   , default='local', help='') 

    args = p.parse_args()
    return args.ref, args.trj, args.radius, args.selection, args.begin, args.wfocus

def make_selections_for_localised_water(selections, radius):
    water_selections = []
    for i, sele in enumerate(selections):
        water_selections.append(f"name OW and sphzone {radius} ({sele})")
        print(f'{i}, {water_selections[i]}')
    return water_selections

def main():
    ref, inTrajs, radius, selections, begin, water_focus = parser()
    print('INPUT TRAJECTORIES: \n', inTrajs)
    print('SELECTIONS :')
    
    if water_focus == 'local': 
        water_selections = make_selections_for_localised_water(selections, radius)

    elif water_focus == 'entire':
        water_selections = ['name OW and around 4.5 protein ']

    else:
        exit(f'Stop: Wrong parameter was specified {water_focus}')


    ## Compute suvival probabilities for each input file.
    scale_factor = 1.0 # for frame no conversion into X 
    for i, itraj in enumerate(inTrajs):
        univ = MDAnalysis.Universe(ref, itraj, in_memory=True)

        #Survival Probability is calculated here
        taus, sps, selected_indexes = [], [], []
        for j, sele in enumerate(water_selections):
            tau_vals, suv_probs, selected_indexes = survivalProb(univ, sele, start=begin, stop=None, step=1, tau_max=30)
            taus.append(scale_factor * tau_vals)
            sps.append(suv_probs)
            prefix = chr(j+97).upper()+str(i)
            jotDown(taus=scale_factor*tau_vals, prefix=prefix, sps=suv_probs, nameForlog=itraj) 
            
            indexes_every_frames = []
            for ind in selected_indexes:
                ind = list(map(int, ind))
                indexes_every_frames.append(sorted(ind))

            with open(f'{prefix}_index.csv', 'w') as fout:
                fout.write(f"#This output was derived from:\n")
                fout.write(f"#{itraj}\n")
                for k, ids in enumerate(indexes_every_frames):
                    fout.write(f'{k}: ')
                    for l, idd in enumerate(ids):
                        fout.write(f'{idd}, ')
                    fout.write('\n')

if __name__ == "__main__":
    main()