let numeros = []
numeros[0] = fncNumero1()
numeros[1] = fncNumero2()

let result = divisao(numeros)
alert('O resultado da divisao é: ' + result)

function fncNumero1(){
  let numero1 = prompt("Insira o primeiro numero: ");
  if (numero1 <= 0 || ''){
    alert("O numero precisa ser inteiro e positivo");
    return fncNumero1();
  }else{
    return numero1
  }
}
function fncNumero2(){
  let numero2 = prompt("Insira o segundo numero: ");
  if (numero2 < 0){
    alert("O numero precisa ser inteiro e positivo");
    return fncNumero2();
  }else{
    return numero2
  }
}
function divisao(){
  let resultado = 0;
  resultado = numeros[0] / numeros[1];
  return resultado;
}