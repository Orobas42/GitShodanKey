# GitShodanKey

---

This tool is now somewhat outdated. There are now better and faster ways to find a published API key on Github. 
<br/>The new Github code search for example.
<br/>https://github.com/search?q=shodan_api_key%3D+remove&type=commits

---

GitShodanKey browses public Github repositories for publicly leaked Shodan API keys in source code.
<br/>Last search 03-2022: 12 unique Shodan API keys were found within about 18 hours.

Since this is just a research project, I will not reveal any keys found! Use at your own risk!

Usage: $> python3 gitshodankey.py \<github-api-token> <keys.out>
  
Requirement:
<br/>&nbsp;&nbsp;  GitHub API Token

Dependencies:
<br/>&nbsp;&nbsp;  python v3.9+
<br/>&nbsp;&nbsp;  pip3 install PyGithub
<br/>&nbsp;&nbsp;  pip3 install shodan
