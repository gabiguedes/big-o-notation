def busca_binaria(A, esquerda, direita, item):
    
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    
    if A[meio] == item:
        return meio
    
    elif A[meio] > item:
        return busca_binaria(A, esquerda, meio - 1, item)
    else: 
        return busca_binaria(A, meio + 1, direita, item)

A = [20, 30, 40, 50, 60, 65, 78, 80]

print("busca_binaria com sucesso:", busca_binaria(A, 0, len(A) - 1, 65))

# O(log n) - (Logaritmo)
