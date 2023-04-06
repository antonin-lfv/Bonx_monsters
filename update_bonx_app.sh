# 'git fetch' to get the latest version of the repository
git fetch

# Compare the local branch with the remote branch
DIFF_OUTPUT="$(git diff HEAD @{u})"

# Show the result of the comparison
if [ -z "$DIFF_OUTPUT" ]; then
    echo "No update available"
else
    git pull
    echo "Update done successfully !"
fi
