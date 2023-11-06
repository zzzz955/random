from PyQt5.QtWidgets import QDialog, QLabel, QToolBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QHBoxLayout
import random_ign


class create_Random_IGN(QDialog):
    def __init__(self, cho, jung, jong):
        super().__init__()
        self.setWindowTitle('랜덤 닉네임 추출')

        # 위젯 생성
        self.layout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        label1 = QLabel('<b>추출 횟수</b>')
        self.lineedit1 = QLineEdit()
        self.button1 = QPushButton('실행')
        self.button2 = QPushButton('종료')

        # 레이아웃 추가
        self.layout.addLayout(hlayout1)
        hlayout1.addWidget(label1)
        hlayout1.addWidget(self.lineedit1)
        hlayout1.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)