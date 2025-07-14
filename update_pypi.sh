#!/bin/bash
# Update PyPI package script

echo "🔄 Updating ttperf package..."

# Check if version argument provided
if [ $# -eq 0 ]; then
    echo "Usage: ./update_pypi.sh <new_version>"
    echo "Example: ./update_pypi.sh 0.1.1"
    exit 1
fi

NEW_VERSION=$1

echo "📝 Updating version to $NEW_VERSION..."
sed -i "s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

echo "🏗️ Building package..."
source venv/bin/activate
python -m build

echo "📦 Uploading to PyPI..."
twine upload dist/*

echo "✅ Package updated successfully!"
echo "📋 Next steps:"
echo "   - git add ."
echo "   - git commit -m \"🚀 Release v$NEW_VERSION\""
echo "   - git push origin master" 