# Algoritmos de Estruturas de Dados 2
*Trabalho 3º Bimestre – Indexação de arquivos grandes*


A Computação está frequentemente ligada ao processamento de
grandes volumes de dados. Os bancos de dados, um dos sistemas
mais presentes em diversas áreas, tem como uma das tarefas buscar,
inserir e editar dados de maneira rápida e uma das técnicas utilizadas
é a árvore de indexação.
Nesta abordagem, temos um arquivo principal com todos os dados
em formato de registro. Por exemplo, registros de aluno possuem
matrícula, nome, data de nascimento, curso e etc, sendo a chave de
busca o número de matrícula. Este arquivo não é ordenado. Ordená-lo
a   cada   inserção/remoção   seria   muito   trabalhoso.   Para   facilitar   a
busca, há uma árvore de indexação.
A árvore é criada com os valores chave do arquivo de registros. Em
nosso exemplo, seria uma árvore com as matrículas. Cada nodo tem
um indicador para a localização do registro (que pode ser o número
da linha para um arquivo de texto ou a posição em bytes para um
arquivo binário). Esta árvore deve ser mantida como uma árvore
binária de busca, ou seja, ordenada e balanceada.
Ao se inserir, remover ou editar o arquivo principal, tanto o arquivo
quanto o índice devem ser atualizados. Qualquer busca no arquivo
através da chave deve utilizar o índice.
Caso a árvore seja muito grande, ou seja, possua muitos nodos, não
há necessidade de se ter um nodo da árvore para cada registro do
arquivo. É possível fazer uma simplificação. Por exemplo, para o caso
do número de matrícula de 6 dígitos, poderia se fazer nodos com
apenas 3 dígitos. Dessa forma, os números 113660, 113754 e 113854
ficariam indexados pelo mesmo nodo. Este nodo não possui mais um
indicador, mas uma lista de indicadores, para cada um dos registros
do arquivo principal.
Observe que uma árvore muito pequena pode gerar listas maiores
nos nodos, o que pode tornar a busca mais lenta. Árvores maiores
tornam a busca mais rápida, mas ocupam maior espaço.
Neste trabalho você deve utilizar a base nacional de CEPS, com
endereço, rua e cidade, tendo o número do CEP como chave.

* Deves então criar rotinas de inserir, alterar, apagar e buscar
endereços.
* Cada modificação deve refletir tanto no arquivo principal quanto
na indexação.
* Deves   criar  uma   função  “terminar   programa”  que  fecha   o
programa e salva a árvore de indexação em disco.
* O número de dígitos da chave é um parâmetro do sistema. O
usuário pode escolher quantos dígitos de CEP ele irá salvar.
Deves criar uma função para mostrar a árvore de indexação.
* A árvore de indexação deverá ser uma árvore binária de busca,
como AVL ou rubro-negra.

Caso tenham interesse, pode-se propor outra base, desde que tenha
as características de chave, tamanho de arquivo e distribuição.
O trabalho poderá ser feito em duplas escolhidas por vocês. A data de
entrega será discutida em aula.
Bom trabalho!
