# GitShodanKey
GitShodanKey browses public Github repositories for publicly leaked Shodan API keys in source code.
<br/>Last search 02-2023: 6 unique Shodan API keys were found within about 12 hours.

Since this is just a research project, I will not reveal any keys found! Use at your own risk!

Usage: `$python3 gitshodankey.py \<github-api-token> <keys.out>`
<br>Example: `python3 gitshodankey.py ghp_...GKu keys`

Requirements:
<br/>&nbsp;&nbsp;  GitHub API Token
<br/>&nbsp;&nbsp;  python v3.9+

for generating GitHub API token go to this [link](https://github.com/settings/tokens) 

Dependencies:
`pip install -r requirements.txt`
