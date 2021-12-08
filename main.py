from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import pyrebase
from self import self

firebaseConfig = {
  "apiKey": "AIzaSyDI76VL0HV23EOWZdiyHAjcXzaeF7EW65k",
  "authDomain": "imc-calculator-4ae1c.firebaseapp.com",
  "projectId": "imc-calculator-4ae1c",
  "storageBucket": "imc-calculator-4ae1c.appspot.com",
  "messagingSenderId": "271987614320",
  "appId": "1:271987614320:web:893a8ea0c9b1d4dbee8ab5",
  "measurementId": "G-5MTXBQ9B3E",
  "databaseURL": "https://imc-calculator-4ae1c-default-rtdb.firebaseio.com/",
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.database()

janela = Tk()
janela.title('Cálculo IMC - Índice de Massa Corporal')
janela.geometry('800x300')
janela.resizable(width=0, height=0)

#### frame cima ####

frame_cima= Frame(janela, width=800, height=100)
frame_cima.grid(row=1, column=1)

### frame meio ###
frame_baixo= Frame(janela, width=800, height=150)
frame_baixo.grid(row=3, column=1)

### frame baixo ###
frame_baixo2= Frame(janela, width=800, height=50)
frame_baixo2.grid(row=5, column=1)

#### Funções ####

def calcular():

  #### Carrega Dados PAciente ####

  nome = linha_texto_nome_pac.get()

  linha_texto_nome['text'] = 'Paciente: ' + nome

  endereco = linha_texto_endec_pac.get()

  linha_texto_endereco['text'] = 'Endereço: ' + endereco

  ##### CALCULOS #####

  peso = float(e_peso.get())
  altura = float(e_altura.get())

  resultado = round(float(peso/altura**2), 2)

  if resultado < 18.5:
    linha_texto_numero['text'] ="Situação: Abaixo do peso"
    situacao = 'Abaixo do peso'

  elif resultado >= 18.5 and resultado <= 25:
    linha_texto_numero['text'] ="Situação: Normal"
    situacao = 'Normal'

  elif resultado >= 25 and resultado <= 30:
    linha_texto_numero['text'] ="Situação: Sobrepeso"
    situacao = 'Sobrepeso'

  else:
    linha_texto_numero['text'] ="Situação: Obesidade"
    situacao = 'Obesidade'

      ### Adicionando informações no Banco de Dados ###

  storage.child().push({"Nome Paciente:": nome,
                        "Endereço:": endereco,
                        "Situação Paciente:": situacao,
                        "Resultado IMC:": resultado
                        })

  linha_texto_resultado['text'] = 'Resultado IMC: ' + "{:.{}f}".format(resultado, 2)


#### Botão sair ####

def sair():
  sys.exit()
  return

#### Botão Reiniciar ####

def reiniciar():
  """Restarts the current program.
  Note: this function does not return. Any cleanup action (like
  saving data) must be done before calling this function."""
  python = sys.executable
  os.execl(python, python, *sys.argv)




### configurando o frame ###

linha_texto = Label(frame_cima, text='Nome do Paciente:')
linha_texto.place(x=10, y=30)

linha_texto_nome_pac = Entry(frame_cima, width=75)
linha_texto_nome_pac.place(x=160, y=29)

linha_texto = Label(frame_cima, text='Endereço Completo:')
linha_texto.place(x=10, y=60)

linha_texto_endec_pac = Entry(frame_cima, width=75)
linha_texto_endec_pac.place(x=160, y=58)



### Informações sobre ###

linha_texto = Label(frame_baixo, text='Altura (m Ex: 1.65):')
linha_texto.place(x=10, y=30)

e_altura = Entry(frame_baixo, width=10)
e_altura.place(x=160, y=29)

linha_texto = Label(frame_baixo, text='Peso (kg Ex: 65):')
linha_texto.place(x=10, y=60)

e_peso = Entry(frame_baixo, width=10, text='Ex: 65')
e_peso.place(x=160, y=58)

### resultado ###

linha_texto_res= Label(frame_baixo, text='RESULTADOS', height=1, pady=5)
linha_texto_res.place(x=330, y=0)

linha_texto_nome= Label(frame_baixo, text='', height=1, pady=5,justify= LEFT)
linha_texto_nome.place(x=330, y=25)

linha_texto_endereco = Label(frame_baixo, text='', height=1, pady=5,justify= LEFT, relief='flat')
linha_texto_endereco.place(x=330, y=50)

linha_texto_resultado = Label(frame_baixo, text='', height=1, pady=5,justify= LEFT, relief='flat')
linha_texto_resultado.place(x=330, y=75)

linha_texto_numero= Label(frame_baixo, text='', height=1, pady=5,justify= LEFT, relief='flat')
linha_texto_numero.place(x=330, y=100)


### botões ###

calcular = Button(frame_baixo2, command=calcular, text='Calcular', width=14, height=1, overrelief=SOLID, anchor='center')
calcular.place(x=160, y=10)

reiniciar = Button(frame_baixo2,command=reiniciar, text='Reiniciar', width=14, height=1, overrelief=SOLID, anchor='center')
reiniciar.place(x=350, y=10)

sair = Button(frame_baixo2, command=sair, text='Sair', width=14, height=1, overrelief=SOLID, anchor='center')
sair.place(x=610, y=10)




janela.mainloop()

