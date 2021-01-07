
def read_wat_ids(filename, tau_lower_bound=50.0):
    with open(filename, 'r') as fin:
        py_sele = []
        for i, line in enumerate(fin):
            index, tau = str(line.split(',')[0]), float(line.split(',')[1])
            if tau >= tau_lower_bound: 
                py_sele.append(index)

    if len(py_sele) == 0:
        wat_ids = None
        return wat_ids
    
    else:
        #wat_ids = 'sele id ' + '+'.join(py_sele)
        wat_ids = '+'.join(py_sele)
        return wat_ids

def get_atom_index_filtered_by_sasa(sasa_dict, relsasa_cutoff = 0.1, outfile=None): #outfile has not been implemented yet. 
    atom_index_w_large_sasa = []
    for key, value in sasa_dict.items():
        chain = key[2]
        resi  = key[-1]

        if value <= relsasa_cutoff:
            atom_index_w_large_sasa.append([chain, resi])

    return atom_index_w_large_sasa

def make_selections_from(atom_index, target_object):
    selections = []
    for i, (chain, resi) in enumerate(atom_index):
        sele = f'(chain {chain} and resi {resi} and name OW)'
        if chain == '':
            #For state 1, "chain" variable is blank, because when flattering {tmp_obj_name}, 
            #blank seemed to be assigned to the chain id in the state 1
            print(f'Empty chain IDs are ignored. The blank IDs are likely to be assigned to the first state.') 
            continue     
        selections.append(sele)
    
    if len(selections) > 2:
        selection_strings = f'{target_object} and (' + selections[0] + ' or ' + ' or '.join(selections[1:]) + ')'
    
    elif len(selections) == 1:
        selection_strings = f'{target_object} and ' + selections
    
    else:
        selection_strings = None
        
    return selection_strings

def show_interest(selections_of_interest):
    for sele in selections_of_interest:
        cmd.show('spheres', sele)
        cmd.util.cbag(sele)
    return 


def main():
    import sys
    #inputs
    filename_wat_ids = sys.argv[1]
    ref  = sys.argv[2]
    traj = sys.argv[3]
    wat_ids = read_wat_ids(filename_wat_ids)
    print('wat_ids selection : ', wat_ids)
     
    #load a reference and the corresponding trajectory
    cmd.load(ref)
    cmd.load_traj(traj)
    cmd.util.cbc('polymer')    
    
    #Create wat_obj
    wat_obj_name = 'wat_obj' 

    # 
    if wat_ids == None:
        print('wat id is none')
        cmd.select(wat_obj_name, None)

    else: 
        print('wat_ids:', wat_ids)
        cmd.select(wat_obj_name, f'id {wat_ids}')
    #---

    # Remove short-stay water molecules 
    cmd.remove(f'not {wat_obj_name} and not polymer')

    # Extract flattened wat_obj
    tmp_obj_name = 'tmp_obj'
    cmd.create(tmp_obj_name, f'{wat_obj_name}')
    
    # Merge all the frames of the tmp_obj into a single object. 
    flatten_wat_obj = 'flatten_wat_obj'
    cmd.do(f'flatten {flatten_wat_obj}, {tmp_obj_name}')
    #cmd.delete(tmp_obj_name) #delete the temporary object
    cmd.hide('nonbonded', 'all')

    # calculate SASA for each atoms of flatten_wat_obj
    sasa_dict = cmd.get_sasa_relative(flatten_wat_obj)
#    pd.DataFrame.from_dict(sasa_dict).to_csv('sasa.csv') #error

    # identify atoms with large ASA values
    atom_index = get_atom_index_filtered_by_sasa(sasa_dict)
    print('selected indexes:', len(atom_index))
    
    # select the identified atoms
    sele_strings = make_selections_from(atom_index, flatten_wat_obj)
    print(sele_strings)

    # Show the water molecules strongly binding. 
    water_long_stay_obj = 'water_long_stay'
    cmd.create(water_long_stay_obj, sele_strings)
    cmd.show('surface', water_long_stay_obj)
    cmd.orient('polymer')

    #optional showing 
    show_interest(['polymer and resi 41+145'])
    cmd.do('set cartoon_transparency, 0.5')
    cmd.png('fig.png', width=1000, height=1000, dpi = 300, ray = 1)

main()