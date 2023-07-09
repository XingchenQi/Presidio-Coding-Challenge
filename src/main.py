"""
This module takes the user input as an argument, search the topic on internet,
return related searches and related questions with answers.

Usage example:

python3 src/main.py

output example are in image folder

"""
import subprocess
import sys
import traceback
import time
import platform
import os
import yaml
from duckpy import Client
from serpapi import GoogleSearch
import Logo as gl

# OS process
if platform.system() == 'Windows':
    subprocess.call("cls", shell=True)
else:
    subprocess.call("clear", shell=True)

UP = '\033[1A'
CLEAR = '\x1b[2K'

class QuickSearchService:
    """
    This class is used to take user input as string to extract useful internet info
    and analyze statistics

    Attributes:
        _topic     User search info

    """
    def __init__(self,topic):
        self._topic=topic

    # public
    def start_service(self):
        """
        This function is to start related services according to user input
        @return
        """
        if self._topic == ':quit':
            print(f'\t{gl.colors.RED}End of Search. Quiting......')
            sys.exit()
        elif self._topic == ':history':
            self.print_history()
            print(f'\t{gl.colors.RED}End of Search. Press any key to quit.')
            input()
            sys.exit()
        else:
            print(
                f'\t{gl.colors.FAIL}Results for: '
                f'{gl.colors.CYAN}"{self._topic}"{gl.colors.ENDC}')
            self.search_info()

            print(
                f'\t{gl.colors.FAIL}People Also Ask about: '
                f'{gl.colors.CYAN}"{self._topic}"{gl.colors.ENDC}')
            self.get_related_questions()
            self._write_history()
            print('')
            print(f'\t{gl.colors.RED}End of Search. Press any key to quit.')
            input()
            sys.exit()

    def print_history(self):  #pylint: disable=no-self-use
        """
        This function is to query search history file and print out
        @return
        """
        if not os.path.isfile('search.history'):
            print(f'{gl.colors.FAIL}No History Found.{gl.colors.ENDC}')
            input()
            sys.exit()
        try:
            with open('search.history', 'r', encoding='UTF-8') as history:
                print(f'\t{gl.colors.FAIL}Search history:\n{gl.colors.ENDC}')
                print(f'{gl.colors.CYAN}')
                index = 1
                for line in history:
                    print(f'\t{index}. {line}')
                    index += 1
                print(f'{gl.colors.ENDC}')
        except OSError:
            print(f'{gl.colors.FAIL}Get History Failed.{gl.colors.ENDC}')
            traceback.print_exc()
            input()
            sys.exit()

    def search_info(self):
        """
        This function makes an API call to Duckgogo server and print
        search results
        """
        try:
            client = Client()
            search_start = time.time()
            duck_results = client.search(self._topic)

            search_end = time.time()
            search_time = search_end - search_start
            search_time = round(search_time, 2)

            return self._print_search_info(search_time,duck_results)
        except Exception:  # pylint: disable=W0718
            print(f'{gl.colors.FAIL}No results available when searching info.{gl.colors.ENDC}')
            traceback.print_exc()
            input()
            sys.exit()

    def get_related_questions(self):
        """
        This function makes an API call to Google SerpAPI service to fetch
        related questions and answers
        """
        api_key=self._read_api_key()
        params = {
                    "q": self._topic,
                    "api_key": api_key
                }
        try:
            search = GoogleSearch(params)
            g_results = search.get_dict()
            if "error" in g_results:
                raise RuntimeError(g_results['error'])
            if "related_questions" not in g_results:
                print('')
                return print(
                            f'\t{gl.colors.FAIL}'
                            f'No related questions available when searching the info.'
                            f'{gl.colors.ENDC}')
            return self._print_related_questions(g_results["related_questions"])
        except RuntimeError as exp:
            print(f'{gl.colors.FAIL}{exp}{gl.colors.ENDC}')
            traceback.print_exc()
            input()
            sys.exit()
        except Exception:  # pylint: disable=W0718
            print(f'{gl.colors.FAIL}Failed to get related questions.{gl.colors.ENDC}')
            traceback.print_exc()
            input()
            sys.exit()

    def get_user_topic(self):
        """
        This function returns the search topic
        @return string as user search info
        """
        return self._topic

    # private
    def _print_search_info(self,search_time,duck_results):  #pylint: disable=no-self-use
        """
        This function parses the Duckgogo search engine results
        and prints the results in a standard format
        """
        print(
            f'\t{gl.colors.FAIL}About {len(duck_results)} search results in {search_time} seconds.'
            f'{gl.colors.ENDC}\n')
        results_length = len(duck_results)
        for i in range(results_length):
            result_index = i + 1
            title = duck_results[i].title
            url = duck_results[i].url
            description = duck_results[i].description
            print(
                f'{gl.colors.CYAN}  {result_index}.{gl.colors.ENDC}'
                f'\t{gl.colors.GREEN}{title}{gl.colors.ENDC}')
            print(f'\t{gl.colors.BLUE}{url}{gl.colors.ENDC}')
            print(
                f'\t{description[0:150]}{gl.colors.RED}...{gl.colors.ENDC}')
            print('')

    def _print_related_questions(self,related_questions):  #pylint: disable=no-self-use
        """
        This function analyses the google search engine related_questions results
        and prints the data in a standard format
        """
        for i,question in enumerate(related_questions):
            print('')
            print(
                f'{gl.colors.CYAN}  {i+1}.{gl.colors.ENDC}'
                f'\t{gl.colors.GREEN}{question["question"]}{gl.colors.ENDC}')
            if "snippet" in question:
                print(
                    f'\t{question["snippet"][0:150]}{gl.colors.RED}...{gl.colors.ENDC}')
            elif "title" in question:
                print(
                    f'\t{question["title"]}{gl.colors.RED}...{gl.colors.ENDC}')
            if "link" in question:
                print(f'\t{gl.colors.BLUE}{question["link"][0:150]}{gl.colors.ENDC}')

    def _write_history(self):
        """
        This function is used to write search history in file
        """
        try:
            with open('search.history', 'a', encoding='UTF-8') as history:
                history.write(f'{self._topic}\n')
        except OSError:
            print(f'{gl.colors.FAIL}Failed to write history in file.{gl.colors.ENDC}')
            traceback.print_exc()
            input()
            sys.exit()

    def _read_api_key(self):  #pylint: disable=no-self-use
        """
        This function reads yaml config file to get the API_KEY for
        Google SerpAPI service
        """
        try:
            with open('config.yml', 'r', encoding='UTF-8') as file:
                conf = yaml.safe_load(file)
            return conf['API_KEY']
        except OSError:
            print(f'{gl.colors.FAIL}Failed to get API Key.{gl.colors.ENDC}')
            traceback.print_exc()
            input()
            sys.exit()


#  Main func declaration is to avoid being executed when this module is
#  imported by another on top level
if __name__ == "__main__":
    print(gl.text)
    print(
        f'\t{gl.colors.FAIL}Type {gl.colors.CYAN}"{gl.colors.GREEN}:history{gl.colors.CYAN}"'
        f'{gl.colors.FAIL} to see your search history.{gl.colors.ENDC}\n')
    print(
        f'\t{gl.colors.FAIL}Type {gl.colors.CYAN}"{gl.colors.GREEN}:quit{gl.colors.CYAN}"'
        f'{gl.colors.FAIL} to quit qsearch.{gl.colors.ENDC}\n')
    try:
        query_search = input(f'\tQuick Search: {gl.colors.CYAN}')
        print(UP, end=CLEAR)
        quick_search=QuickSearchService(query_search)
        quick_search.start_service()
    except Exception as e:  # pylint: disable=invalid-name W0718
        print(f'{gl.colors.FAIL}Quick Search starting failed.{gl.colors.ENDC}')
        traceback.print_exc()
        garbage = input()
        sys.exit()
