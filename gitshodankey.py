import sys

from shodan import Shodan
from github import Github


def remove_duplicates(out):
    ls = []
    with open(out, 'r+') as f:
        ls = list(dict.fromkeys(f.readlines()))

    with open(out, 'w') as f:
        for l in ls:
            f.write(l)


def test_key(k):
    try:
        shodan_api = Shodan(k)
        if shodan_api.info()['query_credits'] >= 50:
            with open(outfile, 'a+') as f:
                f.write(k + " : " + str(shodan_api.info()['query_credits']) + "\n")
    except:
        pass


def search(k, s):
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
                        test_key(split[1])

                elif s + "'" in line:
                    split = original.split("'")
                    if len(split[1]) == 32:
                        test_key(split[1])
    except Exception as e:
        print(e)


if len(sys.argv) != 3:
    print("Usage: gitshodankey.py <github-api-key> <key.out>")
    exit()

key = sys.argv[1]
outfile = sys.argv[2]
searchList = ["shodan_api_key =", "shodan_api_key=", "api_shodan_key=", "api_shodan_key =",
              "api = Shodan(", "api=Shodan(", "api = shodan.Shodan(", "api=shodan.Shodan("]

#for searchString in searchList:
#    search(key, searchString)

remove_duplicates(outfile)

