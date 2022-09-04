<?php 

// Comentários de uma linha
/*
  Comentários de um bloco
*/
echo "Olá, muindo!";
$var1 = 2 + 2;

echo "O Resultado da soma é igual a: " . $var1;

// Declarando variaveis
$Var01 = 10;
$var01 = 100;
$_var01 = 1;

$_nomeCurso = "Programação de Páginas Dinâmicas com PHP"; //string
$ano_criacao = 1994; //number
$flagLinguagemScript = true; // boolean

//----------------------------- VARIAVEL GET -----------------------------

// Requisção GET: /endereco_servidor/script.php?var1=value1&var2=value2&var3=value3

echo $_GET['var1']; //imprimiria value1
echo $_GET['var2']; //imprimiria value2
echo $_GET['var3']; //imprimiria value3

//----------------------------- VARIAVEL POST -----------------------------
//A exemplo de $_GET, a variável predefinida $_POST também é um array associativo. Entretanto, ela contém as variáveis recebidas através de métodos POST.

echo $_POST['var1'];
echo $_POST['var2'];
echo $_POST['var3'];

//----------------------------- VARIAVEL REQUEST -----------------------------
 
//É considerada "coringa", uma vez que exerce múltiplos papéis. Com ela, é possível receber tanto variáveis provenientes de métodos GET quanto POST – e também do método cookies ($_COOKIE).
echo $_REQUEST['var1']

