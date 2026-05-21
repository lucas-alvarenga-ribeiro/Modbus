from clientemodbus import ClienteMODBUS

def main():
    cliente = ClienteMODBUS('localhost', 502)
    if cliente.connect():
        addr = 100
        val = 123.45
        
        print(f"Escrevendo float {val} no endereço {addr}...")
        cliente.escreveFloat(addr, val)
        
        lido = cliente.lerFloat(addr)
        print(f"Valor lido: {lido}")
        
        cliente.close()
    else:
        print("Sem conexão")

if __name__ == '__main__':
    main()