import logging
from googlesearch import search


class GoogleFinder():
    @classmethod
    def find(cls, message_text):

        logging.basicConfig(level=logging.INFO, filename="mylog.log", filemode="w")
        try:
            output = []
            outlist = search(message_text, tld="co.in", num=9, stop=9, pause=1)
            for result in outlist:
                output.append(result)
            logging.info('The googlefinder.find is done')
            return set(output)
        except Exception as e:
            logging.exception(str('The exception is in googlefinder.find ' + str(e)))

