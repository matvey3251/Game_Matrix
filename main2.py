import pygame
import random
import pygame_gui
import os
import pickle

pygame.init()

W = 1000
H = 700
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Matrix")
myfont = pygame.font.SysFont('cambria', 40)

background = pygame.Surface((W, H))
background1 = pygame.Surface((W, H))
reg = pygame.Surface((W, H))
res = pygame.Surface((W, H))
result = pygame.Surface((W, H))
first = pygame.Surface((W, H))
account = pygame.Surface((W, H))
last_results = pygame.Surface((W, H))
teacher_window = pygame.Surface((W, H))
reg_teacher = pygame.Surface((W, H))
log_teacher = pygame.Surface((W, H))
res_ch = pygame.Surface((W, H))

background.fill(pygame.Color('#2496c1'))
background1 = pygame.image.load('font.png')
first = pygame.image.load('Illustration3.png')
reg.fill(pygame.Color('#30d5c8'))
res.fill(pygame.Color('#30d5c8'))
result.fill(pygame.Color('#30d5c8'))
account.fill(pygame.Color('#30d5c8'))
last_results.fill(pygame.Color('#30d5c8'))
teacher_window.fill(pygame.Color('#30d5c3'))
reg_teacher.fill(pygame.Color('#30d5c3'))
log_teacher.fill(pygame.Color('#30d5c3'))
res_ch.fill(pygame.Color('#30d5c3'))

manager = pygame_gui.UIManager((W, H))
manager1 = pygame_gui.UIManager((W, H))
manager2 = pygame_gui.UIManager((W, H))
manager3 = pygame_gui.UIManager((W, H))
manager4 = pygame_gui.UIManager((W, H))
manager5 = pygame_gui.UIManager((W, H))
manager6 = pygame_gui.UIManager((W, H))
manager7 = pygame_gui.UIManager((W, H))
manager8 = pygame_gui.UIManager((W, H))
manager9 = pygame_gui.UIManager((W, H))
manager10 = pygame_gui.UIManager((W, H))
manager11 = pygame_gui.UIManager((W, H))
manager12 = pygame_gui.UIManager((W, H))

accept_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((852, 653), (150, 50)),
                                          text='Принять',
                                          manager=manager)

colvo = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 100), (300, 50)),
                                    text='Выберите кол-во чисел от и до:',
                                    manager=manager)

settings = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 0), (300, 50)), text='НАСТРОЙКИ:',
                                       manager=manager)

drop = pygame_gui.elements.UISelectionList(item_list=['2', '3', '4'], relative_rect=pygame.Rect((8, 148), (154, 75)),
                                           manager=manager)

drop2 = pygame_gui.elements.UISelectionList(item_list=['2', '3', '4'], relative_rect=pygame.Rect((158, 148), (154, 75)),
                                            manager=manager)

start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 350), (150, 50)),
                                         text='НАЧАТЬ',
                                         manager=manager1)

yes_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 350), (150, 50)),
                                       text='Да',
                                       manager=manager3)
no_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 350), (150, 50)),
                                      text='Нет',
                                      manager=manager3)
num = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                  text='Хотите посмотреть результаты?', manager=manager3)

login = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 150), (300, 50)), manager=manager6)

password = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 250), (300, 50)), manager=manager6)

llogin = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                     text='Логин: ', manager=manager6)

ppasword = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 200), (400, 50)),
                                       text='Пароль: ', manager=manager6)

ppasword2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 300), (400, 50)),
                                        text='Подтвердите пароль: ', manager=manager6)

password2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 350), (300, 50)), manager=manager6)

rreg = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((393, 380), (200, 50)),
                                    text='Зарегистрироваться',
                                    manager=manager6)

i_got_acc = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                         text='У меня уже есть аккаунт',
                                         manager=manager6)

llogin1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                      text='Ваш логин: ', manager=manager7)

ppasword1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 200), (400, 50)),
                                        text='Ваш пароль: ', manager=manager7)

login1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 150), (300, 50)), manager=manager7)

password1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 250), (300, 50)), manager=manager7)

enter = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                     text='Зарегистрироваться ',
                                     manager=manager7)

lllogin = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((368, 280), (250, 50)),
                                       text='Войти',
                                       manager=manager7)

leave = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-2, (H - 48)), (250, 50)),
                                     text='Выйти из игры',
                                     manager=manager6)

