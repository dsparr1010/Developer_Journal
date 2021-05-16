from django.http import HttpResponse, JsonResponse
from django.views import View
import requests
import json
import os


HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"),
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Token "+os.getenv('GH_ACCESS_TOKEN')
}


class InitialView(View):
    def get(self, request, *args, **kwargs):
        # GET REPOS FOR AUTHENTICATED USER (ME)
        # r_repos = requests.get('https://api.github.com/user/repos',params={'visibility':'all', 'sort':'created',
        #                                                             'direction':'desc', 'per_page':5, 'page':1}, headers=HEADERS)

        # GET OLLIE'S PUBLIC REPOS
        r_repos = requests.get('https://api.github.com/users/obf73/repos',
                               params={'visibility':'all', 'sort':'created',
                               'direction':'desc', 'per_page':5, 'page':1}, headers=HEADERS)
        if r_repos.status_code != 200:
            print(r_repos.status_code)
            print(r_repos.text)
        data = json.loads(r_repos.text)
        content = []
        for i in data:
            r_commits = requests.get(f'https://api.github.com/repos/obf73/{i["name"]}/commits', params={'per_page':5, 'page':1},
                                     headers=HEADERS)
            if r_commits.status_code != 200:
                print(r_commits.status_code)
                print(r_commits.text)
            data = json.loads(r_commits.text)
            # print(json.dumps(data, indent=2))
            content.append(data)
        return JsonResponse(data=content, safe=False)

