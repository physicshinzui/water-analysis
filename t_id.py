import numpy as np
import pandas as pd 
import sys
import logging

def tau_id(atom_id, t_begin,t_end):
    
    pass

def read_file(filename):
    with open(filename, 'r') as fin:
        id_list = []
        for line in fin:
            if line.strip()[0] == '#': continue
            ti = int(line.split(':')[0])
            ids = list(map(int, line.split(':')[-1].split(',')[0:-1]))
            id_list.append([ti, ids])
    return id_list

def index_set(id_list):
    S_ids = []
    for ti, ids in id_list:
        for idd in ids:
            S_ids.append(idd)
    S_ids = set(S_ids)
    return S_ids

def write_tau(tau):
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

            except ValueError:
                print(f'DBG: a list is zero-element. Key = {key}')
                fout.write(f'{key}, nan \n')



def main():
    filename = sys.argv[1]
    id_list = read_file(filename)
    S_ids   = index_set(id_list) #get a set of indexes
    print(f'The No. of selected atoms = {len(S_ids)}')

    #---initialisation
    t0, prev_ids = id_list[0][0], id_list[0][1] #[]
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

    for ite, (ti, ids) in enumerate(id_list[1:]):
        if ti%10 == 0: print(f'Time: {ti}')
        is_last = ite == len(id_list[1:])-1

        for atom_id in S_ids:    
            
            if (atom_id in ids) and not entered[atom_id]: # Judgement if entering
                tb[atom_id] = ti
                entered[atom_id] = True
                #print(f'    * atom id {atom_id} entered at time {tb[atom_id]}.')

            elif (atom_id not in ids) and (entered[atom_id]): # Judgement if going outside
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

    write_tau(tau)

if __name__ == '__main__':
    main()