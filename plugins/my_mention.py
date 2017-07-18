# -*- coding: utf-8 -*-

from github import Github
from slackbot.bot import respond_to
from slackbot_settings import GITHUB_TOKEN


@respond_to(r'^[a-zA-Z-]+#\d+$')
def github_func(message):
    g = Github(login_or_token=GITHUB_TOKEN)

    text = message.body['text']
    t = text.split('#')
    input_repo = t[0]
    issue_id = int(t[1])

    all_repo_names = ''
    is_found = False
    for repo in g.get_user().get_repos():
        all_repo_names += repo.name + '\n'
        if repo.name == input_repo:
            is_found = True
            try:
                issue = repo.get_issue(issue_id)
                title = issue.title
                body = issue.body
                link = 'https://github.com/sitateru/' + repo.name + '/' + t[1]

                msg = u'repo: {}\n'.format(repo.name)
                msg += u'title: {}\n'.format(title)
                msg += u'body: {}\n'.format(body)
                msg += u'link: {}\n'.format(link)
            except:
                msg = u'issueが見つかりませんでした。id:{}'.format(issue_id)
    if not is_found:
        msg = u'以下の中から選んでください。\n {}'.format(all_repo_names)

    message.reply(msg)
