import matploblib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('A0_survivalProb.dat')

exit()
fig, ax = plt.subplots(1,1, figsize=(10,5))
ax.plot(tausA[i], spsA[i], label='A')
ax.plot(tausB[i], spsB[i], label='B')
#plt.xlabel('Time ')
#plt.ylabel('Survival Probability')
#for i in range(len(inTrajs)):
#    plt.plot(taus[i], sps[i])
# plt.plot(taus[1], sps[1], label="2500bar")
plt.legend()
plt.show()