from clientemodbus import ClienteInterface, ClienteMODBUS

c = ClienteMODBUS('localhost',502)
ci = ClienteInterface(c)
ci.atendimento()
