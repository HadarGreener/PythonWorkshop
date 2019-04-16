#Import all libraries
import numpy as np #In order to define matrices etc.
from matplotlib import pyplot as plt 
from astropy.table import Table #importing Table object
import astropy.units as u #importing astropy.units w/ alias "u"
plt.ion()


def find_distance(dist_mod):
    """
    Find the distance in parsecs given a distance modulus
    
    Parameters
    ----------
    dist_mod: array-like
        distance modulus
        
    Returns
    ---------
    distance: array-like
        distance in parsecs
    """
    distance = 10**((dist_mod+5)/5)
    return distance

def par2megapar(parsec):
    '''
    This function takes a distance in parsec and converts it to a distance in megaparsecs
    
    Parameters
    -----------
    parsec: flt or array-like 
        distance in parsec 
    
    Returns
    ----------
    megapar: flt or array-like
        distance in megaparsec
    
    '''
    megapar = parsec/10**6
    return megapar


#if __name__ == "__main__":
if True: #Makes sure that the interactive plot works
	filename = '../../data/python/hubble_data.dat' #name of file
	tbdata = Table.read(filename,
        	           names = ['galaxy', 'supernova',
                            'm', 'sig_m',
                            'dist_mod', 'sig_dist_mod',
                            'M', 'sig_M',
                            'velocity'],
                   format='ascii') #Give each column a title


	dist_pc = find_distance(tbdata['dist_mod'])
	dist_mpc = par2megapar(dist_pc)

	fit = np.polyfit(dist_mpc, tbdata['velocity'],1)

	plt.plot(dist_mpc,tbdata['velocity'],'o')
	plt.plot(dist_mpc,np.polyval(fit,dist_mpc)) #Plot fit. Generate y values for x values using this poly. fit
	plt.xlabel('Distance (Mpc)')
	plt.ylabel(r'Velocity ($\rm km s^{-1}$)') #r is for "raw string"
	plt.title('Hubble Diagram')
	plt.legend() #Automatic legend

	plt.savefig('hubble_diagram.pdf') #Guesses format via .__

	plt.show()