yep = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (200, 50)),
                                  text='Правильных ответов:', manager=manager4)

noo = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((210, 0), (200, 50)),
                                  text='Неправильных ответов:', manager=manager4)

num = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                  text='Выберите границы чисел в примере от и до:', manager=manager)

back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((230, 350), (170, 50)),
                                    text='Выйти из аккаунта',
                                    manager=manager1)

bback = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                     text='Назад',
                                     manager=manager8)

drop3 = pygame_gui.elements.UISelectionList(item_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                                                       '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
    , '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42',
                                                       '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53'
    , '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72',
                                                       '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
                                                       '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
                                                       '93', '94', '95', '96', '97', '98', '99', '100'],
                                            relative_rect=pygame.Rect((348, 148), (204, 75)), manager=manager, )

drop4 = pygame_gui.elements.UISelectionList(item_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                                                       '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
    , '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42',
                                                       '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53'
    , '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72',
                                                       '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
                                                       '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
                                                       '93', '94', '95', '96', '97', '98', '99', '100'],
                                            relative_rect=pygame.Rect((548, 148), (204, 75)), manager=manager, )

drop5 = pygame_gui.elements.UISelectionList(item_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                                                       '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
    , '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42',
                                                       '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53'
    , '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72',
                                                       '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
                                                       '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
                                                       '93', '94', '95', '96', '97', '98', '99', '100'],
                                            relative_rect=pygame.Rect((348, 219), (204, 75)), manager=manager, )

drop6 = pygame_gui.elements.UISelectionList(item_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                                                       '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
    , '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42',
                                                       '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53'
    , '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72',
                                                       '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
                                                       '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
                                                       '93', '94', '95', '96', '97', '98', '99', '100'],
                                            relative_rect=pygame.Rect((548, 219), (204, 75)), manager=manager, )

div_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 350), (150, 50)),
                                       text='Деление',
                                       manager=manager)

um_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 350), (150, 50)),
                                      text='Умножение',
                                      manager=manager)

plus_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 350), (150, 50)),
                                        text='Плюс',
                                        manager=manager)

minus_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 350), (150, 50)),
                                         text='Минус',
                                         manager=manager)

randm_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 350), (150, 50)),
                                         text='Перемешка',
                                         manager=manager)

ll_r = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 350), (200, 50)),
                                    text='Предыдущие результаты',
                                    manager=manager1)

###############################Вход препа##########################################################
tch_back = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                        text='Назад',
                                        manager=manager10)

tch1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((368, 280), (250, 50)),
                                    text='Войти в аккаунт',
                                    manager=manager10)

llogin2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                      text='Ваш логин: ', manager=manager10)

ppasword2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 200), (400, 50)),
                                        text='Ваш пароль: ', manager=manager10)

login3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 150), (300, 50)), manager=manager10)

password3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 250), (300, 50)), manager=manager10)

ppasword6 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 0), (400, 50)),
                                        text='ВХОД ДЛЯ УЧИТЕЛЯ', manager=manager10)

########################################################################
##########################Регистрация препа#############################
tch2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((393, 380), (200, 50)),
                                    text='Зарегистрироваться',
                                    manager=manager11)

tch_back1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                         text='Назад',
                                         manager=manager11)

login6 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 150), (300, 50)),
                                             manager=manager11)

password6 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 250), (300, 50)),
                                                manager=manager11)

llogin6 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                      text='Логин: ', manager=manager11)

ppasword6 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 200), (400, 50)),
                                        text='Пароль: ', manager=manager11)

u = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 300), (400, 50)),
                                text='Подтвердите пароль: ', manager=manager11)

q = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 0), (400, 50)),
                                text='РЕГИСТРАЦИЯ УЧИТЕЛЯ', manager=manager11)

password7 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((343, 350), (300, 50)),
                                                manager=manager11)

##############################################################################################
##############################Вывод результатов для препа (ВВОД)#####################################

gh = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((W - 400) / 2, 100), (400, 50)),
                                 text='Введите логин ученика:', manager=manager9)

ch_login = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(((W - 300) / 2, 150), (300, 50)),
                                               manager=manager9)

ch_but = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((W - 200) / 2, 180), (200, 50)),
                                      text='Посмотреть статистику',
                                      manager=manager9)

