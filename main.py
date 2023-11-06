from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame, QLabel, \
    QPushButton, QGridLayout, QMessageBox, QLineEdit, QHBoxLayout
from PyQt5.Qt import QIntValidator, Qt
from qt_material import apply_stylesheet
import random_ign


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
        label4 = QLabel('<b>자릿수 지정 : </b>')
        self.lineedit1 = QLineEdit()
        self.do_ran = QPushButton('닉네임 추출 시작')

        self.exit_button = QPushButton("종료")
        self.selected_cho = []
        self.selected_jung = []
        self.selected_jong = []

        # 레이아웃 세팅
        frame1_gridlayout = QGridLayout()
        frame2_gridlayout = QGridLayout()
        frame3_gridlayout = QGridLayout()
        hlayout1 = QHBoxLayout()
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

        layout.addLayout(hlayout1)
        hlayout1.addWidget(label4)
        hlayout1.addWidget(self.lineedit1)
        hlayout1.addWidget(self.do_ran)
        layout.addWidget(self.exit_button)

        # 시그널 세팅
        self.do_ran.clicked.connect(self.run_ran)
        self.exit_button.clicked.connect(self.close)

        # 위젯 제약
        label4.setAlignment(Qt.AlignCenter)
        self.lineedit1.setValidator(QIntValidator())

    def run_ran(self):
        try:
            if self.lineedit1:
                digit = int(self.lineedit1.text())
                if digit <= 0 or digit > 32:
                    QMessageBox.warning(self, '입력 값 오류', '입력 된 자릿 수를 확인해 주세요.\n'
                                                         '입력 가능한 자릿 수 : 1 ~ 32')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='custom.xml')
    window = random_IGN_Create()
    window.show()
    app.exec()
