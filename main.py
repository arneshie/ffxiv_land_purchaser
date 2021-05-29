from threading import Thread, Lock

import win32gui
import win32con
import win32api
from time import sleep

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QFormLayout

# Hook into the process
hwndMain = win32gui.FindWindow("FINAL FANTASY XIV", "FINAL FANTASY XIV")
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

# delays array, in ms
global delays
delays = [500, 800, 400, 400, 1000]


def main():

    # mutex lock - singleton
    y = Lock()

    # UI
    app = QApplication([])
    app.setStyle('Fusion')
    window = QWidget()
    layout = QFormLayout()

    # text inputs
    e1 = QLineEdit()
    e1.setText(str(delays[0]))
    e1.setValidator(QDoubleValidator(0, 10, 0))

    e2 = QLineEdit()
    e2.setText(str(delays[1]))
    e2.setValidator(QDoubleValidator(0, 10, 0))

    e3 = QLineEdit()
    e3.setText(str(delays[2]))
    e3.setValidator(QDoubleValidator(0, 10, 0))

    e4 = QLineEdit()
    e4.setText(str(delays[3]))
    e4.setValidator(QDoubleValidator(0, 10, 0))

    e5 = QLineEdit()
    e5.setText(str(delays[4]))
    e5.setValidator(QDoubleValidator(0, 10, 0))

    # add to layout
    layout.addRow('Delay of 1st keypress:', e1)
    layout.addRow('Delay of 2nd keypress:', e2)
    layout.addRow('Delay of 3rd keypress:', e3)
    layout.addRow('Delay of 4th keypress:', e4)
    layout.addRow('Delay of 5th keypress:', e5)

    # Toggle button
    button = QPushButton('Start')
    button.clicked.connect(lambda: toggle(button, y))

    # Update button
    update_button = QPushButton('Update Delays')
    update_button.clicked.connect(lambda: update_handler(e1, e2, e3, e4, e5))

    layout.addWidget(button)
    layout.addWidget(update_button)

    window.setLayout(layout)
    window.show()

    window.setWindowTitle('FF14 Land Purchaser')
    app.exec_()


if __name__ == "__main__":
    main()