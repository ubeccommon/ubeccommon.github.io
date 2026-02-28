#!/usr/bin/env python3
"""
Script to update author and copyright information in markdown documents.
Recursively processes all .md files in the docs folder and subdirectories.
"""

import os
import re
from pathlib import Path


def update_markdown_file(file_path):
    """
    Update author and copyright information in a single markdown file.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        tuple: (file_path, was_modified, num_author_replacements, num_copyright_replacements)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        author_count = 0
        copyright_count = 0
        
        # Replace author
        content, author_count = re.subn(
            r'author:\s*"Erdpuls Müllrose"',
            'author: "Michel Garand"',
            content
        )
        
        # Replace copyright (handles both em-dash — and regular hyphen -)
        content, copyright_count = re.subn(
            r'©\s*2025[–-]2026\s+Erdpuls Müllrose\s*[–-]\s*Center for Sustainability Literacy, Citizen Science and Reciprocal Economics',
            '© 2025–2026 Michel Garand | Erdpuls Müllrose — Center for Sustainability Literacy, Citizen Science and Reciprocal Economics',
            content
        )
        
        # Write back if modified
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return file_path, True, author_count, copyright_count
        else:
            return file_path, False, 0, 0
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return file_path, False, 0, 0


def process_docs_directory(docs_path='./docs'):
    """
    Recursively process all markdown files in the docs directory.
    
    Args:
        docs_path: Path to the docs directory (default: './docs')
        
    Returns:
        dict: Summary statistics
    """
    docs_dir = Path(docs_path)
    
    if not docs_dir.exists():
        print(f"Error: Directory '{docs_path}' not found.")
        return None
    
    if not docs_dir.is_dir():
        print(f"Error: '{docs_path}' is not a directory.")
        return None
    
    # Find all markdown files
    md_files = list(docs_dir.rglob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in '{docs_path}' or subdirectories.")
        return None
    
    print(f"Found {len(md_files)} markdown file(s) to process.\n")
    
    # Process each file
    total_author_replacements = 0
    total_copyright_replacements = 0
    modified_files = []
    
    for md_file in sorted(md_files):
        file_path, was_modified, author_count, copyright_count = update_markdown_file(md_file)
        
        if was_modified:
            modified_files.append(file_path)
            total_author_replacements += author_count
            total_copyright_replacements += copyright_count
            print(f"✓ Updated: {file_path.relative_to(docs_dir)}")
            print(f"  - Author replacements: {author_count}")
            print(f"  - Copyright replacements: {copyright_count}\n")
        else:
            print(f"- Skipped: {file_path.relative_to(docs_dir)} (no changes needed)\n")
    
    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total files processed: {len(md_files)}")
    print(f"Files modified: {len(modified_files)}")
    print(f"Total author replacements: {total_author_replacements}")
    print(f"Total copyright replacements: {total_copyright_replacements}")
    
    return {
        'total_files': len(md_files),
        'modified_files': len(modified_files),
        'author_replacements': total_author_replacements,
        'copyright_replacements': total_copyright_replacements
    }


if __name__ == '__main__':
    import sys
    
    # Allow custom docs path as command-line argument
    docs_path = sys.argv[1] if len(sys.argv) > 1 else './docs'
    
    print(f"Processing markdown files in: {docs_path}\n")
    process_docs_directory(docs_path)
