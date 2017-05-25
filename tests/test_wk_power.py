import basetest
import cdms2
import cdat_info
import os

class WKTestPower(basetest.TestCase):
    def testPower(self):
        with cdms2.open(os.path.join(cdat_info.get_sampledata_path(),"wk_data.nc")) as f:
            data = f("rlut",time=slice(0,150),latitude=(-15,15))

        ## Process the data, i.e compute spectral wave number and frequencies
        power = self.W.process(data)
        self.assertAllClose(power,self.results("power"))
