import os
import nbformat
from nbclient import NotebookClient

script_dir = os.path.dirname(os.path.abspath(__file__))
notebook_path = os.path.join(script_dir, 'notebook', 'movie_rating_prediction.ipynb')

print(f"Loading notebook from {notebook_path}...")
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

print("Executing notebook...")
client = NotebookClient(
    nb,
    timeout=600,
    kernel_name='python3',
    resources={'metadata': {'path': os.path.join(script_dir, 'notebook')}}
)
client.execute()

print("Saving executed notebook...")
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Execution finished successfully!")
