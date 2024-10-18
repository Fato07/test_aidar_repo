import subprocess

def get_commits_by_aider():
    """
    Get all commits made by 'aider'.
    """
    result = subprocess.run(
        ["git", "log", "--pretty=format:%H %an %ae"],
        stdout=subprocess.PIPE,
        text=True
    )
    commits = result.stdout.splitlines()
    aider_commits = [commit.split()[0] for commit in commits if "aider" in commit]
    return aider_commits

def change_commit_author(commit_hash):
    """
    Change the author and committer of a specific commit.
    """
    subprocess.run(
        ["git", "filter-branch", "-f", "--env-filter",
         f'if [ "$GIT_COMMIT" = "{commit_hash}" ]; then '
         f'export GIT_AUTHOR_NAME="Sha256_Nulled"; '
         f'export GIT_AUTHOR_EMAIL="Fathindos.FD@gmail.com"; '
         f'export GIT_COMMITTER_NAME="Sha256_Nulled"; '
         f'export GIT_COMMITTER_EMAIL="Fathindos.FD@gmail.com"; '
         'fi',
         "HEAD"]
    )

def main():
    aider_commits = get_commits_by_aider()
    for commit_hash in aider_commits:
        print(f"Changing author of commit {commit_hash}...")
        change_commit_author(commit_hash)
    print("All specified commits have been updated.")

if __name__ == "__main__":
    main()

