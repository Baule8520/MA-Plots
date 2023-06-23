import matplotlib.pyplot as plt

plt.plot([3.6,4.2], [0,100])

plt.xlabel('Akkuspannung [V]')
plt.ylabel('Ladezustand [%]')

#plt.show()

plt.savefig('results/LiIon.svg', format='svg', dpi=1200)
plt.clf()

################################################################
S = 12

plt.plot([3.6*S,4.2*S], [0,100])

plt.xlabel('Akkuspannung [V]')
plt.ylabel('Ladezustand [%]')

#plt.show()

plt.savefig(('results/' + str(S) +'SLiIon.svg'), format='svg', dpi=1200)
plt.clf()