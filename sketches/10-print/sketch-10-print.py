import vsketch

class TenPrintSketch(vsketch.SketchClass):
    # Sketch parameters:
    size = vsketch.Param(6)
    paper = vsketch.Param('a4', choices=[
        'a1', 'a2', 'a3', 'a4', 'a5', 'a6'
    ])
    num_x = vsketch.Param(30)
    num_y = vsketch.Param(45)
    probability = vsketch.Param(0.60)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size(self.paper, landscape=False)
        vsk.scale("mm")
        x = 0
        y = 0

        for j in range(self.num_y):
            x = 0
            y = y + self.size
            for i in range(self.num_x):
                if(vsk.random(1) < self.probability):
                    vsk.line(x, y, x + self.size, y + self.size)
                else:
                    vsk.line(x + self.size, y, x, y + self.size)
                x = x + self.size


    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    TenCodeSketch.display()
