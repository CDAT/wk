import basetest


class WKTestFigure3(basetest.TestCase):
    def testFigure3(self):
        S, A = self.results("S"), self.results("A")
        background = self.results("background")
        sid = S.id
        aid = A.id
        S /= background
        A /= background
        S.id = sid
        A.id = aid

        print 'Plotting 3'
        self.WP.plot_figure3(S, A, delta_isofill=.2, delta_isoline=.1, bg=True)
