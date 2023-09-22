
## pip install python-srtm
## environment variable SRTM1_DIR must be set

import srtm

class FitnessFunction:
    def __init__(self):
        self.data = srtm.Srtm1HeightMapCollection()

    def __call__(self,x):
        try:
            elev = self.data.get_altitude(latitude=x[0],longitude=x[1])
        except srtm.exceptions.NoHeightMapDataException:
            elev = None
        return elev


