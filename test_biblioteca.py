from biblioteca import LIVROS

def test_adicionar_livro():
    
    #LIMPAR A LISTA ANTES DE TESTAR
    
    LIVROS.clear()  

    #ADICIONAR O LIVRO

    livro_novo = "amor"
    if livro_novo not in LIVROS:
        LIVROS.append(livro_novo)
    
    #VERIFICAR SE FOI ADICIONADO

    assert "amor" in LIVROS
