import speech_recognition as sr
import pyttsx3
import random
import re
import unicodedata


# ============================================================
# CONFIGURAÇÃO DO JARVIS
# ============================================================

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def falar(texto):
    """Faz o Jarvis falar."""
    print(f"\n🤖 Jarvis: {texto}")
    engine.say(texto)
    engine.runAndWait()


# ============================================================
# RECONHECIMENTO DE VOZ
# ============================================================

reconhecedor = sr.Recognizer()


def ouvir():
    """
    Escuta o aluno pelo microfone e transforma a fala em texto.
    """

    with sr.Microphone() as source:

        print("\n🎤 Estou ouvindo...")
        reconhecedor.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = reconhecedor.listen(
                source,
                timeout=8,
                phrase_time_limit=10
            )

            texto = reconhecedor.recognize_google(
                audio,
                language="pt-BR"
            )

            print(f"👨‍🎓 Aluno: {texto}")

            return texto.lower()

        except sr.WaitTimeoutError:
            print("⏱️ Nenhuma fala detectada.")
            return ""

        except sr.UnknownValueError:
            print("❓ Não consegui entender.")
            return ""

        except sr.RequestError:
            print("🌐 Erro no serviço de reconhecimento de voz.")
            return ""


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def remover_acentos(texto):
    """
    Remove acentos para facilitar a comparação das respostas.
    """

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def normalizar(texto):
    """
    Deixa o texto mais fácil de interpretar.
    """

    texto = remover_acentos(texto.lower())

    texto = re.sub(r"[^\w\s]", " ", texto)

    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


def contem_palavra(texto, palavras):
    """
    Verifica se pelo menos uma palavra-chave aparece na resposta.
    """

    texto = normalizar(texto)

    for palavra in palavras:

        palavra = normalizar(palavra)

        if palavra in texto:
            return True

    return False


# ============================================================
# SISTEMA DE PONTUAÇÃO
# ============================================================

pontuacao = 0

resultado_pilares = {
    "Decomposição": 0,
    "Reconhecimento de Padrões": 0,
    "Abstração": 0,
    "Algoritmos": 0
}


def acertou(pilar):
    global pontuacao

    pontuacao += 1
    resultado_pilares[pilar] += 1

    falar(
        "Muito bem! Resposta correta. "
        "Você está pensando como um programador."
    )


def errou(mensagem):
    falar(mensagem)


# ============================================================
# DESAFIO 1
# DECOMPOSIÇÃO
# ============================================================

def desafio_decomposicao_1():

    pilar = "Decomposição"

    falar(
        "Primeiro desafio de decomposição."
    )

    falar(
        "Você precisa preparar um robô para entregar "
        "um objeto em outra sala."
    )

    falar(
        "Quais tarefas precisamos realizar? "
        "Você pode dizer coisas como pegar o objeto, "
        "encontrar o caminho e entregar o objeto."
    )

    resposta = ouvir()

    palavras = [
        "pegar",
        "objeto",
        "caminho",
        "entregar",
        "sala"
    ]

    if sum(1 for palavra in palavras if palavra in normalizar(resposta)) >= 2:

        acertou(pilar)

    else:

        errou(
            "Quase! Pense nas pequenas tarefas necessárias "
            "para realizar a missão."
        )


# ============================================================
# DESAFIO 2
# DECOMPOSIÇÃO
# ============================================================

def desafio_decomposicao_2():

    pilar = "Decomposição"

    falar(
        "Segundo desafio de decomposição."
    )

    falar(
        "Você precisa fazer um sanduíche."
    )

    falar(
        "Em vez de pensar no sanduíche inteiro, "
        "quais pequenas tarefas podemos realizar?"
    )

    resposta = ouvir()

    palavras = [
        "pegar pão",
        "pao",
        "colocar",
        "ingrediente",
        "montar",
        "abrir",
        "fechar"
    ]

    quantidade = sum(
        1
        for palavra in palavras
        if palavra in normalizar(resposta)
    )

    if quantidade >= 2:

        acertou(pilar)

    else:

        errou(
            "Tente dividir a tarefa em pequenas partes, "
            "como pegar os ingredientes e montar o sanduíche."
        )


# ============================================================
# DESAFIO 3
# DECOMPOSIÇÃO
# ============================================================

def desafio_decomposicao_3():

    pilar = "Decomposição"

    falar(
        "Terceiro desafio de decomposição."
    )

    falar(
        "Um robô precisa limpar uma sala."
    )

    falar(
        "Quais pequenas tarefas podem fazer parte dessa missão?"
    )

    resposta = ouvir()

    palavras = [
        "pegar lixo",
        "lixo",
        "varrer",
        "limpar",
        "organizar",
        "guardar",
        "mesa",
        "cadeira"
    ]

    quantidade = sum(
        1
        for palavra in palavras
        if palavra in normalizar(resposta)
    )

    if quantidade >= 2:

        acertou(pilar)

    else:

        errou(
            "Muito bem por tentar. Pense em várias tarefas menores "
            "que juntas realizam a limpeza."
        )