bbback = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                      text='Назад',
                                      manager=manager9)

##############################Вывод результатов ученика для препа (ИТОГ)#####################################

back_ch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 652), (250, 50)),
                                       text='Назад',
                                       manager=manager12)

speed = 20

White = (225, 225, 225)
MCLR = (150, 180, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Lavender = (141, 94, 182)
Mint = (15, 254, 173)
YG = (177, 251, 31)
Black = (255, 255, 255)
green = (0, 255, 0)

scores = 0
no = 0
FPS = 120
clock = pygame.time.Clock()

a1 = 2
a2 = 4
a3 = 0
a4 = 0
a5 = 10
a6 = 10

x1 = 800
x2 = 800
x3 = 800
x4 = 800
x5 = 800
x6 = 800

spisok = ['/', '*', '+', '-']

gh = [x1, x2, x3, x4, x5, x6]

surf = pygame.Surface((200, 200))
surf.fill(Red)

yu = [85, 185, 285, 385, 485, 585]  # Список координат, для рандомного размещения
fake = []
hard = [10, 30, 100, 20, 50, -10, -30, -40, -50]
random.shuffle(hard)

x = 0  # Координаты примера
y = random.choice(yu)  # Координаты примера
z = random.choice(yu)  # Координаты ответа

flLeft = flRight = False
flUp = flDown = False
var1 = False

hh = 800
flag = 0
fflag = False

r = ['']
n = ['']
nn = ['']
jn = False
kjk = False

currentaccount = None


####################################################REGISTRATION########################################################
class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = myfont.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        sc.blit(self.image, self.rect)
        sc.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        global pole, lt_ri, lt_wr, ri, wr, er, data, currentaccount, fg, n
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            fg = len(n)
            f = open('data.txt', 'rb')
            data = pickle.load(f)
            f.close()

            data.remove(currentaccount)

            for i in range(fg):
                n[i] = n[i] + ' = ' + str(nn[i])

            lg = currentaccount['login']
            pas = currentaccount['password']
            lt_ri = currentaccount['latest_ri']
            lt_wr = currentaccount['latest_wr']
            er = currentaccount['err']
            wr = currentaccount['wrong']
            ri = currentaccount['right']

            lt_ri += scores
            lt_wr += no
            ri = scores
            wr = no
            if len(er) >= 5:
                del er[0]
            er.append(n)

            currentaccount['latest_ri'] = lt_ri
            currentaccount['latest_wr'] = lt_wr
            currentaccount['err'] = er
            currentaccount['wrong'] = wr
            currentaccount['right'] = ri

            data.append(currentaccount)

            f = open('data.txt', 'wb')
            pickle.dump(data, f)
            f.close()
            pole = 3

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = myfont.render(self.text_input, True, "green")
        else:
            self.text = myfont.render(self.text_input, True, "white")


class BButton():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = myfont.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        sc.blit(self.image, self.rect)
        sc.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        global pole, currentaccount, x1, x2, x3, x4, x5, x6, x, n, nn, no, scores
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            pole = 5
            x1 = 800
            x2 = 800
            x3 = 800
            x4 = 800
            x5 = 800
            x6 = 800
            x = 0
            n.clear()
            nn.clear()
            no = 0
            scores = 0
            currentaccount = None
            randomex()

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = myfont.render(self.text_input, True, "green")
        else:
            self.text = myfont.render(self.text_input, True, "white")


button_surface = pygame.image.load('img_2.png')
button_surface = pygame.transform.scale(button_surface, (200, 47))

button_surface1 = pygame.image.load('img_2.png')
button_surface1 = pygame.transform.scale(button_surface, (200, 47))

button = Button(button_surface, 900, 676, 'exit')
button_exit = BButton(button_surface1, 900, 676, 'exit')


def start_pole():
    global pole, flag, currentaccount, n
    time_delta = clock.tick(60) / 1000.0
    miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                       text='Добро пожаловать, ' + str(currentaccount['login']) + '!',
                                       manager=manager1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_btn:
                    pole = 2
                    print(n)
                    flag = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                pole = 1
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ll_r:
                    pole = 7
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back:
                    pole = 5
                    currentaccount = None

        manager1.process_events(event)
    manager1.update(time_delta)
    sc.blit(background1, (0, 0))
    manager1.draw_ui(sc)
    pygame.display.update()


def ress():
    global pole, n, nn
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == yes_btn:
                    print(n)
                    pole = 4
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == no_btn:
                    exit()

        manager3.process_events(event)
    manager3.update(time_delta)
    sc.blit(res, (0, 0))
    manager3.draw_ui(sc)
    pygame.display.update()


def Draw_new_Pole():
    global pole, a1, a2, a3, a4, a5, a6, z, x, spisok, flag
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == accept_btn and flag == 0:
                    x = 0
                    pole = 0
                elif event.ui_element == accept_btn and flag == 1:
                    x = 0
                    pole = 2
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == drop:
                    a1 = int(event.text)
                    x = 0
                    if a2 < a1:
                        a1 = 1
                        a2 = 2
                        err = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 100), (300, 50)),
                                                          text='Число 1 должно быть меньше числа 2', manager=manager)
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == drop2:
                    a2 = int(event.text)
                    x = 0
                    if a2 < a1:
                        a1 = 2
                        a2 = 2
                        err = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 100), (300, 50)),
                                                          text='Число 1 должно быть меньше числа 2', manager=manager)
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == drop3:
                    a3 = int(event.text)
                    x = 0
                    if a3 > a5:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a3 = 1
                        a5 = 10
                    if a4 > a6:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a4 = 1
                        a6 = 10
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == drop4:
                    a4 = int(event.text)
                    x = 0
                    if a3 > a5:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a3 = 1
                        a5 = 10
                    if a4 > a6:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a4 = 1
                        a6 = 10
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == drop5:
                    a5 = int(event.text)
                    x = 0
                    if a3 > a5:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a3 = 1
                        a5 = 10
                    if a4 > a6:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a4 = 1
                        a6 = 10
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == drop6:
                    a6 = int(event.text)
                    x = 0
                    if a3 > a5:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a3 = 1
                        a5 = 10
                    if a4 > a6:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 100), (400, 50)),
                                                           text='Число 1 должно быть больше числа 2', manager=manager)
                        a4 = 1
                        a6 = 10
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == div_btn:
                    spisok.clear()
                    spisok.append('/')
                    x = 0
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == um_btn:
                    spisok.clear()
                    spisok.append('*')
                    x = 0
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == plus_btn:
                    spisok.clear()
                    spisok.append('+')
                    x = 0
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == minus_btn:
                    spisok.clear()
                    spisok.append('-')
                    x = 0
                    randomex()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == randm_btn:
                    spisok.clear()
                    spisok = ['/', '*', '+', '-']
                    x = 0
                    randomex()

        manager.process_events(event)
    manager.update(time_delta)
    sc.blit(background, (0, 0))
    manager.draw_ui(sc)
    pygame.display.update()


