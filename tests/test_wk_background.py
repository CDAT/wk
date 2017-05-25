import basetest

class WKTestBackground(basetest.TestCase):
    def testBackground(self):
        S,A = self.results("S"),self.results("A")
        background = self.W.background(S,A)
        self.assertAllClose(background,self.results('background'))
