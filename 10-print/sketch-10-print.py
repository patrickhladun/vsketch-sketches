import vsketch

class TenCodeSketch(vsketch.SketchClass):
    size = vsketch.Param(4)
    paper = vsketch.Param('a4', choices=[
        'a1', 'a2', 'a3', 'a4', 'a5', 'a6'
    ])
    layers = vsketch.Param(1, 1, 12)
    cols = vsketch.Param(40)
    rows = vsketch.Param(60)
    probability = vsketch.Param(0.60)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size(self.paper, landscape=False)
        vsk.scale("mm")
        x = 0
        y = 0

        for j in range(self.rows):
            x = 0
            y = y + self.size
            for i in range(self.cols):
                vsk.stroke(int(vsk.random(1, self.layers + 1)))
                if(vsk.random(1) < self.probability):
                    vsk.line(x, y, x + self.size, y + self.size)
                else:
                    vsk.line(x + self.size, y, x, y + self.size)
                x = x + self.size

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    TenCodeSketch.display()
