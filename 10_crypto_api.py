from PySide2.QtWidgets import QApplication, QWidget
from design import Ui_Form
import requests

class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.show()

        self.key = "https://api.binance.com/api/v3/ticker/price?symbol="

        self.btn_add_city.clicked.connect(self.add_city)

        self.btn_get_weather.clicked.connect(self.get_weather)

    
    def add_city(self):
        city_name = self.txt_city_info.text().upper()
        self.city_list_combo_box.addItem(city_name)
        self.txt_city_info.clear()

    
    def get_weather(self):
        current_city_name = self.city_list_combo_box.currentText()
        url = self.key + current_city_name + "USDT"
        data = requests.get(url).json()

        city_weather = round(float(data['weather']),2)
        city_name = data['symbol']

        self.lbl_weather_info.setText(city_name + ' ' + str(city_weather))



        

app = QApplication()
widget = Widget()
app.exec_()
