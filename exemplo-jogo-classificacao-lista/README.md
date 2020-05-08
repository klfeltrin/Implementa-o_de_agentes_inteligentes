# Ordenação com mínimo esforço

## Linguagem
Estado -> Lista([x]), onde x são valores ordenáveis entre si.
Ações -> Permutar(i,j), onde i e j são índices válidos de [x].

## Problema

* Estado inicial: qualquer distribuição dos elementos em Lista([x]).
* Teste objetivo: Lista([x0,x1,x2,...,xn]) onde x0<=x1<=x2<=...<=xn.
* Ações(Lista[x]): [Permutar(I,J)], tendo I x J, ou seja, I <- [0 ... len([x]) e J <- [0 ... len([x])].
* Resultado(Lista([x1,x2,...,xi,...,xj,...,xn]), Permutar(i,j)): Lista([x1,x2,...,xj,...,xi,...,xn]).
* Custo de transição: uniforme.