def Ork(numObj, digits=0):
    return float(f"{numObj:.{digits}f}")


def randomex():
    global example, solved, a1
    num = random.randint(a1, a2)
    valid = False
    while not valid:
        example = ''
        for i in range(num - 1):
            example += str(random.randint(a3, a5))
            example += random.choice(spisok)
        example += str(random.randint(a4, a6))
        try:
            solved1 = eval(example)
            solved = float(Ork(solved1, 3))
            if isinstance(solved, int) or isinstance(solved, float):
                valid = True
        except:
            pass


def score():
    global scores
    scores += 1


def miss():
    global no
    no += 1


def Draw_pole():
    global x, y, pole, x1, x2, x3, x4, x5, x6, hh, flag, fflag, no, ttv, scores, r, n, example, jn, kjk, solved, nn
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 100
            elif event.key == pygame.K_DOWN:
                y += 100
            elif event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                pole = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pole = 0
                flag = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())
    fake.clear()
    for i in range(6):
        fake.append(Ork(solved + hard[i], 3))
    sc.blit(first, (0, 0))

    button.changeColor(pygame.mouse.get_pos())
    button.update()

    textsurface = myfont.render(str(example), False, Blue)
    textsurface2 = myfont.render(str(solved), False, Blue)
    example1 = myfont.render(str(fake[1]), False, Blue)
    example2 = myfont.render(str(fake[2]), False, Blue)
    example3 = myfont.render(str(fake[3]), False, Blue)
    example4 = myfont.render(str(fake[4]), False, Blue)
    example5 = myfont.render(str(fake[0]), False, Blue)

    g = textsurface.get_width()
    f = textsurface2.get_width()
    ex1 = example1.get_width()
    ex2 = example2.get_width()
    ex3 = example3.get_width()
    ex4 = example4.get_width()
    ex5 = example5.get_width()

    u1 = 900 - ex1 / 2
    u2 = 900 - ex2 / 2
    u3 = 900 - ex3 / 2
    u4 = 900 - ex4 / 2
    u5 = 900 - ex5 / 2

    if x == x1 - g and y == yu[2]:
        fflag = True
    if x == x2 - g and y == yu[2]:
        fflag = True
    if x == x3 - g and y == yu[2]:
        fflag = True
    if x == x4 - g and y == yu[2]:
        fflag = True
    if x == x5 - g and y == yu[2]:
        fflag = True
    if x == x6 - g and y == yu[2]:
        fflag = True

    if y == 85 and x == x1 - g and fflag == True:
        score()

    if y == 185 and x == x2 - g and fflag == True:
        score()

    if y == 285 and x == x3 - g and fflag == True:
        score()

    if y == 385 and x == x4 - g and fflag == True:
        score()

    if y == 485 and x == x5 - g and fflag == True:
        score()

    if y == 585 and x == x6 - g and fflag == True:
        score()

    if y == 85 and x == x1 - g and fflag != True:
        x1 -= 10
        n.append(example)
        nn.append(solved)
        print(n)
        miss()
    if y == 185 and x == x2 - g and fflag != True:
        x2 -= 10
        n.append(example)
        nn.append(solved)
        print(n)
        miss()

    if y == 285 and x == x3 - g and fflag != True:
        x3 -= 10
        n.append(example)
        nn.append(solved)
        print(n)
        miss()
    if y == 385 and x == x4 - g and fflag != True:
        x4 -= 10
        n.append(example)
        nn.append(solved)
        print(n)
        miss()
    if y == 485 and x == x5 - g and fflag != True:
        x5 -= 10
        n.append(example)
        nn.append(solved)
        print(n)
        miss()
    if y == 585 and x == x6 - g and fflag != True:
        x6 -= 10
        n.append(example)
        nn.append(solved)
        print(n)
        miss()

    pygame.draw.lines(sc, White, False, [(x1, 50), (x1, 150)], 5)
    pygame.draw.lines(sc, White, False, [(x2, 150), (x2, 250)], 5)
    pygame.draw.lines(sc, White, False, [(x3, 250), (x3, 350)], 5)
    pygame.draw.lines(sc, White, False, [(x4, 350), (x4, 450)], 5)
    pygame.draw.lines(sc, White, False, [(x5, 450), (x5, 550)], 5)
    pygame.draw.lines(sc, White, False, [(x6, 550), (x6, 650)], 5)

    if y < -10:
        y = 85
    elif y > 650:
        y = 585
    elif x > x1 - g and y == 85:
        x = 0
        fflag = False
        y = random.choice(yu)
        random.shuffle(yu)
        randomex()
    elif x > x2 - g and y == 185:
        x = 0
        fflag = False
        y = random.choice(yu)
        random.shuffle(yu)
        randomex()
    elif x > x3 - g and y == 285:
        x = 0
        fflag = False
        y = random.choice(yu)
        random.shuffle(yu)
        randomex()
    elif x > x4 - g and y == 385:
        x = 0
        fflag = False
        y = random.choice(yu)
        random.shuffle(yu)
        randomex()
    elif x > x5 - g and y == 485:
        x = 0
        fflag = False
        y = random.choice(yu)
        random.shuffle(yu)
        randomex()
    elif x > x6 - g and y == 585:
        x = 0
        fflag = False
        y = random.choice(yu)
        random.shuffle(yu)
        randomex()

    keys = pygame.key.get_pressed()

    x += 1
    if x < x1 - 50 - g and y == 85:
        if keys[pygame.K_SPACE]:
            x += speed
    if x < x2 - 50 - g and y == 185:
        if keys[pygame.K_SPACE]:
            x += speed
    if x < x3 - 50 - g and y == 285:
        if keys[pygame.K_SPACE]:
            x += speed
    if x < x4 - 50 - g and y == 385:
        if keys[pygame.K_SPACE]:
            x += speed
    if x < x5 - 50 - g and y == 485:
        if keys[pygame.K_SPACE]:
            x += speed
    if x < x6 - 50 - g and y == 585:
        if keys[pygame.K_SPACE]:
            x += speed

    sc.blit(textsurface, (x, y))
    sc.blit(textsurface2, (900 - f / 2, yu[2]))
    sc.blit(example1, (900 - ex1 / 2, yu[1]))
    sc.blit(example2, (900 - ex2 / 2, yu[3]))
    sc.blit(example3, (900 - ex3 / 2, yu[4]))
    sc.blit(example4, (900 - ex4 / 2, yu[5]))
    sc.blit(example5, (900 - ex5 / 2, yu[0]))

    # отрисовка поля
    pygame.draw.lines(sc, White, False, [(0, 50), (997, 50), (997, 650), (0, 650)], 5)
    pygame.draw.lines(sc, White, False, [(0, 150), (997, 150)], 5)
    pygame.draw.lines(sc, White, False, [(0, 250), (997, 250)], 5)
    pygame.draw.lines(sc, White, False, [(0, 350), (997, 350)], 5)
    pygame.draw.lines(sc, White, False, [(0, 450), (997, 450)], 5)
    pygame.draw.lines(sc, White, False, [(0, 550), (997, 550)], 5)
    pygame.display.update()


