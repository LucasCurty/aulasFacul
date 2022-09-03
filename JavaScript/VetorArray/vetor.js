

let alunos = []; //array vazio
let alunosNomes = ['Alex', 'Anna', 'Joao']; //array de strings
let notas = [10, 9.3, 6]; // array de numeros decimais
let mistura = ['um',2,'tres', 4]; // array com tipos de dados diferentes

// Outra forma de criar arrays em JS é com construtor( conceito de Programação orientada a objetos (poo))

let alunosPoo = new Array('Maria', 'Guilherme','Amanda');
console.log(alunosPoo)

// adicionando elementos ao array com metodo push
alunosPoo.push('Helena')
console.log(alunosPoo)

//apagando elemento do vetor
// delete alunosPoo[2]


//pop
// Este método, que não recebe parâmetros, remove um elemento do final do array, atualizando seu tamanho. Sua sintaxe é:

alunosPoo.pop();
console.log(alunosPoo)

// shift
// Embora similar ao pop, este método remove um elemento do início do array. Após a remoção, este é reindexado (ou seja, o elemento de índice 1 passa a ser o de índice 0 e assim sucessivamente). Além disso, o tamanho do array também é atualizado. Sua sintaxe pode ser vista a seguir:

// frutas.shift();

// splice
// Este método, introduzido anteriormente, pode ser usado para exclusão de elementos. Para tanto, ele recebe como parâmetros a quantidade de elementos que se deseja eliminar e o índice a partir do qual estes serão excluídos. A sintaxe a seguir demonstra a remoção de 2 elementos, a partir do índice 2, do array fornecido:

// var primos = [2,3,5,7,11,13,17];

// primos.splice(2,2);

// alert(primos); //imprimirá 2,3,11,13,17

// Nesse método, para fins de remoção, o primeiro parâmetro indica o índice e o segundo, a quantidade de elementos a serem excluídos.

