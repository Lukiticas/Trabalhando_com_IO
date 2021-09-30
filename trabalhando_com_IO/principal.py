import contatos_uteis

try:
    #contatos = contatos_uteis.csv_para_contatos('trabalhando_com_IO\dados\contatos.csv', 'latin_1')
    #contatos_uteis.contatos_para_pickle(contatos, 'trabalhando_com_IO\dados\contatos.pickle')
    #contatos = contatos_uteis.pickle_para_contatos('trabalhando_com_IO\dados\contatos.pickle')
    #contatos_uteis.contatos_para_json(contatos, 'trabalhando_com_IO\dados\contatos.json')

    contatos = contatos_uteis.json_para_contatos('trabalhando_com_IO\dados\contatos.json')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print("NÃO EXISTE ESSE ARQUIVO")
except PermissionError:
    print("NÃO TENHO PERMISSÃO PARA EDITAR ESSE ARQUIVO") 