def resss():
    global scores, no, n, xx

    time_delta = clock.tick(60) / 1000.0
    xx = str(n)
    hh = xx[4:-1]
    trru = myfont.render(str(scores), False, Blue)
    ffalse = myfont.render(str(no), False, Blue)
    labble1 = myfont.render('Кол-во неправильных ответов: ', False, Blue)
    labble = myfont.render('Кол-во правильных ответов:', False, Blue)
    txt = myfont.render('Ошибочные примеры:', False, Blue)
    gg = labble.get_width()
    pp = labble1.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_exit.checkForInput(pygame.mouse.get_pos())
        manager5.process_events(event)
    try:
        num2 = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((0, 140), (400, 30)),
                                                                    options_list=n, starting_option=n[1],
                                                                    manager=manager5)
    except:
        num2 = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((0, 140), (400, 30)),
                                                                    options_list=['Все правильно, молодец!'],
                                                                    starting_option='Все правильно, молодец!',
                                                                    manager=manager5)

    manager.update(time_delta)
    sc.blit(result, (0, 0))
    button_exit.changeColor(pygame.mouse.get_pos())
    button_exit.update()
    manager5.update(time_delta)
    sc.blit(txt, (0, 100))
    sc.blit(ffalse, (pp, 40))
    sc.blit(labble1, (0, 40))
    sc.blit(labble, (0, 0))
    sc.blit(trru, (gg + 7, 0))
    manager5.draw_ui(sc)
    pygame.display.update()


