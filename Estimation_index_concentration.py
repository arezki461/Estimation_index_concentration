from scipy.stats import vonmises
import numpy as np
import matplotlib.pyplot as plt

def largeur95(kappa):
	x = 0
	while vonmises.cdf(x,kappa)<0.975:
		x+=0.01
	return x*(180/np.pi)

def largeur(kappa, ran=70):
	x = 0
	while vonmises.cdf(x,kappa)<0.5 + (ran/200.):
		x+=0.001
	return x*(180/np.pi)

def verif(kappa):
	largeur = largeur95(kappa)
	xx = [ 180.0*i/1000 - 90 for i in range(1000)]
	yy = [ vonmises.pdf( x*2*np.pi/180,kappa)/vonmises.pdf(0,kappa) for x in xx]
	plt.plot(xx,yy)
	plt.vlines( [-largeur/2, largeur/2], 0, 1, color='red')
	plt.show()
	return