// condiçoes com Switch
let numero = -1;

switch(numero){
  case (numero < 0) :
    console.log('numero negativo');
  break;

  case numero == 0 :
    console.log('zero');
  break;

  case numero > 0 :
    console.log('numero positivo');
  break;

  default:
    console.log("qual o numero?");
  break;
}