######################################REG#####################################################
def tch():
    global pole
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == tch_back:
                    pole = 5
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == tch1:
                    login = login3.get_text()
                    password = password3.get_text()
                    f = open('tch.txt', 'rb')
                    data_tch1 = pickle.load(f)
                    f.close()
                    if login == data_tch1['login']:
                        if password == data_tch1['password']:
                            pole = 8
                        else:
                            miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 55), (400, 40)),
                                                               text='Не верный пароль', manager=manager10)
                    else:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 55), (400, 40)),
                                                           text='Не верный логин', manager=manager10)

        manager10.process_events(event)
    manager10.update(time_delta)
    sc.blit(account, (0, 0))
    manager10.draw_ui(sc)
    pygame.display.update()


def tch_log():
    global pole
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == tch_back1:
                    pole = 5
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == tch2:
                    login = login6.get_text()
                    password = password6.get_text()
                    password2 = password7.get_text()
                    if login.rstrip() != '' and password.rstrip() != '':
                        if password == password2:
                            data_tch = {'login': login, 'password': password}
                            f = open('tch.txt', 'wb')
                            pickle.dump(data_tch, f)
                            f.close()
                            pole = 8
                            break
                        else:
                            miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 55), (400, 40)),
                                                               text='Пароли не совпадают', manager=manager11)
                    else:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 55), (400, 40)),
                                                           text='Заполните все поля', manager=manager11)

        manager11.process_events(event)
    manager11.update(time_delta)
    sc.blit(account, (0, 0))
    manager11.draw_ui(sc)
    pygame.display.update()


