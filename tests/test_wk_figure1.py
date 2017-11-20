import basetest


class WKTestFigure1(basetest.BaseGraphicsTest):
    def testFigure1(self):
        # Now tries to do plot this...
        S, A = self.results("S"), self.results("A")
        print('Plotting 1')
        self.WP.plot_figure1(S, A, bg=True)
        self.checkImage("test_wk_figure1.png")

