import pandas as pd 
import numpy as np

def main():
    taus_half = []
    for i in range(10):
        #df = pd.read_csv(f'1uk3_A/triad_taumax1000/A{i}_survivalProb.dat', comment='#', header = None, index_col = 0, delimiter=' ')
        #df = pd.read_csv(f'1uk3_B/triad_taumax1000/A{i}_survivalProb.dat', comment='#', header = None, index_col = 0, delimiter=' ')
        
        #df = pd.read_csv(f'6lu7_mono/triad_taumax1000/A{i}_survivalProb.dat', comment='#', header = None, index_col = 0, delimiter=' ')
        df = pd.read_csv(f'6lu7/triad_taumax1000/A{i}_survivalProb.dat', comment='#', header = None, index_col = 0, delimiter=' ')
        #df = pd.read_csv(f'6lu7/triad_taumax1000/B{i}_survivalProb.dat', comment='#', header = None, index_col = 0, delimiter=' ')

        sp_half = 0.5
        #print(df <= sp_half)
        df = df[df <= sp_half].dropna()
        if len(df)==0: 
            taus_half.append(np.inf)
        else:
            taus_half.append(df.head(1).index[0])
#        print('time <= tau_0.5 : ',

    print(list(map(lambda x:round(x*0.1,2), taus_half)))
    print(f'mean tau_0.5 and std = {np.mean(taus_half)} {np.std(taus_half)}')
    print(f'max = {np.max(taus_half)}' )

if __name__ == '__main__':
    main()
