"""Compile the two editable TeX sources with XeLaTeX; no shell escape."""
from pathlib import Path
import shutil,subprocess

root=Path(__file__).parent
engine=shutil.which('xelatex')
if not engine:raise SystemExit('XeLaTeX is required. Install MiKTeX or TeX Live with ctex.')
(root/'build').mkdir(exist_ok=True)
for name in ['student','solutions']:
    for run in [1,2]:
        result=subprocess.run([engine,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-output-directory=build',name+'.tex'],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (root/'build'/f'{name}-run{run}.txt').write_bytes(result.stdout)
        if result.returncode:
            print(result.stdout.decode('utf-8',errors='replace')[-4000:])
            raise SystemExit(result.returncode)
    print(name, 'compiled',flush=True)
