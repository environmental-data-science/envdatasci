import pandas as pd
from hydrodata import Station
import hydrodata.datasets as hds

def get_ET_wateryear(station_id, water_year, to_csv=False):
    """ Retrieves a single year of ET data from SSEBop service

    Parameters
    ----------
        station_id : str
            The USGS Streamgauge station ID
        water_year : int
            The water year to request
        to_csv : Boolean, optional
            If True, data is written to the class data folder
            (default is False)

    Returns
    -------
        ET data in a pandas DataFrame (only if to_csv is False)
    
    """
    start = str(int(water_year) - 1) + '-10-01'
    end = str(water_year) + '-09-30'
    wshed = Station(start=start, end=end, station_id=station_id, data_dir="../data/lab_1/")
    ET = hds.ssebopeta_byloc(wshed.lon, wshed.lat, start=wshed.start, end=wshed.end, verbose=True)
    ET = ET.rename(columns={'eta (mm/day)':'ET [mm/day]'})
    if to_csv:
        ET.to_csv('../data/lab_1/SSEBop_{sid}_{year}.csv'.format(sid=station_id, year=water_year)) 
        print('ET written to ../data/lab_1/SSEBop_{sid}_{year}.csv'.format(sid=station_id, year=water_year))
    else:
        return ET