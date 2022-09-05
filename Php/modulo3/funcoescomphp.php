<?php

$num1 = 10;
$num2 = 15;

$resultado = soma($num1, $num2);

function soma($numero1, $numero2){
  return $numero1 + $numero2;
}

imprimirResultado($resultado);

function imprimirResultado($numero){
  echo "O resultado da operação é: " . $numero;
}