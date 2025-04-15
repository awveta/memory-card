from PyQt5.QtCore import Qt #модуль, который отвечает за внешний вид окна
from PyQt5.QtWidgets import QButtonGroup, QApplication, QGroupBox, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton #модуль отвечает за виджеты окна
from random import shuffle #модуль рандом
import random

app = QApplication([]) # создаем приложение
main_win = QWidget() #создаем окно приложения
main_win.setWindowTitle('Memory Card') #создаем надпись окна
main_win.resize(400, 200) #устанавливаем размер окна, то есть ширину и высоту в пикселях
 
#Создаем окно вопросов
button_otvet = QPushButton('Ответить')#кнопка ответа
button_next = QPushButton('Следующий вопрос')
vopros = QLabel('В каком году была основана Москва:') #вопрос

RadioGroupBox  = QGroupBox('Варианты ответов')#группа ответов
btn_answer1 = QRadioButton('2005') #Создаем вариант ответа 1
btn_answer2 = QRadioButton('2010') #Создаем вариант ответа 2
btn_answer3 = QRadioButton('2015') #Создаем вариант ответа 3
btn_answer4 = QRadioButton('2020') #Создаем вариант ответа 4

#Создаем группу переключателей
RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

#Создаем окно ответов
OtvetGroupBox = QGroupBox('Результат теста')
result = QLabel('Прав или нет?')
vern_otvet = QLabel('Ответ будет тут')

#Создаем окно с результатом
layout_result = QVBoxLayout() #вертикал. линия
layout_result.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(vern_otvet, alignment =Qt.AlignHCenter, stretch=2)
OtvetGroupBox.setLayout(layout_result)

#Создание лейатуов
layout_1 = QHBoxLayout() #горизонт. линия
layout_2 = QVBoxLayout() #верикал. линия
layout_3 = QVBoxLayout() #верикал. линия
layout_2.addWidget(btn_answer1) #ответ в левом столбце
layout_2.addWidget(btn_answer2) #ответ в левом столбце
layout_3.addWidget(btn_answer3) #ответ в правом столбце
layout_3.addWidget(btn_answer4) #ответ в правом столбце

#Размещаем 2 созданных столбца по одной горизонт. линии(наравне)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioGroupBox.setLayout(layout_1) #размещаем панель с вариантами ответов 

layout_vopros = QHBoxLayout() #горизонт. линия, где будет вопрос
layout_varianty = QHBoxLayout() # гориз. линия с группой вопросов
layout_knopka = QHBoxLayout() #гориз. линия где будет кнопка

layout_vopros.addWidget(vopros, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_varianty.addWidget(RadioGroupBox)
layout_varianty.addWidget(OtvetGroupBox)

layout_knopka.addStretch(2)
layout_knopka.addWidget(button_otvet, stretch=1) #Делаем кнопку большой
layout_knopka.addWidget(button_next,stretch=1)
layout_knopka.addStretch(2)

#Размещаем строки друг под другом
layout_card = QVBoxLayout()
layout_card.addLayout(layout_vopros, stretch=2)
layout_card.addLayout(layout_varianty, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_knopka, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #равные пробелы между содержимым

#Функция отвечает за окно результата
def show_result():
    RadioGroupBox.hide()
    OtvetGroupBox.show()

#Функция отвечает за окно вопроса
def show_vopros():
    n = random.randint(0,3)
    ask(questions_list[n])
    RadioGroupBox.show()
    OtvetGroupBox.hide()
    RadioGroup.setExclusive(False) #Сняли ограничения, чтобы сбросить выбор
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True) #Вернули ограничения


answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
#Функция записывает значения вопроса и ответов в нужные виджеты

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    vopros.setText(q.question)
    result.setText(q.right_answer)

def show_correct(res):
    vern_otvet.setText(res)
    show_result()


#Если нажат правильный ответ, то пишем Правильно, иначе Неправильно
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неправильно')

questions_list = []
questions_list.append(Question('Год создания ютуб', 
'2010', '2006', '2001', '2000'))
questions_list.append(Question('В каком году была создана роблок студио', 
'2020', '2010', '2015', '2005'))
questions_list.append(Question('Государственный язык Португалии', 
'Португальский', 'Английский', 'Испанский', 'Французский'))
questions_list.append(Question('Государственный язык РФ', 
'Русский', 'Английский', 'Испанский', 'Французский'))


OtvetGroupBox.hide()
button_otvet.clicked.connect(check_answer)
button_next.clicked.connect(show_vopros)
main_win.setLayout(layout_card)
main_win.show()
app.exec()

