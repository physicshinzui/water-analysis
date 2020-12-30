#!/Users/siida/anaconda3/bin/python
import numpy as np
import pandas as pd 
import sys
import logging

def tau_id(atom_id, t_begin,t_end):
    pass

def read_file(filename):
    with open(filename, 'r') as fin:
        ids_per_frame = []
        for line in fin:
            if line.strip()[0] == '#': continue
            ti = int(line.split(':')[0])
            ids = list(map(int, line.split(':')[-1].split(',')[0:-1]))
            ids_per_frame.append([ti, ids])
    return ids_per_frame

def index_set(ids_per_frame):
    S_ids = []
    for ti, ids in ids_per_frame:
        for idd in ids:
            S_ids.append(idd)
    S_ids = set(S_ids)
    return S_ids

def write_tau(tau):
    """
    This function writes an file where )
    input: 
        tau: dict. {frame No: [dt1, dt2, ...], 
                    frame No: [dt1, dt2, ...], 
                    ...}, 
                    where dti is the period that a selected atom stays during this.
    return: 
        None 
    """
    with open(f'tau.out', 'w') as fout:
        taus_max = {}
        for key, values in tau.items():
            try:
                taus_max[key] = max(values)
            except ValueError:
                taus_max[key] = 0

        for key, value in sorted(taus_max.items(), key = lambda x:x[1], reverse = True):
            try:
                fout.write(f'{key}, {value}\n')

            #this may not be needed? I've already pudded somewhere?
            except ValueError:
                print(f'DBG: a list is zero-element. Key = {key}')
                fout.write(f'{key}, nan \n')

def parser():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('-i' ,'--index'    , required=True, help='an index file. (.csv)')
    return p.parse_args()

def residence_time(ids_per_frame, S_ids):
    #---initialisation
    t0, prev_ids = ids_per_frame[0][0], ids_per_frame[0][1] #[]
    print(f'Init state (atom ids): \nTime {t0}, \n    * atom ids {prev_ids}')
    entered = {}
    for atom_id in S_ids: 

        if atom_id in prev_ids:
            entered[atom_id] = True
        else:
            entered[atom_id] = False

    tb, te, tau   = {}, {}, {}
    for atom_id in S_ids:
        tb[atom_id]  = 0
        te[atom_id]  = 0
        tau[atom_id] = []

    # O(N*M), where N is the number of frames, 
    # and M is the number of members in a set of atom index.
    # So, many frames and many water molecules of interest leads to large computational time. 
    for ite, (ti, ids) in enumerate(ids_per_frame[1:]):
        if ti%10 == 0: print(f'Time: {ti}')
        is_last = (ite == len(ids_per_frame[1:]) - 1)

        for atom_id in S_ids:    
            
            if (atom_id in ids) and not entered[atom_id]: # Judgement of new entering 
                tb[atom_id] = ti
                entered[atom_id] = True
                #print(f'    * atom id {atom_id} entered at time {tb[atom_id]}.')

            elif (atom_id not in ids) and (entered[atom_id]): # Judgement of going outside
                te[atom_id] = ti
                entered[atom_id] = False
                dt = te[atom_id] - tb[atom_id]
                tau[atom_id].append(dt)
                #print(f'    * atom id {atom_id} went outside at time {te[atom_id]}.')
            
            elif is_last: 
                
                if entered[atom_id]:
                    te[atom_id] = ti
                    dt = te[atom_id] - tb[atom_id] + 1
                    tau[atom_id].append(dt)

            else: #still there
                #print(f'    * atom id {atom_id} is still there.')
                pass

        prev_ids = ids #update previous ids
    return tau

def main():
    """
    Speficication:
    The aim of this program is to assign atom index to residence time.
    For example, if an atom stays at a site from 200 ps to 1000 ps, the residence time is 800 ps.
    The time can be estimated by this program, and hence you'll be able to detect sites where atoms stays for a long time in MD simulation. 

    This program converts atom id into t(id), where t(id) is a residence time of an id that an atom has.
    Usage:
        python this index.csv

    index.csv is generated by 'calc_suviveProb.py'. The file includes selected atom's ids for every frame in each row.
    """
    args = parser()
    filename = args.index
    ids_per_frame = read_file(filename)
    S_ids   = index_set(ids_per_frame) #get a set of indexes
    print(f'The No. of selected atoms = {len(S_ids)}')
    tau = residence_time(ids_per_frame, S_ids)
    write_tau(tau)

if __name__ == '__main__':
    main()