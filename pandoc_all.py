import glob
import os

for f in glob.glob('**/*.md', recursive=True):
    pre, ext = os.path.splitext(f)
    outf = "output/" + pre + ".html"
    os.makedirs(os.path.dirname(outf), exist_ok=True)
    os.system(f"pandoc/core -i \'{f}\' -o \'{outf}\'") 