def window1():
    global pole, flag, login, f, registr, currentaccount
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == i_got_acc:
                    pole = 6
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                if os.path.isfile('tch.txt'):
                    pole = 9
                else:
                    pole = 10
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == leave:
                    exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == rreg:
                    if login.get_text().rstrip() != '' and password.get_text().rstrip() != '':
                        if password.get_text().rstrip() == password2.get_text().rstrip():
                            if os.path.isfile('data.txt'):
                                f = open('data.txt', 'rb')
                                list = pickle.load(f)
                                f.close()
                            else:
                                list = []
                            login_data = login.get_text().rstrip()
                            pas_data = password.get_text().rstrip()
                            check_login = True
                            for i in list:
                                if login_data == i['login']:
                                    check_login = False
                            if check_login == True:
                                registr = {
                                    'login': login_data,
                                    'password': pas_data,
                                    'latest_ri': 0,
                                    'latest_wr': 0,
                                    'err': [],
                                    'wrong': 0,
                                    'right': 0
                                }
                                list.append(registr)
                                f = open("data.txt", "wb")
                                pickle.dump(list, f)
                                f.close()
                                currentaccount = registr

                                pole = 0
                                break
                            else:
                                miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                                                   text='Такой логин уже существует', manager=manager6)
                        else:
                            miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                                               text='Пароли не совпадают', manager=manager6)
                    else:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                                           text='Заполните все поля', manager=manager6)
        manager6.process_events(event)
    manager6.update(time_delta)
    sc.blit(reg, (0, 0))
    manager6.draw_ui(sc)
    pygame.display.update()

    def save_data():
        login_data = login.get_text()
        pas_data = password.get_text()
        registr = {'login': login_data, 'password': pas_data, 'latest': None, 'err': [], 'wrong': None, 'right': None}
        f = open("data.txt", "wb")
        pickle.dump(registr, f)
        f.close()


def accoun():
    global pole, flag, registr, currentaccount, lg, pas, lt_ri, lt_wr, er, wr, ri
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == enter:
                    pole = 5
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == lllogin:
                    if os.path.isfile('data.txt'):
                        f = open('data.txt', 'rb')
                        data = pickle.load(f)
                        f.close()
                        check_acc = False
                        for i in data:
                            if login1.get_text() == i['login']:
                                check_acc = True
                                if password1.get_text() == i['password']:
                                    lg = i['login']
                                    pas = i['password']
                                    lt_ri = i['latest_ri']
                                    lt_wr = i['latest_wr']
                                    er = i['err']
                                    wr = i['wrong']
                                    ri = i['right']
                                    currentaccount = i

                                    pole = 0
                                else:
                                    miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                                                       text='Неправильный пароль', manager=manager7)
                        if check_acc == False:
                            miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                                               text='Неправильный логин', manager=manager7)
                    else:
                        miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 100), (400, 50)),
                                                           text='Неправильный логин или пароль', manager=manager7)

        manager7.process_events(event)
    manager7.update(time_delta)
    sc.blit(account, (0, 0))
    manager7.draw_ui(sc)
    pygame.display.update()


######################################END_REG#####################################################


def l_r():
    global pole, flag, registr, currentaccount, lg, pas, data, lg, pas, lt_ri, er, wr, ri, lt_wr
    time_delta = clock.tick(60) / 1000.0
    mass = []
    for i in range(len(currentaccount['err'])):
        mass.append('GAME ' + str(i + 1))
        mass += currentaccount['err'][i]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bback:
                    pole = 0
        manager8.process_events(event)
    try:
        num2 = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((0, 180), (400, 30)),
                                                                    options_list=mass, starting_option=mass[1],
                                                                    manager=manager8)
    except:
        num2 = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((0, 180), (400, 30)),
                                                                    options_list=['Нет предыдущих результатов'],
                                                                    starting_option='Нет предыдущих результатов',
                                                                    manager=manager8)
    labble1 = myfont.render('Кол-во неправильных ответов за все время: ', False, Blue)
    labble = myfont.render('Кол-во правильных ответов за все время:', False, Blue)
    labble2 = myfont.render('Кол-во неправильных ответов в прошлой игре:', False, Blue)
    labble3 = myfont.render('Кол-во правильных ответов в прошлой игре:', False, Blue)
    trru = myfont.render(str(currentaccount['latest_ri']), False, Blue)
    fall = myfont.render(str(currentaccount['latest_wr']), False, Blue)
    trru1 = myfont.render(str(currentaccount['right']), False, Blue)
    fall1 = myfont.render(str(currentaccount['wrong']), False, Blue)
    manager8.update(time_delta)
    sc.blit(last_results, (0, 0))
    manager8.draw_ui(sc)
    sc.blit(labble1, (0, 40))
    sc.blit(labble, (0, 0))
    sc.blit(trru, (780, 0))
    sc.blit(fall, (820, 40))
    sc.blit(labble2, (0, 80))
    sc.blit(labble3, (0, 120))
    sc.blit(trru1, (840, 120))
    sc.blit(fall1, (880, 80))
    pygame.display.update()


