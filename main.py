from datetime import date
from PyQt5 import QtWidgets
import pyqtgraph as pg
import sys

import plot_builder.ui_settings as ui
import plot_builder.design as design
import currency


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setGeometry(*ui.DEFAULT_GEOMETRY)
        self.setWindowTitle(ui.DEFAULT_WINDOWTITLE)
        self.baseCombo.addItems(ui.CURRENCIES)
        self.convertCombo.addItems(ui.CURRENCIES)
        self.startEdit.setDate(ui.DEFAULT_START_DATE)
        self.stopEdit.setDate(ui.DEFAULT_STOP_DATE)
        self.baseCombo.setCurrentText(ui.DEFAULT_BASE_CURRENCY)
        self.convertCombo.setCurrentText(ui.DEFAULT_CONVERT_CURRENCY)

        self.buildButton.clicked.connect(self.build_plot)

    def build_plot(self):
        print('BUILD!')
        base_currency = self.baseCombo.currentText()
        convert_currency = self.convertCombo.currentText()

        currency_pair = currency.CurrencyPair(currency_x=base_currency, currency_y=convert_currency)
        c = currency.Currency(currency_pair)

        start_date = date(*map(int, reversed(self.startEdit.text().split('.'))))
        stop_date = date(*map(int, reversed(self.stopEdit.text().split('.'))))

        json_data = c.get_rate(start_date=start_date, stop_date=stop_date)
        data = sorted([(k, v.get(convert_currency)) for k, v in json_data.get('rates').items()], key=lambda x: x[0])
        print(data)
        days = [int(day[0].replace('-', '')) for day in data]
        rates = [day[1] for day in data]

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.graphWidget.plot(days, rates)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
