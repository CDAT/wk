# Adapted for numpy/ma/cdms2 by convertcdms.py
import cdms2
import WK
import cdutil
import os
import cdat_info
import unittest


class WKTest(unittest.TestCase):
    def setUp(self):
        f = cdms2.open(os.path.join(cdat_info.get_sampledata_path(), 'clt.nc'))

        self.data = f('clt')

        self.W = WK.WK()

    def testNoBoundsFails(self):
        with self.assertRaises(Exception) as e:
            p = self.W.process(self.data)

    def testProcess(self):
        cdutil.times.setTimeBoundsMonthly(self.data)
        p = self.W.process(self.data)
        self.assertEqual(p.shape, (1, 46, 97, 73))

        s, a = self.W.split(p)

        b = self.W.background(s, a)
        self.assertEqual(b.shape, (97, 73))