def teacher_w():
    global pole, cur_ch, masss
    time_delta = clock.tick(60) / 1000.0
    f = open('tch.txt', 'rb')
    data_tch = pickle.load(f)
    f.close()
    f = open('data.txt', 'rb')
    data_t = pickle.load(f)
    f.close()
    masss = []
    for i in data_t:
        if ch_login.get_text() == i['login']:
            cur_ch = i
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bbback:
                    pole = 5
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ch_but:
                    pole = 11

        manager9.process_events(event)
    miss = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(((W - 400) / 2, 0), (400, 50)),
                                       text='Добро пожаловать, ' + str(data_tch['login']) + '!',
                                       manager=manager9)
    sc.blit(teacher_window, (0, 0))
    manager9.update(time_delta)
    manager9.draw_ui(sc)
    pygame.display.update()


def ch_result():
    global pole, pas, data, lg, pas, lt_ri, er, wr, ri, lt_wr, masss, cur_ch
    time_delta = clock.tick(60) / 1000.0
    masss = []
    for i in range(len(cur_ch['err'])):
        masss.append('GAME ' + str(i + 1))
        masss += cur_ch['err'][i]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_ch:
                    pole = 8
        manager12.process_events(event)
    try:
        num2 = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((0, 180), (400, 30)),
                                                                    options_list=masss, starting_option=masss[1],
                                                                    manager=manager12)
    except:
        num2 = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect=pygame.Rect((0, 180), (400, 30)),
                                                                    options_list=['Нет предыдущих результатов'],
                                                                    starting_option='Нет предыдущих результатов',
                                                                    manager=manager12)

    sc.blit(teacher_window, (0, 0))
    labble1 = myfont.render('Кол-во неправильных ответов за все время: ', False, Blue)
    labble = myfont.render('Кол-во правильных ответов за все время:', False, Blue)
    labble2 = myfont.render('Кол-во неправильных ответов в прошлой игре:', False, Blue)
    labble3 = myfont.render('Кол-во правильных ответов в прошлой игре:', False, Blue)
    trru = myfont.render(str(cur_ch['latest_ri']), False, Blue)
    fall = myfont.render(str(cur_ch['latest_wr']), False, Blue)
    trru1 = myfont.render(str(cur_ch['right']), False, Blue)
    fall1 = myfont.render(str(cur_ch['wrong']), False, Blue)
    manager12.update(time_delta)
    sc.blit(last_results, (0, 0))
    manager12.draw_ui(sc)
    sc.blit(labble1, (0, 40))
    sc.blit(labble, (0, 0))
    sc.blit(trru, (780, 0))
    sc.blit(fall, (820, 40))
    sc.blit(labble2, (0, 80))
    sc.blit(labble3, (0, 120))
    sc.blit(trru1, (840, 120))
    sc.blit(fall1, (880, 80))
    pygame.display.update()


randomex()
pole = 5
while 1:
    if pole == 2:
        Draw_pole()
    elif pole == 1:
        Draw_new_Pole()
    elif pole == 0:
        start_pole()
    elif pole == 3:
        ress()
    elif pole == 4:
        resss()
    elif pole == 5:
        window1()
    elif pole == 6:
        accoun()
    elif pole == 7:
        l_r()
    elif pole == 8:
        teacher_w()
    elif pole == 9:
        tch()
    elif pole == 10:
        tch_log()
    elif pole == 11:
        ch_result()

    clock.tick(FPS)

''' последний результаты
    логин 
    пароль 
    список непр. примеров и ответов
    общая статистика'''