#!/usr/bin/env python3
"""
Static site generator for personal blog.
Converts markdown posts to HTML using templates.
"""

import os
import re
from datetime import datetime
from pathlib import Path
import markdown
from markdown.extensions import fenced_code, tables, codehilite

# Configuration
POSTS_DIR = Path("posts")
OUTPUT_DIR = Path("posts")
TEMPLATE_FILE = Path("post-template.html")
INDEX_FILE = Path("index.html")
ASSETS_DIR = Path("assets")


def parse_frontmatter(content):
    """
    Parse YAML-style frontmatter from markdown content.

    Expected format:
    ---
    title: Post Title
    date: 2025-01-15
    excerpt: Brief description of the post
    ---
    """
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    if not match:
        raise ValueError("No frontmatter found in markdown file")

    frontmatter_text = match.group(1)
    content_without_frontmatter = content[match.end():]

    # Parse frontmatter fields
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()

    return metadata, content_without_frontmatter


def convert_markdown_to_html(markdown_content):
    """Convert markdown content to HTML."""
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'codehilite',
        'nl2br',
        'sane_lists'
    ])
    return md.convert(markdown_content)


def format_date(date_str):
    """Convert date string to display format."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%B %d, %Y')


def create_slug(title):
    """Create URL-friendly slug from title."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug


def process_post(md_file):
    """
    Process a single markdown file and generate HTML.
    Returns post metadata for index generation.
    """
    print(f"Processing {md_file.name}...")

    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse frontmatter and content
    metadata, markdown_content = parse_frontmatter(content)

    # Validate required fields
    required_fields = ['title', 'date', 'excerpt']
    for field in required_fields:
        if field not in metadata:
            raise ValueError(f"Missing required field '{field}' in {md_file.name}")

    # Convert markdown to HTML
    html_content = convert_markdown_to_html(markdown_content)

    # Add Substack subscription link at the end
    substack_link = '''
<div class="substack-subscribe">
    <p><a href="https://iliaov.substack.com/" target="_blank">Subscribe on Substack</a> to get updates when new posts are published.</p>
</div>
'''
    html_content += substack_link

    # Load template
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    # Create slug for output filename
    slug = create_slug(metadata['title'])
    output_file = OUTPUT_DIR / f"{slug}.html"

    # Format date
    date_display = format_date(metadata['date'])

    # Replace template placeholders
    html = template.replace('{{TITLE}}', metadata['title'])
    html = html.replace('{{DATE_ISO}}', metadata['date'])
    html = html.replace('{{DATE_DISPLAY}}', date_display)
    html = html.replace('{{EXCERPT}}', metadata['excerpt'])
    html = html.replace('{{CONTENT}}', html_content)

    # Write output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  → Generated {output_file}")

    # Return metadata for index generation
    return {
        'title': metadata['title'],
        'date': metadata['date'],
        'date_display': date_display,
        'excerpt': metadata['excerpt'],
        'url': f"posts/{slug}.html",
        'slug': slug
    }


def generate_index(posts):
    """Update index.html with list of blog posts."""
    print("Updating index.html...")

    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Generate blog post cards HTML
    posts_html = ""
    for post in posts:
        posts_html += f"""
            <article class="blog-post-card">
                <h2><a href="{post['url']}">{post['title']}</a></h2>
                <div class="post-meta">
                    <time datetime="{post['date']}">{post['date_display']}</time>
                </div>
                <p class="post-excerpt">{post['excerpt']}</p>
                <a href="{post['url']}" class="read-more">Read more →</a>
            </article>
"""

    # Read current index.html
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Find the blog-posts section and replace its content
    pattern = r'(<section class="blog-posts">)(.*?)(</section>)'
    replacement = f'\\1\n{posts_html}        \\3'

    new_index = re.sub(pattern, replacement, index_content, flags=re.DOTALL)

    # Write updated index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_index)

    print(f"  → Updated index with {len(posts)} posts")


def main():
    """Main build process."""
    print("=" * 60)
    print("Building static site...")
    print("=" * 60)

    # Ensure directories exist
    POSTS_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    # Find all markdown files in posts directory
    md_files = list(POSTS_DIR.glob("*.md"))

    if not md_files:
        print("\nNo markdown files found in posts/ directory.")
        print("Create a .md file in posts/ directory to get started.")
        return

    print(f"\nFound {len(md_files)} markdown file(s)")
    print()

    # Process all posts
    posts = []
    for md_file in md_files:
        try:
            post_metadata = process_post(md_file)
            posts.append(post_metadata)
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
            continue

    print()

    # Update index page
    if posts:
        generate_index(posts)

    print()
    print("=" * 60)
    print(f"Build complete! Generated {len(posts)} post(s)")
    print("=" * 60)


if __name__ == "__main__":
    main()
