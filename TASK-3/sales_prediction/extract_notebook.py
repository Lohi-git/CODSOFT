import json
import re

with open("sales-prediction-simple-linear-regression.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

code_cells = []
for cell in notebook.get("cells", []):
    if cell.get("cell_type") == "code":
        source = "".join(cell.get("source", []))
        if source.strip():
            # Adjust the dataset path to the local one
            source = re.sub(
                r'["\']\.\./input/advertising\.csv["\']',
                '"data/Advertising.csv"',
                source
            )
            # Remove plt.show() so execution doesn't block waiting for user to close windows
            source = source.replace("plt.show()", "# plt.show()")
            code_cells.append(source)

full_code = "\n\n# --- CODE CELL ---\n\n".join(code_cells)

# Write output script
with open("run_notebook.py", "w", encoding="utf-8") as f:
    f.write(full_code)

print("Successfully extracted code to run_notebook.py")
