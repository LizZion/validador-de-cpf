import string

def limpar_cpf(cpf):
    pontos = string.punctuation
    traços = "-"
    for p in pontos:
        cpf = cpf.replace(p, "")
    for t in traços:
        cpf = cpf.replace(t, "")
    return cpf

def obter_digitos_verificadores(cpf_cortado):
    cpf_validador = 0
    contador = 2
    for i in reversed(cpf_cortado):
        cpf_validador += int(i) * contador
        contador += 1
    cpf_validador %= 11
    if cpf_validador < 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - cpf_validador
    return str(digito_verificador)

def validar_cpf(cpf):
    cpf_limpo = limpar_cpf(cpf)
    cpf_cortado = list(cpf_limpo[:9])
    digito_verificador1 = obter_digitos_verificadores(cpf_cortado)
    cpf_cortado.append(digito_verificador1)
    digito_verificador2 = obter_digitos_verificadores(cpf_cortado)
    cpf_cortado.append(digito_verificador2)
    return cpf_limpo == "".join(cpf_cortado)

cpf_inserido = input("Insira o CPF para validar: ")
valido = validar_cpf(cpf_inserido)
print(valido)