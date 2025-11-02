# Personal Website

A professional static personal website with blog functionality, built for GitHub Pages.

## Features

- Professional, responsive design
- Blog system with Markdown-to-HTML conversion
- Separate resume page
- Image asset management
- No CMS required - just write Markdown files
- Optimized for GitHub Pages deployment

## Project Structure

```
personal-website/
├── index.html              # Blog homepage
├── resume.html            # Resume page
├── post-template.html     # Template for blog posts
├── build.py               # Build script to convert markdown to HTML
├── requirements.txt       # Python dependencies
├── css/
│   └── style.css         # Main stylesheet
├── posts/
│   ├── *.md              # Your markdown blog posts
│   └── *.html            # Generated HTML posts (created by build.py)
├── assets/
│   └── images/           # Image files for blog posts
└── js/                   # JavaScript files (optional)
```

## Getting Started

### 1. Install Dependencies

First, create a virtual environment and install the required Python packages:

```bash
cd personal-website

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

Note: The virtual environment directory (`venv/`) is already in `.gitignore` so it won't be committed to your repository.

### 2. Write a Blog Post

Create a new markdown file in the `posts/` directory. Each post must include frontmatter with title, date, and excerpt:

```markdown
---
title: Your Post Title
date: 2025-01-15
excerpt: A brief description of your post that will appear on the blog homepage.
---

## Your Content Here

Write your blog post content using standard Markdown syntax...
```

#### Markdown Features Supported

- Headings (`#`, `##`, `###`, etc.)
- Bold and italic text
- Links: `[text](url)`
- Images: `![alt text](../assets/images/image.png)`
- Code blocks with syntax highlighting
- Lists (ordered and unordered)
- Tables
- Blockquotes

#### Using Images

1. Place your images in `assets/images/`
2. Reference them in your markdown:
   ```markdown
   ![Image description](../assets/images/your-image.jpg)
   ```

### 3. Build the Site

Run the build script to convert your markdown posts to HTML:

```bash
# Make sure your virtual environment is activated
source venv/bin/activate  # On Linux/Mac

# Run the build script
python build.py
```

This will:
- Convert all `.md` files in `posts/` to HTML
- Generate individual post pages
- Update `index.html` with the list of posts

### 4. Preview Locally

You can preview your site locally using Python's built-in HTTP server:

```bash
python -m http.server 8000
```

Then open your browser to `http://localhost:8000`

### 5. Deploy to GitHub Pages

#### Initial Setup

1. Create a new repository on GitHub (e.g., `username.github.io` or any repository name)

2. Initialize git in your project directory (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Personal website"
   ```

3. Add your GitHub repository as remote:
   ```bash
   git remote add origin https://github.com/username/repository-name.git
   git branch -M main
   git push -u origin main
   ```

#### Configure GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**

Your site will be available at `https://username.github.io/repository-name/` (or `https://username.github.io/` if using a username repository).

#### Publishing New Posts

Whenever you write a new post:

```bash
# 1. Write your markdown post in posts/

# 2. Activate virtualenv and build the site
source venv/bin/activate
python build.py

# 3. Commit and push
git add .
git commit -m "Add new blog post"
git push
```

GitHub Pages will automatically update your site within a few minutes.

## Customization

### Updating Your Information

1. **Resume**: Edit `resume.html` to update your professional information
2. **Blog homepage**: Edit the hero section in `index.html`
3. **Footer**: Update footer information in all HTML files
4. **Navigation**: Modify the nav links in header sections

### Styling

Edit `css/style.css` to customize:
- Colors (see CSS variables at the top of the file)
- Fonts
- Layout
- Responsive breakpoints

### Template

Modify `post-template.html` to change the structure of blog post pages.

## Tips

- **Frontmatter is required**: Every markdown file must have valid frontmatter (title, date, excerpt)
- **Date format**: Use `YYYY-MM-DD` format for dates (e.g., `2025-01-15`)
- **File names**: Use descriptive file names for your markdown files (e.g., `my-first-post.md`)
- **URL slugs**: Post URLs are automatically generated from titles (e.g., "My First Post" → `my-first-post.html`)
- **Images**: Store all images in `assets/images/` and use relative paths from the posts directory

## Workflow Summary

1. Write markdown post in `posts/your-post-name.md`
2. Activate virtualenv: `source venv/bin/activate`
3. Run `python build.py`
4. Test locally with `python -m http.server 8000`
5. Commit and push to GitHub
6. GitHub Pages updates automatically

## Troubleshooting

### Build script errors

- **"No frontmatter found"**: Make sure your markdown file starts with `---` and includes title, date, and excerpt
- **"Missing required field"**: Check that all three frontmatter fields are present

### GitHub Pages not updating

- Check that you committed and pushed all files
- Verify GitHub Pages is enabled in repository settings
- Wait 2-3 minutes for GitHub to rebuild the site
- Check the Actions tab for build errors

### Images not showing

- Verify the image path is correct relative to the post location
- Ensure images are committed to the repository
- Check image file names match exactly (case-sensitive on Linux/GitHub)

## License

This is a personal website template. Feel free to use and modify it for your own site.

## Contact

- Email: ilya at ovsy dot com
- LinkedIn: [linkedin.com/in/iliao](https://www.linkedin.com/in/iliao/)
