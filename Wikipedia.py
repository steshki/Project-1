import wikipedia as w
import logging
import GoogleFinder

class WikiFinder():
    @classmethod
    def find(cls, input):
        logging.basicConfig(level=logging.INFO, filename="mylog.log", filemode="w")
        try:
            gf = GoogleFinder.GoogleFinder()
            gf.find(input)
            w.set_lang("ru")
            res = w.search(input)
            logging.info('WikiFinder is done')
            return res
        except Exception as e:
            logging.exception(str('The exception is in WikiFinder' + str(e)))

if __name__ == "__main__":
#
#
    gf = WikiFinder()
    res = gf.find(input="summary")