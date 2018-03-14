import unittest
import cdms2
import numpy.ma
import cdat_info
import os
import WK
import checkimage
import vcs

class TestCase(unittest.TestCase):
    def setUp(self):
        self.results = cdms2.open(
            os.path.join(
                cdat_info.get_sampledata_path(),
                "wk_results.nc"))
        here = os.path.dirname(__file__)
        self.W = WK.WK()

    def assertAllClose(self, data1, data2):
        self.assertTrue(numpy.allclose(data1, data2))

class BaseGraphicsTest(TestCase):
    def __init__(self, *args, **kwargs):
        self.geometry = {"width": 1200, "height": 1090}
        if 'geometry' in kwargs:
            self.geometry = kwargs['geometry']
            del kwargs['geometry']
        self.bg = int(os.environ.get("VCS_BACKGROUND",1))
        if 'bg' in kwargs:
            self.bg = kwargs['bg']
            del kwargs['bg']
        super(BaseGraphicsTest, self).__init__(*args, **kwargs)

    def setUp(self):
        # This is for circleci that crashes for any mac bg=True
        self.x=vcs.init(geometry=self.geometry,bg=self.bg)
        self.x.setantialiasing(0)
        self.x.drawlogooff()
        if self.geometry is not None:
            self.x.setbgoutputdimensions(self.geometry['width'],
                                         self.geometry['height'],
                                         units="pixels")
        self.WP = WK.WKPlot(x=self.x)
        here = os.path.dirname(__file__)
        self.WP.x.scriptrun(os.path.join(here, "colormap.scr"))
        self.WP.x.setcolormap("cmap")
        self.orig_cwd = os.getcwd()
        self.pngsdir = "tests_png"
        if not os.path.exists(self.pngsdir):
            os.makedirs(self.pngsdir)
        self.basedir = os.path.join("tests","baselines")
        super(BaseGraphicsTest, self).setUp()

    def checkImage(self,fnm,src=None,threshold=checkimage.defaultThreshold,pngReady=False,pngPathSet=False):
        if src is None:
            src = os.path.join(self.basedir,os.path.basename(fnm))
        if not pngPathSet:
            fnm = os.path.join(self.pngsdir,fnm)
        print("Test file  :",fnm)
        print("Source file:",src)
        if not pngReady:
            self.x.png(fnm,
                       width=self.x.width,
                       height=self.x.height,
                       units="pixels")
        ret = checkimage.check_result_image(fnm,src,threshold)
        self.assertEqual(ret,0)
        return ret
    def tearDown(self):
        os.chdir(self.orig_cwd)
        self.x.clear()
        del(self.x)
        # if png dir is empty (no failures) remove it
