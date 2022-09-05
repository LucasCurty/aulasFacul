<?php

$var1 = 5;
$var2 = '5';
if($var1 == $var2){
  echo "$var1 é igual a $var2";
}else{
  echo "$var1 Nao é igual a $var2";
}

// Forma alternativa

if($var1 == $var2):
  echo "\n\Forma alternativa \n\n";
  echo "$var1 NÃO é igual a $var2";
else:
  echo "$var1 Não é igual a $var2";
endif;

//switch

$fruta = 'laranja';
switch($fruta){
  case 'laranja':
    echo "Faça uma Laranjada";
    break;
  case 'limao':
    echo "Faça uma Limonada";
    break; 
  case 'caja':
    echo "Faça uma Cajadada";
    break;
  case 'abacate':
    echo "Faça uma Abacatada";
    break;
  default:
    echo "Fruta indefinida";
    break;
}

// while
$a = 1;
 while ($a <= 10) {
    echo "Imprimindo while";
    echo "Valor de a: $a";
    $a++;
 }

 //do-while
 $i = 1;
 do{
    echo "Impimindo o do-while";
    echo "Valor de i: $i";
    $i++;
 }while($i <= 5);

 die;

 //for com array
$arrayFrutas = Array("Laranja", "Maça", "Uva");

 for($f = 0; $f<count($arrayFrutas); $f++){
  echo "Fruta: " . $arrayFrutas[$f];
 }

 //foreach com array
 foreach($arrayFrutas as $fruta){
  echo "Fruta: " . $fruta;
 }
