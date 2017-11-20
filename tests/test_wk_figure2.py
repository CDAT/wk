import basetest


class WKTestFigure2(basetest.BaseGraphicsTest):
    def testFigure2(self):
        print('Plotting 2')
        self.WP.plot_figure2(
            self.results("background"),
            min=-1,
            max=2,
            bg=True)
        self.checkImage("test_wk_figure2.png")
