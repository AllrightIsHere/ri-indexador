from index.indexer import *
from index.structure import *

if __name__ == "__main__":
    htmlIndexer = HTMLIndexer(FileIndex())
    htmlIndexer.cleaner = Cleaner(stop_words_file="stopwords.txt",
                                  language="portuguese",
                                  perform_stop_words_removal=True,
                                  perform_accents_removal=True,
                                  perform_stemming=False)

    htmlIndexer.index_text_dir("ri-tp-wiki-data")
    htmlIndexer.index.write("wiki.idx")
