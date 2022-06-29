import sys
from DesignFuelCalculator import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Calculadora(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.warmupBox = None
        super().setupUi(self)
        self.calculaBtn.clicked.connect(self.calcular)
        self.limpaBtn.clicked.connect(self.resetar)

    def calcular(self, null=None):
        try:
            raceLe = float(self.raceLeng.text())
            minLap = float(self.minLap.text())
            secLap = float(self.secLap.text())
            msLap = (self.msLap.text())
            ms = float(msLap[0:3])
            fuelPerLap = self.fuelPerLap.text()
            fuelPerLap = float(fuelPerLap.replace(',', '.'))
            warmupBox = self.warmupBox.checkState()
            totaLap = ((minLap * 60) + secLap + (ms / 1000))
            estLaps = int(round((raceLe * 60) / totaLap) + 1)
            if warmupBox == 2:
                estLaps += 1
            estFuel = estLaps * fuelPerLap
            recFuel = estFuel + fuelPerLap
            self.estLaps.setText(str(round(estLaps, 0)))
            self.estFuel.setText(str(round(estFuel, 1)))
            self.recFuel.setText(str(round(recFuel, 1)))
        except:
            pass

    def resetar(self):
        self.raceLeng.clear()
        self.minLap.clear()
        self.secLap.clear()
        self.msLap.clear()
        self.fuelPerLap.clear()
        self.estLaps.clear()
        self.estFuel.clear()
        self.recFuel.clear()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    c = Calculadora()
    c.show()
    qt.exec_()
