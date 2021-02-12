import logging 

logging.basicConfig(filename='debug.log',level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s',filemode='w')


logging.debug("Je suis un debug")
logging.info("Je suis un info")
logging.warning("Je suis un warning")
logging.error("Je suis un error")
logging.critical("Je suis un critical")