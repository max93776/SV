from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1622, 951)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.console = QtWidgets.QScrollArea(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 850, 1041, 51))
        self.console.setWidgetResizable(True)
        self.console.setObjectName("console")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1039, 49))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.console.setWidget(self.scrollAreaWidgetContents)
        self.IP = QtWidgets.QLabel(self.centralwidget)
        self.IP.setGeometry(QtCore.QRect(1240, 870, 381, 31))
        self.IP.setObjectName("IP")
        self.p1 = QtWidgets.QPushButton(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(250, 20, 71, 71))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QPushButton(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(330, 20, 71, 71))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QPushButton(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(410, 20, 71, 71))
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QPushButton(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(490, 20, 71, 71))
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QPushButton(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(570, 20, 71, 71))
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QPushButton(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(650, 20, 71, 71))
        self.p6.setObjectName("p6")
        self.p7 = QtWidgets.QPushButton(self.centralwidget)
        self.p7.setGeometry(QtCore.QRect(730, 20, 71, 71))
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QPushButton(self.centralwidget)
        self.p8.setGeometry(QtCore.QRect(810, 20, 71, 71))
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QPushButton(self.centralwidget)
        self.p9.setGeometry(QtCore.QRect(890, 20, 71, 71))
        self.p9.setObjectName("p9")
        self.p10 = QtWidgets.QPushButton(self.centralwidget)
        self.p10.setGeometry(QtCore.QRect(970, 20, 71, 71))
        self.p10.setObjectName("p10")
        self.p12 = QtWidgets.QPushButton(self.centralwidget)
        self.p12.setGeometry(QtCore.QRect(330, 100, 71, 71))
        self.p12.setObjectName("p12")
        self.p14 = QtWidgets.QPushButton(self.centralwidget)
        self.p14.setGeometry(QtCore.QRect(490, 100, 71, 71))
        self.p14.setObjectName("p14")
        self.p11 = QtWidgets.QPushButton(self.centralwidget)
        self.p11.setGeometry(QtCore.QRect(250, 100, 71, 71))
        self.p11.setObjectName("p11")
        self.p18 = QtWidgets.QPushButton(self.centralwidget)
        self.p18.setGeometry(QtCore.QRect(810, 100, 71, 71))
        self.p18.setObjectName("p18")
        self.p16 = QtWidgets.QPushButton(self.centralwidget)
        self.p16.setGeometry(QtCore.QRect(650, 100, 71, 71))
        self.p16.setObjectName("p16")
        self.p19 = QtWidgets.QPushButton(self.centralwidget)
        self.p19.setGeometry(QtCore.QRect(890, 100, 71, 71))
        self.p19.setObjectName("p19")
        self.p13 = QtWidgets.QPushButton(self.centralwidget)
        self.p13.setGeometry(QtCore.QRect(410, 100, 71, 71))
        self.p13.setObjectName("p13")
        self.p15 = QtWidgets.QPushButton(self.centralwidget)
        self.p15.setGeometry(QtCore.QRect(570, 100, 71, 71))
        self.p15.setObjectName("p15")
        self.p17 = QtWidgets.QPushButton(self.centralwidget)
        self.p17.setGeometry(QtCore.QRect(730, 100, 71, 71))
        self.p17.setObjectName("p17")
        self.p20 = QtWidgets.QPushButton(self.centralwidget)
        self.p20.setGeometry(QtCore.QRect(970, 100, 71, 71))
        self.p20.setObjectName("p20")
        self.p22 = QtWidgets.QPushButton(self.centralwidget)
        self.p22.setGeometry(QtCore.QRect(330, 180, 71, 71))
        self.p22.setObjectName("p22")
        self.p24 = QtWidgets.QPushButton(self.centralwidget)
        self.p24.setGeometry(QtCore.QRect(490, 180, 71, 71))
        self.p24.setObjectName("p24")
        self.p21 = QtWidgets.QPushButton(self.centralwidget)
        self.p21.setGeometry(QtCore.QRect(250, 180, 71, 71))
        self.p21.setObjectName("p21")
        self.p28 = QtWidgets.QPushButton(self.centralwidget)
        self.p28.setGeometry(QtCore.QRect(810, 180, 71, 71))
        self.p28.setObjectName("p28")
        self.p26 = QtWidgets.QPushButton(self.centralwidget)
        self.p26.setGeometry(QtCore.QRect(650, 180, 71, 71))
        self.p26.setObjectName("p26")
        self.p29 = QtWidgets.QPushButton(self.centralwidget)
        self.p29.setGeometry(QtCore.QRect(890, 180, 71, 71))
        self.p29.setObjectName("p29")
        self.p23 = QtWidgets.QPushButton(self.centralwidget)
        self.p23.setGeometry(QtCore.QRect(410, 180, 71, 71))
        self.p23.setObjectName("p23")
        self.p25 = QtWidgets.QPushButton(self.centralwidget)
        self.p25.setGeometry(QtCore.QRect(570, 180, 71, 71))
        self.p25.setObjectName("p25")
        self.p27 = QtWidgets.QPushButton(self.centralwidget)
        self.p27.setGeometry(QtCore.QRect(730, 180, 71, 71))
        self.p27.setObjectName("p27")
        self.p30 = QtWidgets.QPushButton(self.centralwidget)
        self.p30.setGeometry(QtCore.QRect(970, 180, 71, 71))
        self.p30.setObjectName("p30")
        self.p32 = QtWidgets.QPushButton(self.centralwidget)
        self.p32.setGeometry(QtCore.QRect(330, 260, 71, 71))
        self.p32.setObjectName("p32")
        self.p34 = QtWidgets.QPushButton(self.centralwidget)
        self.p34.setGeometry(QtCore.QRect(490, 260, 71, 71))
        self.p34.setObjectName("p34")
        self.p31 = QtWidgets.QPushButton(self.centralwidget)
        self.p31.setGeometry(QtCore.QRect(250, 260, 71, 71))
        self.p31.setObjectName("p31")
        self.p38 = QtWidgets.QPushButton(self.centralwidget)
        self.p38.setGeometry(QtCore.QRect(810, 260, 71, 71))
        self.p38.setObjectName("p38")
        self.p36 = QtWidgets.QPushButton(self.centralwidget)
        self.p36.setGeometry(QtCore.QRect(650, 260, 71, 71))
        self.p36.setObjectName("p36")
        self.p39 = QtWidgets.QPushButton(self.centralwidget)
        self.p39.setGeometry(QtCore.QRect(890, 260, 71, 71))
        self.p39.setObjectName("p39")
        self.p33 = QtWidgets.QPushButton(self.centralwidget)
        self.p33.setGeometry(QtCore.QRect(410, 260, 71, 71))
        self.p33.setObjectName("p33")
        self.p35 = QtWidgets.QPushButton(self.centralwidget)
        self.p35.setGeometry(QtCore.QRect(570, 260, 71, 71))
        self.p35.setObjectName("p35")
        self.p37 = QtWidgets.QPushButton(self.centralwidget)
        self.p37.setGeometry(QtCore.QRect(730, 260, 71, 71))
        self.p37.setObjectName("p37")
        self.p40 = QtWidgets.QPushButton(self.centralwidget)
        self.p40.setGeometry(QtCore.QRect(970, 260, 71, 71))
        self.p40.setObjectName("p40")
        self.p42 = QtWidgets.QPushButton(self.centralwidget)
        self.p42.setGeometry(QtCore.QRect(330, 340, 71, 71))
        self.p42.setObjectName("p42")
        self.p44 = QtWidgets.QPushButton(self.centralwidget)
        self.p44.setGeometry(QtCore.QRect(490, 340, 71, 71))
        self.p44.setObjectName("p44")
        self.p41 = QtWidgets.QPushButton(self.centralwidget)
        self.p41.setGeometry(QtCore.QRect(250, 340, 71, 71))
        self.p41.setObjectName("p41")
        self.p48 = QtWidgets.QPushButton(self.centralwidget)
        self.p48.setGeometry(QtCore.QRect(810, 340, 71, 71))
        self.p48.setObjectName("p48")
        self.p46 = QtWidgets.QPushButton(self.centralwidget)
        self.p46.setGeometry(QtCore.QRect(650, 340, 71, 71))
        self.p46.setObjectName("p46")
        self.p49 = QtWidgets.QPushButton(self.centralwidget)
        self.p49.setGeometry(QtCore.QRect(890, 340, 71, 71))
        self.p49.setObjectName("p49")
        self.p43 = QtWidgets.QPushButton(self.centralwidget)
        self.p43.setGeometry(QtCore.QRect(410, 340, 71, 71))
        self.p43.setObjectName("p43")
        self.p45 = QtWidgets.QPushButton(self.centralwidget)
        self.p45.setGeometry(QtCore.QRect(570, 340, 71, 71))
        self.p45.setObjectName("p45")
        self.p47 = QtWidgets.QPushButton(self.centralwidget)
        self.p47.setGeometry(QtCore.QRect(730, 340, 71, 71))
        self.p47.setObjectName("p47")
        self.p50 = QtWidgets.QPushButton(self.centralwidget)
        self.p50.setGeometry(QtCore.QRect(970, 340, 71, 71))
        self.p50.setObjectName("p50")
        self.p52 = QtWidgets.QPushButton(self.centralwidget)
        self.p52.setGeometry(QtCore.QRect(330, 420, 71, 71))
        self.p52.setObjectName("p52")
        self.p54 = QtWidgets.QPushButton(self.centralwidget)
        self.p54.setGeometry(QtCore.QRect(490, 420, 71, 71))
        self.p54.setObjectName("p54")
        self.p51 = QtWidgets.QPushButton(self.centralwidget)
        self.p51.setGeometry(QtCore.QRect(250, 420, 71, 71))
        self.p51.setObjectName("p51")
        self.p58 = QtWidgets.QPushButton(self.centralwidget)
        self.p58.setGeometry(QtCore.QRect(810, 420, 71, 71))
        self.p58.setObjectName("p58")
        self.p56 = QtWidgets.QPushButton(self.centralwidget)
        self.p56.setGeometry(QtCore.QRect(650, 420, 71, 71))
        self.p56.setObjectName("p56")
        self.p59 = QtWidgets.QPushButton(self.centralwidget)
        self.p59.setGeometry(QtCore.QRect(890, 420, 71, 71))
        self.p59.setObjectName("p59")
        self.p53 = QtWidgets.QPushButton(self.centralwidget)
        self.p53.setGeometry(QtCore.QRect(410, 420, 71, 71))
        self.p53.setObjectName("p53")
        self.p55 = QtWidgets.QPushButton(self.centralwidget)
        self.p55.setGeometry(QtCore.QRect(570, 420, 71, 71))
        self.p55.setObjectName("p55")
        self.p57 = QtWidgets.QPushButton(self.centralwidget)
        self.p57.setGeometry(QtCore.QRect(730, 420, 71, 71))
        self.p57.setObjectName("p57")
        self.p60 = QtWidgets.QPushButton(self.centralwidget)
        self.p60.setGeometry(QtCore.QRect(970, 420, 71, 71))
        self.p60.setObjectName("p60")
        self.p62 = QtWidgets.QPushButton(self.centralwidget)
        self.p62.setGeometry(QtCore.QRect(330, 500, 71, 71))
        self.p62.setObjectName("p62")
        self.p64 = QtWidgets.QPushButton(self.centralwidget)
        self.p64.setGeometry(QtCore.QRect(490, 500, 71, 71))
        self.p64.setObjectName("p64")
        self.p61 = QtWidgets.QPushButton(self.centralwidget)
        self.p61.setGeometry(QtCore.QRect(250, 500, 71, 71))
        self.p61.setObjectName("p61")
        self.p68 = QtWidgets.QPushButton(self.centralwidget)
        self.p68.setGeometry(QtCore.QRect(810, 500, 71, 71))
        self.p68.setObjectName("p68")
        self.p66 = QtWidgets.QPushButton(self.centralwidget)
        self.p66.setGeometry(QtCore.QRect(650, 500, 71, 71))
        self.p66.setObjectName("p66")
        self.p69 = QtWidgets.QPushButton(self.centralwidget)
        self.p69.setGeometry(QtCore.QRect(890, 500, 71, 71))
        self.p69.setObjectName("p69")
        self.p63 = QtWidgets.QPushButton(self.centralwidget)
        self.p63.setGeometry(QtCore.QRect(410, 500, 71, 71))
        self.p63.setObjectName("p63")
        self.p65 = QtWidgets.QPushButton(self.centralwidget)
        self.p65.setGeometry(QtCore.QRect(570, 500, 71, 71))
        self.p65.setObjectName("p65")
        self.p67 = QtWidgets.QPushButton(self.centralwidget)
        self.p67.setGeometry(QtCore.QRect(730, 500, 71, 71))
        self.p67.setObjectName("p67")
        self.p70 = QtWidgets.QPushButton(self.centralwidget)
        self.p70.setGeometry(QtCore.QRect(970, 500, 71, 71))
        self.p70.setObjectName("p70")
        self.p72 = QtWidgets.QPushButton(self.centralwidget)
        self.p72.setGeometry(QtCore.QRect(330, 580, 71, 71))
        self.p72.setObjectName("p72")
        self.p74 = QtWidgets.QPushButton(self.centralwidget)
        self.p74.setGeometry(QtCore.QRect(490, 580, 71, 71))
        self.p74.setObjectName("p74")
        self.p71 = QtWidgets.QPushButton(self.centralwidget)
        self.p71.setGeometry(QtCore.QRect(250, 580, 71, 71))
        self.p71.setObjectName("p71")
        self.p78 = QtWidgets.QPushButton(self.centralwidget)
        self.p78.setGeometry(QtCore.QRect(810, 580, 71, 71))
        self.p78.setObjectName("p78")
        self.p76 = QtWidgets.QPushButton(self.centralwidget)
        self.p76.setGeometry(QtCore.QRect(650, 580, 71, 71))
        self.p76.setObjectName("p76")
        self.p79 = QtWidgets.QPushButton(self.centralwidget)
        self.p79.setGeometry(QtCore.QRect(890, 580, 71, 71))
        self.p79.setObjectName("p79")
        self.p73 = QtWidgets.QPushButton(self.centralwidget)
        self.p73.setGeometry(QtCore.QRect(410, 580, 71, 71))
        self.p73.setObjectName("p73")
        self.p75 = QtWidgets.QPushButton(self.centralwidget)
        self.p75.setGeometry(QtCore.QRect(570, 580, 71, 71))
        self.p75.setObjectName("p75")
        self.p77 = QtWidgets.QPushButton(self.centralwidget)
        self.p77.setGeometry(QtCore.QRect(730, 580, 71, 71))
        self.p77.setObjectName("p77")
        self.p80 = QtWidgets.QPushButton(self.centralwidget)
        self.p80.setGeometry(QtCore.QRect(970, 580, 71, 71))
        self.p80.setObjectName("p80")
        self.p82 = QtWidgets.QPushButton(self.centralwidget)
        self.p82.setGeometry(QtCore.QRect(330, 660, 71, 71))
        self.p82.setObjectName("p82")
        self.p84 = QtWidgets.QPushButton(self.centralwidget)
        self.p84.setGeometry(QtCore.QRect(490, 660, 71, 71))
        self.p84.setObjectName("p84")
        self.p81 = QtWidgets.QPushButton(self.centralwidget)
        self.p81.setGeometry(QtCore.QRect(250, 660, 71, 71))
        self.p81.setObjectName("p81")
        self.p88 = QtWidgets.QPushButton(self.centralwidget)
        self.p88.setGeometry(QtCore.QRect(810, 660, 71, 71))
        self.p88.setObjectName("p88")
        self.p86 = QtWidgets.QPushButton(self.centralwidget)
        self.p86.setGeometry(QtCore.QRect(650, 660, 71, 71))
        self.p86.setObjectName("p86")
        self.p89 = QtWidgets.QPushButton(self.centralwidget)
        self.p89.setGeometry(QtCore.QRect(890, 660, 71, 71))
        self.p89.setObjectName("p89")
        self.p83 = QtWidgets.QPushButton(self.centralwidget)
        self.p83.setGeometry(QtCore.QRect(410, 660, 71, 71))
        self.p83.setObjectName("p83")
        self.p85 = QtWidgets.QPushButton(self.centralwidget)
        self.p85.setGeometry(QtCore.QRect(570, 660, 71, 71))
        self.p85.setObjectName("p85")
        self.p87 = QtWidgets.QPushButton(self.centralwidget)
        self.p87.setGeometry(QtCore.QRect(730, 660, 71, 71))
        self.p87.setObjectName("p87")
        self.p90 = QtWidgets.QPushButton(self.centralwidget)
        self.p90.setGeometry(QtCore.QRect(970, 660, 71, 71))
        self.p90.setObjectName("p90")
        self.p92 = QtWidgets.QPushButton(self.centralwidget)
        self.p92.setGeometry(QtCore.QRect(330, 740, 71, 71))
        self.p92.setObjectName("p92")
        self.p94 = QtWidgets.QPushButton(self.centralwidget)
        self.p94.setGeometry(QtCore.QRect(490, 740, 71, 71))
        self.p94.setObjectName("p94")
        self.p91 = QtWidgets.QPushButton(self.centralwidget)
        self.p91.setGeometry(QtCore.QRect(250, 740, 71, 71))
        self.p91.setObjectName("p91")
        self.p98 = QtWidgets.QPushButton(self.centralwidget)
        self.p98.setGeometry(QtCore.QRect(810, 740, 71, 71))
        self.p98.setObjectName("p98")
        self.p96 = QtWidgets.QPushButton(self.centralwidget)
        self.p96.setGeometry(QtCore.QRect(650, 740, 71, 71))
        self.p96.setObjectName("p96")
        self.p99 = QtWidgets.QPushButton(self.centralwidget)
        self.p99.setGeometry(QtCore.QRect(890, 740, 71, 71))
        self.p99.setObjectName("p99")
        self.p93 = QtWidgets.QPushButton(self.centralwidget)
        self.p93.setGeometry(QtCore.QRect(410, 740, 71, 71))
        self.p93.setObjectName("p93")
        self.p95 = QtWidgets.QPushButton(self.centralwidget)
        self.p95.setGeometry(QtCore.QRect(570, 740, 71, 71))
        self.p95.setObjectName("p95")
        self.p97 = QtWidgets.QPushButton(self.centralwidget)
        self.p97.setGeometry(QtCore.QRect(730, 740, 71, 71))
        self.p97.setObjectName("p97")
        self.p100 = QtWidgets.QPushButton(self.centralwidget)
        self.p100.setGeometry(QtCore.QRect(970, 740, 71, 71))
        self.p100.setObjectName("p100")
        self.s1=0
        self.s2=0
        self.s3=0
        self.s4=0
        self.s5=0
        self.s6=0
        self.s7=0
        self.s8=0
        self.s9=0
        self.s10=0
        self.s11=0
        self.s12=0
        self.s13=0
        self.s14=0
        self.s15=0
        self.s16=0
        self.s17=0
        self.s18=0
        self.s19=0
        self.s20=0
        self.s21=0
        self.s22=0
        self.s23=0
        self.s24=0
        self.s25=0
        self.s26=0
        self.s27=0
        self.s28=0
        self.s29=0
        self.s30=0
        self.s31=0
        self.s32=0
        self.s33=0
        self.s34=0
        self.s35=0
        self.s36=0
        self.s37=0
        self.s38=0
        self.s39=0
        self.s40=0
        self.s41=0
        self.s42=0
        self.s43=0
        self.s44=0
        self.s45=0
        self.s46=0
        self.s47=0
        self.s48=0
        self.s49=0
        self.s50=0
        self.s51=0
        self.s52=0
        self.s53=0
        self.s54=0
        self.s55=0
        self.s56=0
        self.s57=0
        self.s58=0
        self.s59=0
        self.s60=0
        self.s61=0
        self.s62=0
        self.s63=0
        self.s64=0
        self.s65=0
        self.s66=0
        self.s67=0
        self.s68=0
        self.s69=0
        self.s70=0
        self.s71=0
        self.s72=0
        self.s73=0
        self.s74=0
        self.s75=0
        self.s76=0
        self.s77=0
        self.s78=0
        self.s79=0
        self.s80=0
        self.s81=0
        self.s82=0
        self.s83=0
        self.s84=0
        self.s85=0
        self.s86=0
        self.s87=0
        self.s88=0
        self.s89=0
        self.s90=0
        self.s91=0
        self.s92=0
        self.s93=0
        self.s94=0
        self.s95=0
        self.s96=0
        self.s97=0
        self.s98=0
        self.s99=0
        self.s100=0
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(50, 20, 111, 31))
        self.Name.setObjectName("Name")
        self.Chat = QtWidgets.QLabel(self.centralwidget)
        self.Chat.setGeometry(QtCore.QRect(1110, 30, 201, 41))
        self.Chat.setObjectName("Chat")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1110, 670, 441, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1110, 730, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1430, 730, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.ChatArea = QtWidgets.QTextEdit(self.centralwidget)
        self.ChatArea.setGeometry(QtCore.QRect(1110, 80, 441, 571))
        self.ChatArea.setObjectName("ChatArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1622, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SV"))
        self.IP.setText(_translate("MainWindow", "IP-Adresse"))
        self.Name.setText(_translate("MainWindow", "Name eingeben"))
        self.Chat.setText(_translate("MainWindow", "Chat"))
        self.pushButton.setText(_translate("MainWindow", "Senden"))
        self.pushButton_2.setText(_translate("MainWindow", "Löschen"))
        
    def appendMessage(self, message):
        self.ChatArea.append(message)
        
    def setIP(self, addr):
        1+1
        #self.IP.setText(addr)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    from server import TCPconnection
    t = TCPconnection()
    t.startlistening()
    ui = Ui_MainWindow()
    ui.setIP(t.getipaddr())
    t.setWindow(ui)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
