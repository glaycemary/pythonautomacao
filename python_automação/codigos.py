##### Passo a passo do projeto

# importar ferramentas - biblioteca de códigos
import pyautogui


# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela      
# pyautogui.hotkey -> combinação de teclas (ex: ctrl,c)

#adicionar tempo para passar etapas no navegador
pyautogui.PAUSE = 0.5
import time

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")

# Quero dar uma pausa tempo/segundos para esperar a página carregar
time.sleep(1)

# entrar no link
pyautogui.click(x=435, y=62) 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=714, y=402)

# escrever o seu email
pyautogui.write("glaycemary84ti@gmail.com")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.press("tab")

# Passo 3: Importar a base de produtos pra cadastrar
# instalar - pip install pandas - no terminal
import pandas 


# base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar 01 produto
 # pegar da tabela o valor do campo que a gente quer preencher

linha = 0

time.sleep(1)

# para cada linha da tabela fazer um loop (for)

for linha in tabela.index:
    # clicar no campo de código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca do Produto 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo do Produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # Categoria do Produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço Unitário do Produto
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # Custo do Produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # OBS
    #nan = not a Number = vazio
    obs = tabela.loc[linha, "obs"]
    # if condicao:
        # o que que fazer se a condicao for verdadeira
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")



    # cadastra o produto (botao enviar)
    pyautogui.press("enter")

    # dar scroll de tudo pra cima
    pyautogui.scroll(10000)



    
# Passo 5: Repetir o processo de cadastro até o fim
