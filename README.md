# PD_QuestoesLeetcode


**Número da Lista**: 5  
**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01  


## Alunos


<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/Guilermanoo"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/98980548?v=4" width="190;" alt=""/><br /><sub><b>Guilherme Coelho Mendonça</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
  </tr>
</table>

| Matrícula   | Aluno                             |
| ----------- | ---------------------------------- |
| 20/2016364  | Guilherme Coelho Mendonça        |
</div>

## Sobre 
Este repositório apresenta resoluções de problemas envolvendo *Programação Dinâmica*, propostos como parte da Lista 5 da disciplina de Projeto de Algoritmos.

A plataforma [LeetCode](https://leetcode.com) foi utilizada para selecionar e resolver as questões, que possuem dificuldade média ou difícil. A resolução de cada questão está em sua pasta correspondente neste repositório; caso queira conferir o enunciado, basta clicar no link disponível na [Tabela](#exercícios-resolvidos).

As soluções apresentadas foram elaboradas focando nos conceitos explicados em sala de aula sobre programação dinâmica, como Maior Subsequência Crescente, Knapsack DP vs Greed e Programação Dinâmica com Matrizes.

**Linguagem**: Python

## Sobre LeetCode

A [LeetCode](https://leetcode.com) é uma famosa plataforma (online) utilizada por programadores que querem desenvolver suas habilidades com os mais diversos conceitos e práticas de TI.

A plataforma disponibiliza problemas classificados por dificuldade (fácil, médio e difícil), sendo utilizadas para este trabalho 2 questões médias e 1 dificil. Vale ressaltar que este repositório foi feito por um aluno, no qual não formou dupla, portanto só tem 3 questões e o aluno espera uma avaliação justa de acordo.

## Exercícios Resolvidos

| Exercício | Enunciado | Resolução | Dificuldade | Autor da Resolução |
| :--: | -- | :--: | -- | -- |
| 1 | [322. Coin Change](https://leetcode.com/problems/coin-change/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM) | [LC322.py](./Projeto/Questao_322_CoinChange.py) | Média | Guilherme Coelho Mendonça |
| 2 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM) | [LC300.py](./Projeto/Questao_300_Longest_Increasing_Subsequence.py) | Média | Guilherme Coelho Mendonça |
| 3 | [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM) | [LC10.py](./Projeto/Questao_10_Regular_Expression_Matching.py) | Difícil | Guilherme Coelho Mendonça |


## Screenshots

300. Longest Increasing Subsequence

Para resolver o exercício LeetCode 300: Longest Increasing Subsequence, utilizei uma abordagem de Programação Dinâmica. A ideia foi construir uma tabela dp, onde cada célula dp[i] guarda o comprimento da maior subsequência crescente que termina no índice i da lista nums.

Primeiro, iniciei o array dp com valor 1 para todos os índices, já que cada elemento isolado é uma subsequência crescente de comprimento 1. Em seguida, percorri a lista nums, e para cada elemento nums[i], comparei com todos os elementos anteriores nums[j] (onde j < i). Quando nums[i] > nums[j], isso indica que o elemento nums[i] pode ser adicionado à subsequência que termina em nums[j], e atualizei o valor de dp[i] com o máximo entre o valor atual de dp[i] e dp[j] + 1.

Essa comparação e atualização foram realizadas para todos os pares possíveis, o que garante que no final da iteração, o valor máximo em dp será o comprimento da maior subsequência crescente de nums.

Por fim, o resultado final é o valor máximo encontrado no array dp, que nos dá o comprimento da maior subsequência crescente em nums.

A complexidade dessa solução é O(n²), pois temos dois laços aninhados para comparar cada par de elementos na lista, onde n é o número de elementos na lista.

<p align="center">
  <img src="screenshots\3.png" alt="Print da Questão 300" width="600"/>
</p>

10. Regular Expression Matching

Para resolver o exercício LeetCode 10: Regular Expression Matching, usei uma abordagem de Programação Dinâmica. A ideia principal foi construir uma tabela de soluções parciais para verificar se a string s corresponde ao padrão p, que pode conter os caracteres especiais . e *.

Primeiro, iniciei uma tabela dp, onde cada célula dp[i][j] indica se a substring s[0..i-1] corresponde ao padrão p[0..j-1]. Inicializei a célula dp[0][0] como True, pois uma string vazia corresponde a um padrão vazio.

Durante a construção da tabela, usei duas regras importantes:

Se o caractere do padrão for um ponto (.), ele corresponde a qualquer caractere da string.

Se o caractere for um asterisco (*), ele pode indicar zero ou mais ocorrências do caractere anterior, então o padrão pode ser ignorado ou repetir o caractere anterior.

A cada iteração, comparava a substring de s com o padrão p e preenchia a tabela de acordo. No final, o valor de dp[len(s)][len(p)] indicava se a string s inteira corresponde ao padrão p.

Essa abordagem permite uma solução eficiente, evitando a repetição de cálculos para subproblemas e garantindo que a correspondência seja verificada de maneira ordenada, como um processo de comparação recursiva, mas utilizando a tabela de DP para armazenar os resultados intermediários.

A solução final tem complexidade O(m * n), onde m é o comprimento de s e n é o comprimento de p.


<p align="center">
  <img src="screenshots\10Dificil.png" alt="Print da Questão 10" width="600"/>
</p>

322. Coin Change

Para resolver o exercício LeetCode 322: Coin Change, utilizei Programação Dinâmica. A ideia foi criar um array dp, onde dp[i] representa o número mínimo de moedas necessárias para formar o valor i. Inicializei dp[0] como 0 e os outros valores como infinito.

Para cada moeda disponível, percorri todos os valores de i de coin até amount, e atualizei dp[i] com o valor mínimo entre o valor atual de dp[i] e dp[i - coin] + 1.

Ao final, dp[amount] contém o número mínimo de moedas necessárias. Se for infinito, retornamos -1, indicando que não é possível formar o valor com as moedas disponíveis.

Complexidade: O(n * amount), onde n é o número de moedas e amount é o valor alvo.

<p align="center">
  <img src="screenshots\322.png" alt="Print da Questão 320" width="600"/>
</p>

## Apresentação 

<div align="center">
<a href="linkyt"><img src="https://i.imgur.com/.png" width="50%"></a>
</div>

<font size="3"><p style="text-align: center">Autor: [Guilherme Coelho Mendonça](https://github.com/Guilermanoo).</p></font>


## Execução dos códigos na plataforma LeetCode
A maneira mais fácil de exceutar ou reproduzir os códigos e os resultados mostrados nos prints da plataforma LeetCode, é na própria plataforma. Basta acessar os links das questões acima e executar ou submeter os códigos. No entanto para isso, é preciso criar uma conta gratuita na ferramenta.

Caso não queira utilizar a plataforma LeetCode, é necessário adaptar os códigos alterando ou removendo as funções adequando ou removendo os parâmetros, bem como incluir os imports necessários.

## Disciplina
Este trabalho foi desenvolvido para a disciplina Projeto de Algoritmos, ministrada pelo Prof. Maurício, no curso de Engenharia de Software da Universidade de Brasília - Faculdade de Ciências e Tecnologias em Engenharia (UnB - FCTE).