# ============================================================
# DESAFIO 4
# RECONHECIMENTO DE PADRÕES
# ============================================================

def desafio_padroes_1():

    pilar = "Reconhecimento de Padrões"

    falar(
        "Agora vamos procurar padrões."
    )

    falar(
        "Observe esta sequência: dois, quatro, seis, oito."
    )

    falar(
        "Qual é o próximo número?"
    )

    resposta = ouvir()

    if "dez" in normalizar(resposta) or "10" in resposta:

        acertou(pilar)

    else:

        errou(
            "Observe novamente. Os números estão aumentando "
            "de dois em dois."
        )


# ============================================================
# DESAFIO 5
# PADRÕES
# ============================================================

def desafio_padroes_2():

    pilar = "Reconhecimento de Padrões"

    falar(
        "Segundo desafio."
    )

    falar(
        "Imagine uma sequência de cores: "
        "vermelho, azul, vermelho, azul, vermelho."
    )

    falar(
        "Qual cor aparece depois?"
    )

    resposta = ouvir()

    if "azul" in normalizar(resposta):

        acertou(pilar)

    else:

        errou(
            "Observe o que está se repetindo: "
            "vermelho, azul, vermelho, azul."
        )


# ============================================================
# DESAFIO 6
# PADRÕES
# ============================================================

def desafio_padroes_3():

    pilar = "Reconhecimento de Padrões"

    falar(
        "Terceiro desafio."
    )

    falar(
        "Um robô faz a sequência: "
        "andar, pular, andar, pular, andar."
    )

    falar(
        "Qual será a próxima ação?"
    )

    resposta = ouvir()

    if "pular" in normalizar(resposta):

        acertou(pilar)

    else:

        errou(
            "Procure a ação que está se repetindo "
            "depois de andar."
        )


# ============================================================
# DESAFIO 7
# ABSTRAÇÃO
# ============================================================

def desafio_abstracao_1():

    pilar = "Abstração"

    falar(
        "Agora vamos aprender sobre abstração."
    )

    falar(
        "Imagine que um robô precisa encontrar a biblioteca."
    )

    falar(
        "A escola possui alunos, professores, paredes, "
        "janelas, salas e portas."
    )

    falar(
        "Qual informação é importante para o robô?"
    )

    resposta = ouvir()

    resposta = normalizar(resposta)

    palavras = [
        "sala",
        "caminho",
        "biblioteca",
        "porta",
        "localizacao",
        "local"
    ]

    if any(palavra in resposta for palavra in palavras):

        acertou(pilar)

    else:

        errou(
            "Pense apenas nas informações que ajudam "
            "o robô a encontrar a biblioteca."
        )


# ============================================================
# DESAFIO 8
# ABSTRAÇÃO
# ============================================================

def desafio_abstracao_2():

    pilar = "Abstração"

    falar(
        "Segundo desafio de abstração."
    )

    falar(
        "Um robô precisa encontrar uma bola azul."
    )

    falar(
        "Precisamos saber a cor da parede da sala?"
    )

    resposta = ouvir()

    resposta = normalizar(resposta)

    if "nao" in resposta or "não" in resposta:

        acertou(pilar)

    else:

        errou(
            "A cor da parede não ajuda o robô a encontrar "
            "a bola. Essa informação pode ser ignorada."
        )


# ============================================================
# DESAFIO 9
# ABSTRAÇÃO
# ============================================================

def desafio_abstracao_3():

    pilar = "Abstração"

    falar(
        "Terceiro desafio."
    )

    falar(
        "Um aplicativo precisa encontrar uma pessoa "
        "pelo nome."
    )

    falar(
        "Qual informação é mais importante: "
        "o nome da pessoa ou a cor da roupa dela?"
    )

    resposta = ouvir()

    resposta = normalizar(resposta)

    if "nome" in resposta:

        acertou(pilar)

    else:

        errou(
            "Pense em qual informação o aplicativo "
            "realmente precisa para encontrar a pessoa."
        )


# ============================================================
# DESAFIO 10
# ALGORITMOS
# ============================================================

def desafio_algoritmo_1():

    pilar = "Algoritmos"

    falar(
        "Agora você será o programador."
    )

    falar(
        "Precisamos ensinar um robô a escovar os dentes."
    )

    falar(
        "As ações são: pegar a escova, "
        "colocar pasta, escovar os dentes e guardar a escova."
    )

    falar(
        "Diga a ordem correta."
    )

    resposta = normalizar(ouvir())

    ordem = [
        "pegar",
        "pasta",
        "escovar",
        "guardar"
    ]

    posicoes = []

    for palavra in ordem:

        posicao = resposta.find(palavra)

        if posicao != -1:
            posicoes.append(posicao)

    if len(posicoes) == 4 and posicoes == sorted(posicoes):

        acertou(pilar)

    else:

        errou(
            "Quase! Primeiro precisamos pegar a escova, "
            "depois colocar a pasta, escovar os dentes "
            "e finalmente guardar a escova."
        )


