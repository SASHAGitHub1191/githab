#print(eval(input('Введи выражение')))
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QRadioButton,QSlider,QDial,QLineEdit,QGroupBox, QHBoxLayout
from PyQt6.QtCore import Qt
from random import randint
from  random import shuffle

class Question:
    def __init__(self, question,right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer  = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
app.number_question = 0
app.final_balls = 0
window = QWidget()
window.show()

question_label = QLabel('Вопрос')
radiobutton1 = QRadioButton('Ответ1')

radiobutton2 = QRadioButton("Ответ2")

radiobutton3 = QRadioButton('Ответ3')

radiobutton4 = QRadioButton('Ответ4')
answers = [radiobutton1, radiobutton2, radiobutton3, radiobutton4]

result_label = QLabel('Неверно!')
true_answer_label = QLabel('______')
box_hline_hight = QHBoxLayout()
box_hline_low = QHBoxLayout()
def start_tast() :
    if button_answer.text() == 'Ответить':
        show_answer()
    else:
        show_question()

def show_answer():
    question_box.hide()
    answer_box.show()
    button_answer.setText('Следуйщий вопрос')
    check_answer()
    if app.number_question == 3:
        button_answer.setText('Фнал')
        answer_box.setTitle(f'{app.final_balls} из 4')
def show_question():
    question_box.show()
    answer_box.hide()
    button_answer.setText('Ответить')
    next_question()
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[3].setText(q.wrong3)
    answers[2].setText(q.wrong2)
    answers[1].setText(q.wrong1)
    question_label.setText(q.question)
    true_answer_label.setText(q.right_answer)
def check_answer():
    if answers[0].isChecked():
        result_label.setText('Верно!Ура!')
        app.final_balls += 1
    else:
        result_label.setText('Неверно!не ура!')

def next_question():
        app.number_question += 1
        ask(question_list[app.number_question])


main_line = QVBoxLayout()
question_box_vline = QVBoxLayout()
answer_box_vline = QVBoxLayout()
question_box = QGroupBox('Варианты ответов:')
answer_box = QGroupBox('Результат теста:')
button_answer = QPushButton('Ответить')
main_line.addWidget(question_label, alignment=Qt.AlignmentFlag.AlignCenter)
window.setLayout(main_line)
question_box.setLayout(question_box_vline)
question_box_vline.addLayout(box_hline_hight)
question_box_vline.addLayout(box_hline_low)
main_line.addWidget(question_box, alignment=Qt.AlignmentFlag.AlignCenter)

box_hline_hight.addWidget(radiobutton1, alignment=Qt.AlignmentFlag.AlignCenter)
box_hline_low.addWidget(radiobutton3, alignment=Qt.AlignmentFlag.AlignCenter)
box_hline_hight.addWidget(radiobutton2, alignment=Qt.AlignmentFlag.AlignCenter)
box_hline_low.addWidget(radiobutton4, alignment=Qt.AlignmentFlag.AlignCenter)

answer_box.hide()
button_answer.clicked.connect(start_tast)
main_line.addWidget(answer_box, alignment=Qt.AlignmentFlag.AlignCenter)

answer_box.setLayout(answer_box_vline)
answer_box_vline.addWidget(result_label, alignment=Qt.AlignmentFlag.AlignLeft)

main_line.addWidget(button_answer, alignment=Qt.AlignmentFlag.AlignCenter)
answer_box_vline.addWidget(true_answer_label, alignment=Qt.AlignmentFlag.AlignCenter)

question_list = [Question('Сколько планет в солнечной системе?','8','9','7',"2"),
                 Question('Скольуо городов России(2024)','1118','3000','489','759'),
                 Question('Какую планету Солнечной системы открыл в XVI в. Н. Коперник?','Землю','Юпитер','Луну','Солнце'),
                 Question(' Какой  государственный язык в Бразилии ?',  'Португальский','Английскиий','Испанский','Бразильский')]

ask(question_list[app.number_question])
print(app.final_balls)
app.exec()#исполнять

