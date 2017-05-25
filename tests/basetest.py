import unittest
import cdms2
import numpy.ma
import cdat_info
import os
import WK

class TestCase(unittest.TestCase):
    def setUp(self):
        self.results = cdms2.open(os.path.join(cdat_info.get_sampledata_path(),"wk_results.nc"))
        here = os.path.dirname(__file__)
        self.WP = WK.WKPlot()
        self.WP.x.scriptrun(os.path.join(here,"colormap.scr"))
        self.WP.x.setcolormap("cmap")
        self.W = WK.WK()

    def assertAllClose(self,data1,data2):
        self.assertTrue(numpy.allclose(data1,data2))


