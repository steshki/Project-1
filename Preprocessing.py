from nltk.corpus import stopwords
from string import punctuation
import nltk
import logging


class Preprocessing():
    """
    It is a main preprocessing
    """
    @classmethod
    def preprocess_text(cls, text):
#
#
        logging.basicConfig(level=logging.INFO, filename="misa.log", filemode="w")
        try:

            logging.info('The preprocessing.preprocess_text is done')
            return text
        except Exception as e:
            logging.exception(str('The exception is in preprocessing.preprocess_text ' + str(e)))


if __name__ == "__main__":
#
#
    gf = Preprocessing()
    nltk.download('stopwords')
    res = gf.preprocess_text(text="Текст")