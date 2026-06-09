def calcular_percentual(respostas):

    media = sum(respostas) / len(respostas)

    percentual = ((media - 1) / 6) * 100

    return round(percentual, 2)


def classificar(valor):

    if valor <= 20:
        return "Muito Baixo"

    elif valor <= 40:
        return "Baixo"

    elif valor <= 60:
        return "Moderado"

    elif valor <= 80:
        return "Elevado"

    return "Muito Elevado"