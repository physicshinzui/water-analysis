#!/bin/bash
set -Ceu

# water_index_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/entire_protein/1uj1'
# traj_path='/Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/skip100' 
# ref_path='/Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/200ns.pdb'

water_index_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/entire_protein/6lu7'
traj_path='/Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/skip100' 
ref_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/6lu7/em2.pdb'

# water_index_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/entire_protein/1uk3_B'
# traj_path='/Volumes/siida-SSD/corona_project/corona_B_1uk3/xtc_files/system/skip100/' 
# ref_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/1uk3_B/em2.pdb'

# water_index_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/entire_protein/mono_6lu7'
# traj_path='/Volumes/siida-SSD/corona_project/corona_mono_6lu7/xtc_files/system/skip100/' 
# ref_path='/Users/siida/Dropbox/00_Research/06_coronavirus/analysis/wat_resident_time/6lu7_mono/em2.pdb'

exe='/usr/local/Cellar/pymol/2.3.0/bin/pymol'
for i in $(seq 0 0); do
    ${exe} spotting_water.py -- ${water_index_path}/tau_${i}.out \
                                   ${ref_path} \
                                   ${traj_path}/npt_prod_${i}_skip100.xtc
    #mv fig.png fig_${i}.png
done
