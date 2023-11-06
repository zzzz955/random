from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame, QLabel, \
    QPushButton, QGridLayout, QMessageBox
from qt_material import apply_stylesheet


class random_IGN_Create(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("랜덤 닉네임 추출")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 위젯 선언
        frame1 = QFrame(self)
        frame2 = QFrame(self)
        frame3 = QFrame(self)
        label1 = QLabel("<b>윗 자음 선택</b>")
        label2 = QLabel("<b>모음 선택</b>")
        label3 = QLabel("<b>아랫 자음 선택</b>")
        self.do_ran = QPushButton('닉네임 추출 시작')

        self.exit_button = QPushButton("종료")
        self.selected_cho = []
        self.selected_jung = []
        self.selected_jong = []

        # 레이아웃 세팅
        frame1_gridlayout = QGridLayout()
        frame2_gridlayout = QGridLayout()
        frame3_gridlayout = QGridLayout()
        layout.addWidget(label1)
        layout.addWidget(frame1)
        frame1.setLayout(frame1_gridlayout)
        for i in range(3):
            for j in range(7):
                if i * 7 + j == 19:
                    break
                self.cho_button = QPushButton(str(chr(0x1100 + (i * 7 + j))))
                frame1_gridlayout.addWidget(self.cho_button, i, j)
                self.cho_button.setCheckable(True)
                self.selected_cho.append(self.cho_button)

        layout.addWidget(label2)
        layout.addWidget(frame2)
        frame2.setLayout(frame2_gridlayout)
        for i in range(3):
            for j in range(7):
                if i * 7 + j == 21:
                    break
                self.jung_button = QPushButton(str(chr(0x1161 + (i * 7 + j))))
                frame2_gridlayout.addWidget(self.jung_button, i, j)
                self.jung_button.setCheckable(True)
                self.selected_jung.append(self.jung_button)

        layout.addWidget(label3)
        layout.addWidget(frame3)
        frame3.setLayout(frame3_gridlayout)
        for i in range(4):
            for j in range(7):
                if i * 7 + j == 27:
                    break
                self.jong_button = QPushButton(str(chr(0x11A8 + (i * 7 + j))))
                frame3_gridlayout.addWidget(self.jong_button, i, j)
                self.jong_button.setCheckable(True)
                self.selected_jong.append(self.jong_button)
        layout.addWidget(self.exit_button)

        # 시그널 세팅


if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='custom.xml')
    window = random_IGN_Create()
    window.show()
    app.exec()
