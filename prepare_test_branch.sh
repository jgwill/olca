#!/usr/bin/env bash

REPO_URL="git@github.com:jgwill/olca.git"
BRANCH="20-add-persistent-session-memory"
DIR_NAME="olca"

echo "🚀 Setting up OLCA with persistent session memory"
echo "Repository: $REPO_URL"
echo "Branch: $BRANCH"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check if directory already exists
if [ -d "$DIR_NAME" ]; then
    echo "📂 Directory $DIR_NAME already exists"
    echo "⏳ Updating repository..."
    cd $DIR_NAME
    git fetch
    git checkout $BRANCH
    git pull
    echo "✅ Updated and checked out branch: $BRANCH"
else
    echo "🔄 Cloning repository..."
    git clone $REPO_URL
    cd $DIR_NAME
    git checkout $BRANCH
    echo "✅ Repository cloned and branch checked out: $BRANCH"
fi

echo "🧪 Ready to run tests! Try:"
echo "cd $DIR_NAME"
echo "for test in tests/test_*.sh; do chmod +x \$test; bash \$test; done"