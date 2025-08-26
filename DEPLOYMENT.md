# 🚀 Deploying to GitHub Pages

This guide walks you through deploying your CSCI 8945 course website to GitHub Pages using GitHub Actions for automatic deployment.

## 📋 Prerequisites

- GitHub account
- Git installed on your computer
- Course website built and tested locally

## 🎯 Method 1: Automatic Deployment with GitHub Actions (Recommended)

### Step 1: Prepare Your Repository

1. **Create a new repository on GitHub:**
   ```
   Repository name: csci8945-advanced-representation-learning
   Description: Course materials for CSCI 8945: Advanced Representation Learning
   Public: ✅ (required for free GitHub Pages)
   Initialize with README: ❌ (we already have one)
   ```

2. **Prepare your local project:**
   ```bash
   cd /path/to/your/Fall2025/directory
   python setup.py deploy-prep
   ```

3. **Initialize Git repository (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: CSCI 8945 course website"
   git branch -M main
   ```

4. **Connect to GitHub repository:**
   ```bash
   git remote add origin https://github.com/yourusername/csci8945-advanced-representation-learning.git
   git push -u origin main
   ```

### Step 2: Configure GitHub Pages

1. **Go to your GitHub repository**
2. **Click on "Settings" tab**
3. **Scroll down to "Pages" in the left sidebar**
4. **Under "Source", select "GitHub Actions"**
5. **Save the settings**

### Step 3: Enable Actions

1. **Go to the "Actions" tab in your repository**
2. **If prompted, click "I understand my workflows, go ahead and enable them"**
3. **The deployment workflow should start automatically**

### Step 4: Monitor Deployment

1. **Go to Actions tab to see the build progress**
2. **Wait for the "Deploy Course Website to GitHub Pages" workflow to complete (green checkmark)**
3. **Your site will be available at: `https://yourusername.github.io/csci8945-advanced-representation-learning/`**

## 🎯 Method 2: Manual Deployment

If you prefer manual control over deployment:

### Step 1: Build Locally

```bash
python setup.py build
```

### Step 2: Create gh-pages Branch

```bash
# Create and switch to gh-pages branch
git checkout --orphan gh-pages

# Remove all files from the branch
git rm -rf .

# Copy built documentation
cp -r _build/html/* .
cp -r _build/html/.* . 2>/dev/null || true

# Create .nojekyll file
touch .nojekyll

# Add and commit
git add .
git commit -m "Deploy course website"

# Push to GitHub
git push origin gh-pages

# Switch back to main branch
git checkout main
```

### Step 3: Configure GitHub Pages

1. **Go to Settings > Pages**
2. **Set Source to "Deploy from a branch"**
3. **Select Branch: "gh-pages"**
4. **Select Folder: "/ (root)"**
5. **Save**

## 🔧 Updating Your Site

### With Automatic Deployment (Method 1)
Simply push changes to your main branch:
```bash
git add .
git commit -m "Update course content"
git push origin main
```
The site will automatically rebuild and deploy.

### With Manual Deployment (Method 2)
Rebuild and redeploy:
```bash
python setup.py build
git checkout gh-pages
cp -r _build/html/* .
git add .
git commit -m "Update site"
git push origin gh-pages
git checkout main
```

## 📝 Customizing for Your Course

### Update Repository Links

1. **Edit notebooks to update Colab links:**
   In `notebooks/tutorial1_pca.ipynb`, change:
   ```markdown
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/csci8945-advanced-representation-learning/blob/main/notebooks/tutorial1_pca.ipynb)
   ```

2. **Update README.md links:**
   Replace placeholder URLs with your actual repository URLs.

### Custom Domain (Optional)

1. **Add a CNAME file** to your repository root:
   ```bash
   echo "courses.yourdomain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

2. **Configure DNS** at your domain provider:
   - Create a CNAME record pointing to `yourusername.github.io`

## 🛠️ Troubleshooting

### Build Fails
- Check the Actions tab for detailed error logs
- Ensure all dependencies are in `requirements.txt`
- Test build locally with `python setup.py build`
- **Pandoc issues**: The workflow now automatically installs Pandoc
- **Title underline warnings**: Ensure RST title underlines are at least as long as the title text

### Notebook Issues
- Clear outputs: `python setup.py clean`
- Ensure notebooks don't have execution errors
- Check matplotlib backend compatibility

### Pages Not Updating
- Check Actions tab for successful deployment
- Clear browser cache
- Wait a few minutes for CDN updates

### Permission Errors
- Ensure repository is public for free GitHub Pages
- Check that Actions are enabled in repository settings

## 📚 Repository Structure

Your deployed repository should look like:
```
csci8945-advanced-representation-learning/
├── .github/workflows/deploy.yml    # GitHub Actions workflow
├── .nojekyll                      # Disable Jekyll processing
├── notebooks/                     # Course tutorials
├── course_info/                   # Course information
├── _static/                       # CSS and assets
├── conf.py                        # Sphinx configuration
├── index.rst                      # Main page
├── requirements.txt               # Dependencies
├── setup.py                       # Setup script
├── Makefile                       # Build commands
└── README.md                      # Project documentation
```

## 🎉 Success!

Once deployed, your course website will be available at:
- **GitHub Pages URL**: `https://yourusername.github.io/csci8945-advanced-representation-learning/`
- **Custom Domain** (if configured): `https://courses.yourdomain.com/`

Students can now access:
- 📚 Course information and syllabus
- 📓 Interactive Jupyter notebooks
- 📋 Assignment descriptions
- 🔗 Resource links
- 🚀 Direct links to Google Colab

## 🔄 Maintenance

### Regular Updates
- Update course content in source files
- Test locally with `python setup.py serve`
- Push to GitHub for automatic deployment

### Adding New Tutorials
1. Create new notebook in `notebooks/`
2. Add to `index.rst` toctree
3. Test build locally
4. Push to GitHub

### Monitoring
- Check GitHub Actions for deployment status
- Monitor site accessibility
- Review student feedback and analytics

---

**Need help?** Check the [GitHub Pages documentation](https://docs.github.com/en/pages) or open an issue in your repository.
