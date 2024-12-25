from PySide6.QtWidgets import QWidget
from my_design import Ui_TemperatureConversion
 
 
class Widget(QWidget,Ui_TemperatureConversion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)# helps to run ui here through ide
        self.setWindowTitle("Temperature Converter")
        # connecting with our ui
        self.celsius_lineEdit.textChanged.connect(self.convert_temp)
        self.fahrenheit_lineEdit.textChanged.connect(self.convert_temp)
        self.celsius_lineEdit2.textChanged.connect(self.convert_temp)
        self.fahrenheit_lineEdit2.textChanged.connect(self.convert_temp)
        self.kelvin_lineEdit.textChanged.connect(self.convert_temp)
        self.kelvin_lineEdit2.textChanged.connect(self.convert_temp)
        # creating functions
    def convert_temp(self):
        try:
            # check input field 
            sender=self.sender()
            
            # celsius to fahrenheit and fahrenheit to celsius
            if sender == self.celsius_lineEdit:
                celsius_value=float(self.celsius_lineEdit.text())
                fahrenheit_value=self.celsius_to_fahrenheit(celsius_value)
                self.fahrenheit_lineEdit.setText(f"{fahrenheit_value:.2f} ⁰F")
            
            elif sender==self.fahrenheit_lineEdit:
                fahrenheit_value=float(self.fahrenheit_lineEdit.text())
                celsius_value=self.fahrenheit_to_celsius(fahrenheit_value)
                self.celsius_lineEdit.setText(f"{celsius_value:.2f} ⁰C")
                
                # celsius to kelvin
            if sender == self.celsius_lineEdit2:
                celsius_value=float(self.celsius_lineEdit2.text())
                Kelvin_value=self.celsius_to_kelvin(celsius_value)
                self.kelvin_lineEdit.setText(f"{Kelvin_value:.2f} K")
            
            elif sender==self.kelvin_lineEdit:
                Kelvin_value=float(self.kelvin_lineEdit.text())
                celsius_value=self.kelvin_to_celsius(Kelvin_value)
                self.celsius_lineEdit2.setText(f"{celsius_value:.2f} ⁰C")
                
                # fahrenheit to kelvin
            if sender == self.fahrenheit_lineEdit2:
                fahrenheit_value=float(self.fahrenheit_lineEdit2.text())
                Kelvin_value=self.fahrenheit_to_kelvin(fahrenheit_value)
                self.kelvin_lineEdit2.setText(f"{Kelvin_value:.2f} K")
            
            elif sender==self.kelvin_lineEdit2:
                Kelvin_value=float(self.kelvin_lineEdit2.text())
                fahrenheit_value=self.kelvin_to_fahrenheit(Kelvin_value)
                self.fahrenheit_lineEdit2.setText(f"{fahrenheit_value:.2f} ⁰F")
            
            
        except ValueError:
            pass
            
  
    def celsius_to_fahrenheit(self,celsius):
       return(celsius*9/5) + 32
  
    def fahrenheit_to_celsius(self,fahrenheit):
       return(fahrenheit-32)*5/9
   
    def celsius_to_kelvin(self,celsius):
        return(celsius)+273.15
  
    def kelvin_to_celsius(self,kelvin):
        return(kelvin-273.15)
    
    def fahrenheit_to_kelvin(self,fahrenheit):
        return(fahrenheit-32)*5/9 +273.15
    
    def kelvin_to_fahrenheit(self,kelvin):
        return(kelvin-273.15)*9/5+32