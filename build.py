import shutil
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from data import teaching, research

BASE_URL = 'http://127.0.0.1:8000'

""" Serve the website
python -m http.server --directory ./_site/
"""

BUILD_DIR = '_site'
STATIC_DIR = 'static'
CURRENT_PATH = Path.cwd()
BUILD_PATH = CURRENT_PATH / Path(BUILD_DIR)
STATIC_PATH = CURRENT_PATH / Path(STATIC_DIR)
# clean-up build folder
try:
    shutil.rmtree(BUILD_PATH)
except FileNotFound:
    print("Build dir does not exist yet.")
# Copy static assets
shutil.copytree(STATIC_PATH, BUILD_PATH)


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


"""
Index
"""
template = env.get_template('base.html')
output = template.render(
  base_url=BASE_URL,
  title="INDEX"
)
o = BUILD_PATH /  Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)
    
"""
About
"""
# /about.html
template = env.get_template('about.html')
output = template.render(
  base_url=BASE_URL,
  title="ABOUT ME"
)
o = BUILD_PATH / Path("about")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

"""
Teaching
"""
# /teaching.html
template = env.get_template('teaching.html')
output = template.render(
  base_url=BASE_URL,
    title="Teaching",
    universities=teaching
)
o = BUILD_PATH / Path("teaching")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)
    
"""
Research
"""
# /research
template = env.get_template('research.html')
output = template.render(
    base_url=BASE_URL,
    title="Research",
    projects=research['projects']
)
o = BUILD_PATH / Path("research")
o.mkdir(parents=True, exist_ok=True)
o = o / Path('index.html')
with o.open(mode='w') as fh:
    fh.write(output)

# /research/{slug}
template = env.get_template('research_detail.html')
for r in research['projects']:
    output = template.render(
        base_url=BASE_URL,
        title='Project details',
        project=r
    )
    o = BUILD_PATH / Path("research/"+r['slug'])
    o.mkdir(parents=True, exist_ok=True)
    o = o / Path('index.html')
    with o.open(mode='w') as fh:
        fh.write(output)