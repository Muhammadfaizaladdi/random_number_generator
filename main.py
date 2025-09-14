from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

# define the APp
app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle("Number Generator")

# buat widget
label = QLabel("Click to find Out")
winner = QLabel("?")
btn_generate = QPushButton("Generate")
main_box = QVBoxLayout()

# desain
main_box.addWidget(label)
main_box.addWidget(winner)
main_box.addWidget(btn_generate)

# Logic App
def generate_number():
    number = randint(1,100)
    winner.setText(str(number))
    label.setText("Winner")

btn_generate.clicked.connect(generate_number)

# Show and run the App
window.setLayout(main_box)
window.show()
app.exec()
