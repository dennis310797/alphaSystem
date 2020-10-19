from PyQt5 import uic, QtWidgets
class Adicionar:
    def __init__ (self, modelo, ducha, completa, secar, cera, aspirar, alugar):
        self.modelo=modelo 
        self.ducha=ducha
        self.completa=completa
        self.aspirar=aspirar
        self.alugar=alugar
        self.cera=cera
        self.secar=secar
        
        self.pc_ducha=0
        self.pc_completa=0
        self.pc_alugar=0
        self.pc_aspirar=0
        self.pc_secar=0
        self.pc_cera=0
        
        '''self.pc_ducha=self.receber_valor_ducha()
        self.pc_completa=self.receber_valor_completa()
        self.pc_alugar=self.receber_valor_alugar()
        self.pc_aspirar=self.receber_valor_aspirar()
        self.pc_secar=self.receber_valor_secar()
        self.pc_cera=0'''
        
        self.preco_servico=0
    def receber_valor_ducha(self):
        if self.ducha == True:    
            if self.modelo == 1:
                self.pc_ducha = 12
            elif self.modelo == 2:
                self.pc_ducha = 20
            elif self.modelo == 3:
                self.pc_ducha = 30
            elif self.modelo == 4:
                self.pc_ducha=0
        
        return self.pc_ducha
     
    def receber_valor_completa(self):
        if self.completa == True:
            if self.modelo == 1:
                self.pc_completa = 40
            elif self.modelo == 2:
                self.pc_completa = 50
            elif self.modelo == 3:
                self.pc_completa = 60
            elif self.modelo == 4:
                self.pc_completa = 20
        return self.pc_completa
    
    def receber_valor_alugar(self):
        if self.alugar==True:
            if self.modelo == 4:
                self.pc_alugar = 0
            else:
                self.pc_alugar = 7
        return self.pc_alugar
    
    def receber_valor_aspirar(self):
        if self.aspirar==True:
            if self.modelo == 4:
                self.pc_aspirar = 0
            else:
                self.pc_aspirar = 15
        return self.pc_aspirar
    
    def receber_valor_secar(self):
        if self.secar==True:
            if self.modelo == 4:
                self.pc_secar = 0
            else:
                self.pc_secar = 5
        return self.pc_secar 
      
    def receber_valor_cera(self):
        if self.cera==True:
            if self.modelo == 4:
                self.pc_cera = 0
            elif self.modelo == 2:
                self.pc_cera = 10
            else:
                self.pc_cera=5
        return self.pc_cera
    
    def calcular_servicos (self):
        self.preco_servico=self.pc_ducha+self.pc_completa+self.pc_secar+self.pc_cera+self.pc_alugar+self.pc_aspirar
        return self.preco_servico
         
def inserir_carro():
    carro_lido = alpha.le_modelo.text()
    radio_button=0
    ducha=False
    completa=False
    aspirar=False
    alugar=False
    cera=False
    secar=False
    
    if alpha.rb_carro.isChecked():
        radio_button = 1
        
    elif alpha.rb_camionete.isChecked():
        radio_button = 2
        
    elif alpha.rb_utilitario.isChecked():
        radio_button = 3
        
    elif alpha.rb_moto.isChecked():
        radio_button = 4
        
    else:
#inserir mensagem de erro <<<<<<<<<<<<<<<<<<<
        print("Nada Selecionado")
        
    if alpha.ck_ducha.isChecked()==True:
        ducha=True  
    elif alpha.ck_completa.isChecked()==True:
        completa=True
    elif alpha.ck_aspirar.isChecked()==True:
        aspirar=True
    elif alpha.ck_alugar.isChecked()==True:
        alugar=True
    elif alpha.ck_cera.isChecked()==True:
        cera=True
    elif alpha.ck_secar.isChecked()==True:
        secar=True
    
    obj=Adicionar(radio_button, ducha, completa, secar, cera, aspirar, alugar)

    preco=obj.receber_valor_ducha()+obj.receber_valor_secar()
    #preco=Adicionar.calcular_servicos()

    print(preco)
    print(carro_lido)
    print(radio_button)
        

#INICIO DO PROGRAMA
if __name__ == "__main__":
    pass
    app=QtWidgets.QApplication([])
    alpha=uic.loadUi("main.ui")

    #AÇÃO EXECUTADA QUANDO APERTA O BOTÃO DE INSERIR
    alpha.btn_inserir.clicked.connect(inserir_carro)

    alpha.show()
    app.exec()