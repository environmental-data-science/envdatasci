#!usr/bin/env python
# -*- coding: utf-8 -*-
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

__author__ = 'Bryn Morgan'
__contact__ = 'bryn.morgan@geog.ucsb.edu'
__copyright__ = '(c) Bryn Morgan 2020'

__license__ = 'MIT'
__date__ = 'Fri May 22 19:26:35 2020'
__version__ = '1.0'
__status__ = 'initial release'
__url__ = ''


"""

Name:           filename.py
Compatibility:  Python 3.7.0
Description:    Description of what program does

URL:            https://

Requires:       list of libraries required

Dev ToDo:       None

AUTHOR:         Bryn Morgan
ORGANIZATION:   University of California, Santa Barbara
Contact:        bryn.morgan@geog.ucsb.edu
Copyright:      (c) Bryn Morgan 2020


"""


#% IMPORTS
import pandas as pd

def lhf_wpl(df,rho_v='rho_v',rho_d='rho_d',T_K='T_K',
           cov_h2o_Uz='cov_h2o_Uz',cov_Ts_Uz='cov_Ts_Uz'):

    '''
    Calculates latent heat flux with WPL correction.

    Parameters
    ----------
    df : DataFrame
        DataFrame with raw data for calculations.
    rho_v : str, optional
        Name of column with vapor density. The default is 'rho_v'.
    rho_d : str, optional
        Name of column with dry air density. The default is 'rho_d'.
    T_K : str, optional
        Name of column with temperature values in K. The default is 'T_K'.
    cov_h2o_Uz : str, optional
        Name of column with LHF eddy covariance term. The default is 'cov_h2o_Uz'.
    cov_Ts_Uz : str, optional
        Name of column with SHF eddy covariance term. The default is 'cov_Ts_Uz'.

    Returns
    -------
    LE : Series
        Latent heat flux values in W m-2.

    '''
    # Define constants
    lambda_v = 2440     # enthalpy of vaporization, J g-1
    M_h2o = 18.01528    # molar mass of water, g mol-1
    M_air = 28.9647     # molar mass of air, g mol-1
    
    # Calculate LHF
    LE = lambda_v * (1 + ((M_air / M_h2o)*(df[rho_v]/df[rho_d]))) * \
        (df[cov_h2o_Uz] + ((df[rho_d]/1000) / df[T_K]) * df[cov_Ts_Uz])
    
    return LE

