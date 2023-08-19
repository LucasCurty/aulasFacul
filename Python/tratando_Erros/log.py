import logging
#Definindo o formato da mensagem
LOG_FORMAT = "%(levelname)s - %(asctime)s - %(message)s"

#configurando o baisco para o arqvuivo log, passando o nome do arquivo, o tipo de prioridade de captura e o formato definido acima
logging.basicConfig(filename="logs.log", level=logging.DEBUG, format=LOG_FORMAT)
#criando a capturação dos eventos logs
log = logging.getLogger()

#Chamando o evento log passando seus tipos.
log.info("Starting")
log.critical("Erro critico")
log.error("Holve um erro")
log.debug("Erro Grave!")
log.warning("Erro Muito Grave!  ")
#printando o tipo do level definido no log por padr]ao ele vem 30 = WARNING
print(log.level)