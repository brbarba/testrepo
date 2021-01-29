def create_fortune_cookie_message(how_many_lucky_numbers: int) -> str:
    mensaje = generate_fortune()
    numeros = generate_lucky_numbers(how_many_lucky_numbers)
    print("\n",mensaje,"\n",numeros,"\nconcatenando")
    #full_mensaje = mensaje + numeros
    #print (full_mensaje)
    return numeros



    print("\n {} \n {} \nconcatenando".format(mensaje, numeros))
