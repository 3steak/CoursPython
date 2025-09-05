import logging

# selectionner le type de nivo a afficher
# Ecrire un fichier de log avec le format voulu
logging.basicConfig(level=logging.WARNING,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")