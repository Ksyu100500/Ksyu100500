
# from PyQt5.QtWidget import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([]) #создание объекта приложения
main_win = QWidget() #создание окна
main_win.setWindowTitle('AXAXXAXAXAXAXAXAXXAXAXAXXAXAXAXAXAXAXXAA') #заголовок главного окна


main_win.resize(800,600)
main_win.show()
app.exec_()