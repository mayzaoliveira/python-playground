def fizzbuzz(numero):
    retorno = ''

    if numero % 3 == 0:
        retorno += 'fizz'

    if numero % 5 == 0:
        retorno += 'buzz'

    if retorno:
        return retorno

    return numero

if __name__ == "__main__":
	print fizzbuzz(15)