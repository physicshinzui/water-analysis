#python calc_suviveProb.py -r ../00_samples/sample3/em2.pdb \
#                          -rd 6.0 \
#                          -s 'segid A and (resid 41 or resid 145)' \
#                          -b 0 \
#                          -wf 'local' \
#                          -t ../00_samples/sample3/npt_prod_0_skip100.xtc

python calc_suviveProb.py -r ../00_samples/sample3/em2.pdb \
                          -rd 6.0 \
                          -s 'segid A and (resid 41 or resid 145)' \
                          -b 0 \
                          -wf 'entire' \
                          -t ../00_samples/sample3/npt_prod_0_skip100.xtc


#python calc_suviveProb.py -r 6lu7_mono/em2.pdb \
#                          -rd 5.0 \
#                          -s 'resid 41 or resid 164 or resid 187' \
#                          -b 2000 \
#                          -t /Volumes/siida-SSD/corona_project/corona_mono_6lu7/xtc_files/system/npt_prod_0.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_mono_6lu7/xtc_files/system/npt_prod_1.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_mono_6lu7/xtc_files/system/npt_prod_2.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_mono_6lu7/xtc_files/system/npt_prod_3.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_mono_6lu7/xtc_files/system/npt_prod_4.xtc

#python calc_suviveProb.py -r 6lu7/em2.pdb \
#                          -rd 5.0 \
#                          -s 'segid A and (resid 41 or resid 164 or resid 187)' 'segid B and (resid 41 or resid 164 or resid 187)' \
#                          -b 2000 \
#                          -t /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_0.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_1.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_2.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_3.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_4.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_5.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_6.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_7.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_8.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_6lu7_apo/xtc_files/system/npt_prod_9.xtc 
                          #-s 'segid A and (resid 41 or resid 145)' 'segid B and (resid 41 or resid 145)' \


#python calc_suviveProb.py -r 1uk3_A/em2.pdb \
#                          -rd 5.0 \
#                          -s 'resid 41 or resid 164 or resid 187' \
#                          -b 2000 \
#                          -t /Volumes/siida-SSD/corona_project/corona_A_1uk3/xtc_files/system/npt_prod_0.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_A_1uk3/xtc_files/system/npt_prod_1.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_A_1uk3/xtc_files/system/npt_prod_2.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_A_1uk3/xtc_files/system/npt_prod_3.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_A_1uk3/xtc_files/system/npt_prod_4.xtc 

#python calc_suviveProb.py -r 1uk3_B/em2.pdb \
#                          -rd 5.0 \
#                          -s 'resid 41 or resid 164 or resid 187' \
#                          -b 2000 \
#                          -t /Volumes/siida-SSD/corona_project/corona_B_1uk3/xtc_files/system/npt_prod_0.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_B_1uk3/xtc_files/system/npt_prod_1.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_B_1uk3/xtc_files/system/npt_prod_2.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_B_1uk3/xtc_files/system/npt_prod_3.xtc \
#                             /Volumes/siida-SSD/corona_project/corona_B_1uk3/xtc_files/system/npt_prod_4.xtc 

python calc_suviveProb.py -r 1uj1/em2.pdb \
                          -rd 5.0 \
                          -s 'segid A and (resid 41 or resid 164 or resid 187)' 'segid B and (resid 41 or resid 164 or resid 187)' \
                          -b 2000 \
                          -t /Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/npt_prod_0.xtc \
                             /Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/npt_prod_1.xtc \
                             /Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/npt_prod_2.xtc \
                             /Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/npt_prod_3.xtc \
                             /Volumes/siida-SSD/corona_project/corona_1uj1/xtc_files/system/npt_prod_4.xtc 
#
#
