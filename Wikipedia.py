import wikipedia as w
import logging

class WikiFinder():
    @classmethod
    def find(cls, input):
        logging.basicConfig(level=logging.INFO, filename="mylog.log", filemode="w")
        try:
            

            logging.info('WikiFinder is done')
            return
        except Exception as e:
            logging.exception(str('The exception is in WikiFinder' + str(e)))
