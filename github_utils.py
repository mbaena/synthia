import os
from github import Github
import git
from config import GITHUB_ACCESS_TOKEN

def get_github_repo(repo_name):
    github = Github(GITHUB_ACCESS_TOKEN)
    return github.get_repo(repo_name)

def create_branch(repo, branch_name):
    git_repo = git.Repo.clone_from(repo.clone_url, os.path.join(".", branch_name))
    git_repo.git.checkout("-b", branch_name)
    return git_repo

def commit_and_push_changes(git_repo, branch_name, commit_message):
    git_repo.git.add("--all")
    git_repo.git.commit("-m", commit_message)
    git_repo.git.push("--set-upstream", "origin", branch_name)

def create_pull_request(repo, branch_name, title, body):
    base = "main"  # Asegúrese de que esta sea la rama principal de su repositorio
    head = branch_name
    return repo.create_pull(title=title, body=body, base=base, head=head)

def is_pull_request_merged(repo, pull_request):
    pr = repo.get_pull(pull_request.number)
    return pr.merged

def get_pull_request_comments(repo, pull_request):
    pr = repo.get_pull(pull_request.number)
    return [comment.body for comment in pr.get_review_comments()]