# ============================================================
# DESAFIO 11
# ALGORITMOS
# ============================================================

def desafio_algoritmo_2():

    pilar = "Algoritmos"

    falar(
        "Segundo desafio de algoritmos."
    )

    falar(
        "Um robô precisa beber água."
    )

    falar(
        "Qual sequência faz mais sentido?"
    )

    falar(
        "Pegar o copo, colocar água, beber e guardar o copo."
    )

    falar(
        "Agora diga a sequência usando os números "
        "um, dois, três e quatro."
    )

    resposta = normalizar(ouvir())

    resposta = resposta.replace("um", "1")
    resposta = resposta.replace("dois", "2")
    resposta = resposta.replace("tres", "3")
    resposta = resposta.replace("quatro", "4")

    numeros = re.findall(r"[1-4]", resposta)

    if numeros[:4] == ["1", "2", "3", "4"]:

        acertou(pilar)

    else:

        errou(
            "A sequência correta é: "
            "pegar o copo, colocar água, beber e guardar o copo."
        )


# ============================================================
# DESAFIO 12
# ALGORITMOS
# ============================================================

def desafio_algoritmo_3():

    pilar = "Algoritmos"

    falar(
        "Último desafio!"
    )

    falar(
        "Você precisa ensinar um robô a atravessar "
        "uma sala até chegar à porta."
    )

    falar(
        "O robô deve primeiro levantar, "
        "depois andar até a porta e finalmente abrir a porta."
    )

    falar(
        "Diga quais são as três ações na ordem correta."
    )

    resposta = normalizar(ouvir())

    palavras = [
        "levantar",
        "andar",
        "abrir"
    ]

    posicoes = []

    for palavra in palavras:

        posicao = resposta.find(palavra)

        if posicao != -1:
            posicoes.append(posicao)

    if len(posicoes) == 3 and posicoes == sorted(posicoes):

        acertou(pilar)

    else:

        errou(
            "Pense na sequência: "
            "levantar, andar até a porta e abrir a porta."
        )


# ============================================================
# EXECUÇÃO DOS DESAFIOS
# ============================================================

desafios = [

    ("Decomposição", desafio_decomposicao_1),
    ("Decomposição", desafio_decomposicao_2),
    ("Decomposição", desafio_decomposicao_3),

    ("Reconhecimento de Padrões", desafio_padroes_1),
    ("Reconhecimento de Padrões", desafio_padroes_2),
    ("Reconhecimento de Padrões", desafio_padroes_3),

    ("Abstração", desafio_abstracao_1),
    ("Abstração", desafio_abstracao_2),
    ("Abstração", desafio_abstracao_3),

    ("Algoritmos", desafio_algoritmo_1),
    ("Algoritmos", desafio_algoritmo_2),
    ("Algoritmos", desafio_algoritmo_3)
]


# ============================================================
# INÍCIO DO JOGO
# ============================================================

def iniciar():

    global pontuacao

    pontuacao = 0

    for pilar in resultado_pilares:
        resultado_pilares[pilar] = 0

    falar(
        "Olá! Eu sou o Mini Jarvis."
    )

    falar(
        "Hoje você terá uma missão especial."
    )

    falar(
        "Você será o programador e deverá ensinar "
        "um robô a resolver diferentes problemas."
    )

    falar(
        "Teremos quatro tipos de desafios."
    )

    falar(
        "Preparado?"
    )

    input("\nPressione ENTER para começar...")

    random.shuffle(desafios)

    for numero, (pilar, desafio) in enumerate(desafios, start=1):

        print("\n" + "=" * 60)
        print(f"DESAFIO {numero} DE 12")
        print("=" * 60)

        desafio()

        input("\nPressione ENTER para continuar...")

    finalizar()


# ============================================================
# RESULTADO FINAL
# ============================================================

def finalizar():

    print("\n")
    print("=" * 60)
    print("🏆 MISSÃO CONCLUÍDA")
    print("=" * 60)

    print(f"\nPontuação final: {pontuacao}/12")

    falar(
        f"Missão concluída! "
        f"Você conseguiu {pontuacao} pontos de 12."
    )

    print("\n📊 Desempenho por habilidade:\n")

    for pilar, pontos in resultado_pilares.items():

        print(
            f"{pilar}: {pontos}/3"
        )

    falar(
        "Agora vamos descobrir quais habilidades "
        "de pensamento computacional você utilizou."
    )

    falar(
        "Você trabalhou com decomposição, "
        "reconhecimento de padrões, abstração e algoritmos."
    )

    falar(
        "Parabéns, programador!"
    )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    try:

        iniciar()

    except KeyboardInterrupt:

        print("\n\nPrograma encerrado pelo usuário.")

    except Exception as erro:

        print("\n❌ Ocorreu um erro:")
        print(erro)