# CSCI 8945: Advanced Representation Learning

Welcome to the course website for **CSCI 8945: Advanced Representation Learning**! This repository contains all course materials including lecture notebooks, assignments, and documentation.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Fall2025
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the documentation:**
   ```bash
   make html
   ```

4. **View the website:**
   ```bash
   make serve
   ```
   Then open http://localhost:8000 in your browser.

## 📚 Course Structure

```
Fall2025/
├── notebooks/              # Jupyter notebooks for tutorials
│   └── tutorial1_pca.ipynb
├── course_info/            # Course information pages
│   ├── syllabus.rst
│   ├── assignments.rst
│   └── resources.rst
├── _static/                # Custom CSS and assets
├── _templates/             # Sphinx templates
├── conf.py                 # Sphinx configuration
├── index.rst              # Main course page
├── requirements.txt       # Python dependencies
├── Makefile              # Build commands
└── README.md             # This file
```

## 🎓 Course Content

### Tutorial Notebooks

1. **Tutorial 1: Principal Component Analysis (PCA)**
   - Mathematical foundations
   - Implementation from scratch
   - Comparison with sklearn
   - Real-world applications

*More tutorials will be added as the course progresses.*

### Course Information

- **Syllabus**: Detailed course description, objectives, and policies
- **Assignments**: Programming assignments and project descriptions  
- **Resources**: Textbooks, papers, datasets, and tools

## 🛠️ Development

### Building the Documentation

The course website is built using [Sphinx](https://www.sphinx-doc.org/) with the [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io/).

**Available make targets:**

```bash
make html           # Build HTML documentation
make clean          # Clean build files
make serve          # Serve documentation locally
make watch          # Auto-rebuild on changes
make clean-notebooks # Clear notebook outputs
make install-deps   # Install dependencies
make build-course   # Complete build process
```

### Adding New Content

**Adding a new tutorial notebook:**

1. Create the notebook in the `notebooks/` directory
2. Add it to the toctree in `index.rst`
3. Rebuild the documentation with `make html`

**Adding course information:**

1. Create or edit `.rst` files in `course_info/`
2. Update the toctree in `index.rst` if needed
3. Rebuild with `make html`

### Notebook Guidelines

- **Clear structure**: Use markdown cells for explanations
- **Executable code**: Ensure all code cells run without errors
- **Documentation**: Include docstrings and comments
- **Reproducibility**: Set random seeds for consistent results
- **Visualization**: Include plots and figures where helpful

## 📱 Running Notebooks

### Local Environment

```bash
# Install Jupyter
pip install jupyter

# Start Jupyter Lab
jupyter lab

# Or Jupyter Notebook
jupyter notebook
```

### Google Colab

Each notebook includes a "Open in Colab" badge for easy cloud execution:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/csci8945-advanced-representation-learning/blob/main/notebooks/tutorial1_pca.ipynb)

### Computing Resources

- **University Cluster**: Contact instructor for access
- **Cloud Platforms**: AWS, GCP, Azure (educational credits available)
- **Free Options**: Google Colab, Kaggle Kernels

## 🎨 Customization

### Styling

The website uses custom CSS in `_static/custom.css` for:
- Course-specific color scheme
- Enhanced notebook styling
- Responsive design
- Print-friendly layouts

### Configuration

Sphinx settings are in `conf.py`:
- Extensions for notebook support
- Theme configuration
- Mathematical notation settings
- Navigation structure

## 📦 Dependencies

**Core requirements:**
- `sphinx>=4.0.0` - Documentation generation
- `sphinx-rtd-theme>=1.0.0` - Read the Docs theme
- `nbsphinx>=0.8.0` - Jupyter notebook support
- `numpy>=1.21.0` - Numerical computing
- `matplotlib>=3.5.0` - Plotting
- `scikit-learn>=1.0.0` - Machine learning
- `jupyter>=1.0.0` - Interactive computing

**Optional (for advanced tutorials):**
- `torch>=1.10.0` - Deep learning
- `transformers>=4.15.0` - NLP models

See `requirements.txt` for the complete list.

## 🚀 Deployment

### GitHub Pages

1. Build the documentation: `make html`
2. Create a `gh-pages` branch
3. Copy `_build/html/` contents to the branch
4. Push to GitHub
5. Enable GitHub Pages in repository settings

### Read the Docs

1. Connect your GitHub repository to [Read the Docs](https://readthedocs.org/)
2. Configure the build settings
3. Documentation will auto-build on commits

### University Server

Contact your IT department for hosting options and requirements.

## 🤝 Contributing

### Students

- **Report issues**: Use GitHub issues for bugs or suggestions
- **Ask questions**: Use the course discussion forum
- **Contribute examples**: Submit interesting applications or variations

### Instructors

- **Fork the repository** for your own course
- **Customize content** for your specific needs
- **Share improvements** via pull requests

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Notebooks**: Clear structure with markdown explanations
- **Documentation**: Write clear, helpful comments

## 📄 License

This course material is provided for educational purposes. 

**Code**: MIT License - feel free to use and adapt
**Content**: Creative Commons Attribution 4.0 - please provide attribution

## 📞 Support

### Course-Related

- **Discussion Forum**: [Course Forum Link]
- **Office Hours**: [Schedule and Location]
- **Email**: [Instructor Email]

### Technical Issues

- **Documentation**: Check Sphinx and nbsphinx documentation
- **GitHub Issues**: Report bugs or feature requests
- **Stack Overflow**: General Python/Jupyter questions

## 🔗 Links

- **Course Website**: [Deployed Site URL]
- **Repository**: [GitHub Repository URL]
- **Resources**: See course_info/resources.rst
- **University Course Catalog**: [Catalog Link]

---

**Happy Learning! 🎓**

*This course website was inspired by the excellent [UvA Deep Learning Notebooks](https://uvadlc-notebooks.readthedocs.io/en/latest/).*
