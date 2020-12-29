#!/bin/bash

path='.'
for i in $(seq 0 0); do
    python t_id.py ${path}/entire_A0_index.csv 
    mv tau.out tau_${i}.out 
done