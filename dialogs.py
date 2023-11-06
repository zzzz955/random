from PyQt5.QtWidgets import QDialog, QLabel, QToolBox, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QHBoxLayout, \
    QMessageBox
import random_ign as ra
from PyQt5.Qt import QIntValidator, Qt


class create_Random_IGN(QDialog):
    def __init__(self, cho, jung, jong, digit):
        super().__init__()
        self.setWindowTitle('랜덤 닉네임 추출')

        # 위젯 생성
        self.layout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        self.glayout1 = QGridLayout()
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
        self.layout.addLayout(self.glayout1)
        self.setLayout(self.layout)

        # 시그널 추가
        self.button1.clicked.connect(lambda: self.show_igns(cho, jung, jong, digit))
        self.button2.clicked.connect(self.close)

        # 위젯 제약
        label1.setAlignment(Qt.AlignCenter)
        self.lineedit1.setValidator(QIntValidator())

    def show_igns(self, cho, jung, jong, digit):
        if self.lineedit1:
            nums = int(self.lineedit1.text())
            if nums <= 0 or nums > 20:
                QMessageBox.warning(self, '입력 값 오류', '입력 된 실행 횟수를 확인해 주세요.\n'
                                                     '입력 가능한 실행 횟수 : 1 ~ 20')
            else:
                for i in range(1, nums + 1):
                    nick_name = QLabel()
                    nick_name.setText(ra.create_random_ign(cho, jung, jong, digit))
                    index = QLabel(str(i))
                    self.glayout1.addWidget(index, i - 1, 0)
                    self.glayout1.addWidget(nick_name, i - 1, 1)