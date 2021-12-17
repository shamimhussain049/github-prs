from github import Github

# First create a Github instance:

# access_token="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"
# using an access token
g = Github("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")

# Github Enterprise with custom hostname
# Github Enterprise with custom hostname

print(g.get_user())

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("shamimhussain049/demo-code")
issues = repo.get_pulls(state="open").get_page(0)

print(repo.get_pull(3))
# print(repo.get_pull(3).user)
# print(repo.get_pull(3).url)
# print(repo.get_pull(3).created_at)
# print(issues.__len__())
# print(issues.__getitem__(0))
#
# print(issues)
