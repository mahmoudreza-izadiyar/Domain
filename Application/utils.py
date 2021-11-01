import re
import sys
import os
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
NEW_LINE = '\n'
report_file = 'report.txt'
limitation_words_file = 'limited_words.txt'



def read_file(file_path):
    """Reading the context file to extract file from """
    f_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_path)
    path, file_name = os.path.split(file_path)
    # check file extend
    if not file_name.endswith('.txt'):
        logging.warning(f'{file_name}  is not a Text file, Please select a correct file.')
        sys.exit(1)
    else:
        try:
            with open(f_path, 'r') as file:
                all_words = {}
                for line in file:
                    line = line.strip()
                    line = line.lower()
                    words = re.findall(r"[\w']+", line)
                    for word in words:
                        if word in all_words:
                            all_words[word] = all_words[word] + 1
                        else:
                            all_words[word] = 1
            sorted_words = sorted(all_words.items(), key=lambda item: item[1], reverse=True)

            return sorted_words
        except FileNotFoundError:
            logging.warning(f"File {read_file} not found.  Aborting")
            sys.exit(1)
        except OSError:
            logging.warning(f"OS error occurred trying to open {read_file}")
            sys.exit(1)
        except Exception as err:
            logging.warning(f"Unexpected error opening {read_file} is", repr(err))
            sys.exit(1)  # or replace this with "raise"




def limited_words():
    """This function will remove all the words inside the Limited_words.text from the report"""
    f = open(limitation_words_file, "r")
    limited_words = []
    for line in f:
        line = line.strip()
        line = line.lower()
        words = re.findall(r"[\w']+", line)
        for word in words:
            if word not in limited_words:
                limited_words.append(word)
    return limited_words


def parse_report(minimum_count, file_path):
    """Create a report file"""
    f = open(report_file, "w")
    data = []
    limited_word = limited_words()
    words = read_file(file_path)
    for word, count in words:
        if word not in limited_word and count >= minimum_count:
            word_count = f"{word}:{count}"
            data.append(word_count)
    report_data = NEW_LINE.join(data)
    f.write(report_data)
    f.close()
    logging.info(f"report.txt file has been created.")
