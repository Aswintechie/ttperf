#!/bin/bash
# Release script for ttperf

echo "🚀 ttperf Release Script"

# Check if version argument provided
if [ $# -eq 0 ]; then
    echo "Usage: ./release.sh <new_version>"
    echo "Example: ./release.sh 0.1.1"
    exit 1
fi

NEW_VERSION=$1
TAG_NAME="v$NEW_VERSION"

echo "📝 Updating version to $NEW_VERSION..."
sed -i "s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

echo "📋 Updating CHANGELOG.md..."
# Add new version to changelog
sed -i "s/## \[Unreleased\]/## [Unreleased]\n\n## [$NEW_VERSION] - $(date +%Y-%m-%d)/" CHANGELOG.md

echo "📦 Committing version bump..."
git add pyproject.toml CHANGELOG.md
git commit -m "🚀 Bump version to $NEW_VERSION"

echo "🏷️ Creating and pushing tag..."
git tag -a "$TAG_NAME" -m "Release $TAG_NAME"
git push origin master
git push origin "$TAG_NAME"

echo "✅ Release process initiated!"
echo ""
echo "🔥 GitHub Actions will now:"
echo "   1. Run tests across Python versions"
echo "   2. Build the package"
echo "   3. Publish to PyPI"
echo "   4. Create GitHub Release"
echo ""
echo "📊 Monitor progress at:"
echo "   https://github.com/Aswintechie/ttperf/actions"
echo ""
echo "🎯 PyPI package will be available at:"
echo "   https://pypi.org/project/ttperf/$NEW_VERSION/" 