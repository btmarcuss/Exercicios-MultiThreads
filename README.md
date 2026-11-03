Exercícios:

1) Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id como parâmetro e imprima no console o texto “Thread #” + id. Antes de imprimir o valor, deve-
se fazer um sleep de 0.5 segundos.

2) Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis
inteiras para valores, crie um vetor de parâmetros, com o id como primeiro parâmetro e um
vetor com os 5 valores recebidos. As variáveis que recebem os valores devem receber, cada
uma delas, um valor aleatório de 1 a 100. Esses parâmetros devem ser preenchidos para 3
chamadas de Threads. Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread,
deve calcular a soma de cada linha (Cada iteração do laço, para a soma deve ser seguido por
um sleep de 0.2 segundos), ao final, deve-se imprimir a identificação da linha e o resultado da
soma.
3) Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1
sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância
máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o
tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para
cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu.
Assim que o sapo percorrer a distância máxima, a Thread deve apresentar que o sapo chegou.
Dica: O exercício deve ser resolvido todo em console, ou seja, como se estivesse sendo
narrado.
