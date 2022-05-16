# GitShodanKey
GitShodanKey browses public Github repositories for publicly leaked Shodan API keys in source code.
<br/>Last search 03-2022: 12 unique Shodan API keys were found within about 18 hours.

Since this is just a research project, I will not reveal any keys found! Use at your own risk!

Usage: $> gitshodankey.py \<github-api-token> <keys.out>
  
Requirement:
<br/>&nbsp;&nbsp;  GitHub API Token

Dependencies:
<br/>&nbsp;&nbsp;  python v3.9+
<br/>&nbsp;&nbsp;  pip install PyGithub
<br/>&nbsp;&nbsp;  pip install shodan
