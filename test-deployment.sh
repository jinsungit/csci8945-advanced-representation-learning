#!/bin/bash
# Test script for GitHub Pages deployment

echo "🧪 Testing Course Website Deployment"
echo "===================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository. Run 'git init' first."
    exit 1
fi

# Check if GitHub remote exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ No GitHub remote found. Add your repository:"
    echo "   git remote add origin https://github.com/USERNAME/REPOSITORY.git"
    exit 1
fi

# Test local build
echo "🔨 Testing local build..."
python setup.py clean
if python setup.py build; then
    echo "✅ Local build successful"
else
    echo "❌ Local build failed. Fix errors before deploying."
    exit 1
fi

# Check if workflow file exists
if [ ! -f ".github/workflows/deploy.yml" ]; then
    echo "❌ GitHub Actions workflow not found"
    exit 1
fi

echo "✅ GitHub Actions workflow found"

# Prepare for deployment
echo "📦 Preparing for deployment..."
python setup.py deploy-prep

# Check git status
echo "📋 Git status:"
git status --porcelain

# Ask user if they want to commit and push
echo ""
echo "🚀 Ready to deploy! Next steps:"
echo "1. Commit your changes:"
echo "   git add ."
echo "   git commit -m 'Deploy course website'"
echo "   git push origin main"
echo ""
echo "2. Go to your GitHub repository > Actions tab to monitor deployment"
echo "3. Once successful, your site will be at:"
echo "   https://$(git remote get-url origin | sed 's/.*github.com[:/]\([^/]*\)\/\([^./]*\).*/\1.github.io\/\2/')/"
echo ""
echo "🎉 Deployment test completed successfully!"
