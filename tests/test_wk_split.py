import basetest


class WKTestSplit(basetest.TestCase):
    def testSplit(self):
        # Split between Sym and ASym components
        # Averages over time if compresstime is True (default)
        # ,compresstime=False,smooth=False)
        S, A = self.W.split(self.results("power"))
        self.assertAllClose(S, self.results("S"))
        self.assertAllClose(A, self.results("A"))
