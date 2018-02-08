import matplotlib.pyplot as plt
plt.switch_backend('agg')

class plotter():
    def  __init__(self):
        import itertools
        self.marker = itertools.cycle((',', '+', '.', 'o', '*'))
        self.handles=[]
    def plot(self,x,y, xLabel="Number of Classes",yLabel = "Accuracy", legend="none",title="none"):
        self.x = x
        self.y = y
        plt.grid(color='r', linestyle='-', linewidth=2)
        self.handles.append(plt.plot(x,y,linestyle='--', marker=next(self.marker), label=legend))

        self.xLabel = xLabel
        self.yLabel = yLabel
        plt.title(title)

    def saveFig(self, path):
        plt.legend(handles=self.handles)
        plt.ylim( (0, 100) )
        plt.xlim((0,100))
        plt.ylabel(self.yLabel)
        plt.xlabel(self.xLabel)
        plt.savefig(path)

if __name__=="__main__":
    pl = plotter()
    pl.plot([1,2,3,4], [2,3,6,2])
    pl.saveFig("test.jpg")
