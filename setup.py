#!/usr/bin/env python3
"""
Setup script for CSCI 8945: Advanced Representation Learning
Course website and materials

Usage:
    python setup.py install    # Install dependencies
    python setup.py build      # Build documentation
    python setup.py serve      # Serve documentation locally
    python setup.py clean      # Clean build files
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and handle errors."""
    if description:
        print(f"🔄 {description}...")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    else:
        print(f"✅ Python version: {sys.version}")

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False
    
    # Install dependencies
    success = run_command(
        "pip install -r requirements.txt",
        "Installing Python packages"
    )
    
    if success:
        print("✅ Dependencies installed successfully")
    
    return success

def build_documentation():
    """Build the Sphinx documentation."""
    print("🏗️ Building documentation...")
    
    # Clean previous builds
    run_command("make clean", "Cleaning previous builds")
    
    # Build HTML documentation
    success = run_command("make html", "Building HTML documentation")
    
    if success:
        print("✅ Documentation built successfully")
        print("📂 Documentation available in: _build/html/")
        print("🌐 Open _build/html/index.html in your browser")
    
    return success

def serve_documentation():
    """Serve the documentation locally."""
    build_dir = Path("_build/html")
    
    if not build_dir.exists():
        print("❌ Documentation not built yet. Building now...")
        if not build_documentation():
            return False
    
    print("🌐 Starting local server...")
    print("📍 Documentation will be available at: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop the server")
    
    os.chdir(build_dir)
    try:
        subprocess.run([sys.executable, "-m", "http.server", "8000"])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")

def clean_build():
    """Clean build files and notebook outputs."""
    print("🧹 Cleaning build files...")
    
    # Clean Sphinx build
    run_command("make clean", "Cleaning Sphinx build files")
    
    # Clean notebook outputs
    run_command("make clean-notebooks", "Clearing notebook outputs")
    
    print("✅ Cleanup completed")

def check_installation():
    """Check if installation is working correctly."""
    print("🔍 Checking installation...")
    
    # Check if key modules can be imported
    modules_to_check = [
        'numpy', 'matplotlib', 'sklearn', 'jupyter', 'sphinx'
    ]
    
    for module in modules_to_check:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module} - not installed")
            return False
    
    print("✅ All core modules available")
    return True

def prepare_for_deployment():
    """Prepare the project for GitHub Pages deployment."""
    print("📦 Preparing for GitHub Pages deployment...")
    
    # Clear notebook outputs
    print("🧹 Clearing notebook outputs...")
    run_command(
        "find . -name '*.ipynb' -exec jupyter nbconvert --clear-output --inplace {} \\;",
        "Clearing notebook outputs"
    )
    
    # Build documentation
    if build_documentation():
        # Create .nojekyll file if it doesn't exist
        nojekyll_path = Path(".nojekyll")
        if not nojekyll_path.exists():
            nojekyll_path.touch()
            print("✅ Created .nojekyll file")
        
        print("✅ Project ready for deployment!")
        print("\n📋 Next steps:")
        print("1. Push your code to GitHub")
        print("2. Go to Settings > Pages in your GitHub repository")
        print("3. Set Source to 'GitHub Actions'")
        print("4. The site will auto-deploy on every push to main/master")
        print("\n🔗 Your site will be available at:")
        print("   https://yourusername.github.io/repository-name/")
        
        return True
    else:
        print("❌ Build failed. Please fix errors before deployment.")
        return False

def main():
    """Main setup function."""
    parser = argparse.ArgumentParser(
        description="Setup script for CSCI 8945 course website"
    )
    parser.add_argument(
        'action',
        choices=['install', 'build', 'serve', 'clean', 'check', 'all', 'deploy-prep'],
        help='Action to perform'
    )
    
    args = parser.parse_args()
    
    print("🎓 CSCI 8945: Advanced Representation Learning")
    print("=" * 50)
    
    # Check Python version first
    check_python_version()
    
    if args.action == 'install':
        install_dependencies()
        check_installation()
        
    elif args.action == 'build':
        build_documentation()
        
    elif args.action == 'serve':
        serve_documentation()
        
    elif args.action == 'clean':
        clean_build()
        
    elif args.action == 'check':
        check_installation()
        
    elif args.action == 'deploy-prep':
        prepare_for_deployment()
        
    elif args.action == 'all':
        print("🚀 Full setup process...")
        if install_dependencies() and check_installation():
            build_documentation()
            print("\n🎉 Setup completed successfully!")
            print("💡 Run 'python setup.py serve' to start the local server")
        else:
            print("❌ Setup failed. Please check the errors above.")

if __name__ == "__main__":
    main()
