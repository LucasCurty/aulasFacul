<?php


// ---------- OPERADOES  DE ATRIBUIÇÃO ----------
$var1 = 4; //a variável foi inicializada com o valor de 4
$var1 += 2; //com a utilização da combinação de operadores a variável $var1 passou a ter o valor de 6 (4 + 2)
$var1 *= 2; //com a utilização da combinação de operadores a variável $var1 passou a ter o valor de 12 (4 + 2) * 2

$var2 = "Programação";
$var2 .= " com PHP"; //com a utilização da combinação de operadores a variável $var2 passou a ter o conteúdo "Programação com PHP"

$var3 = ($var4 = "Copie esses códigos") . " e pratique seus conhecimentos!" ;
/*
No exemplo acima o conteúdo da variável $var3 é igual a "Copie esses códigos e pratique seus conhecimentos!"
Já a variável $var4 possui o conteúdo "Copie esses códigos"
*/

// ---------- OPERADOES  DE COMPARAÇÃO ----------
  // São utilizados para comparar dois valores. A tabela 2 apresenta os operadores disponíveis e suas funções:
	$var1 == $var2	//Verifica se $var1 é igual a $var2
	$var1 === $var2	//Verifica se $var1 é idêntica a $var2. Nesse caso, além do valor, verifica se ambas são do mesmo tipo
	$var1 != $var2	//Verifica se $var1 é diferente de $var2
	$var1 <> $var2  //Tbm Verifica se $var1 é diferente de $var2 
	$var1 !== $var2	//Verifica se não são idênticas/iguais ou se não são do mesmo tipo
	$var1 < $var2	  //Verifica se $var1 é menor que $var2
	$var1 > $var2   //Verifica se $var1 é maior que $var2
	$var1 <= $var2	//Verifica se $var1 é menor ou igual a $var2
	$var1 >= $var2	//Verifica se $var1 é maior ou igual a $var2

  //A partir da versão 7 do PHP, um novo operador foi incluído, o “spaceship”, cuja forma de utilização é “$var1<=> $var2”. Ele retorna -1, 0 ou 1 quando $var1 for, respectivamente, menor, igual ou maior que $var2.

// ---------- OPERADOES  DE COMPARAÇÃO ----------
  //São usados para combinar expressões lógicas. A tabela 3 mostra os operadores lógicos disponíveis em PHP:
$var1 and $var2	// Retorna true se $var1 E $var2 forem verdadeiras
$var1 or $var2	// Retorna true se $var1 OU $var2 forem verdadeiras
$var1 xor $var2	// Retorna true se $var1 OU $var2 forem verdadeiras, mas não ambas
!$var1	        // Retorna true se $var1 não for verdadeira
$var1 && $var2	// Retorna true se $var1 E $var2 forem verdadeiras
$var1 || $var2	// Retorna true se $var1 OU $var2 forem verdadeiras


// Caso o arquivo só contenha codigo php, nao sera preciso fechar a tag, logo, se tiver codigo html ele precisará.
?>
