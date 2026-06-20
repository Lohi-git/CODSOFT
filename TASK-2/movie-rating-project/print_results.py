import nbformat

def print_notebook_outputs():
    try:
        with open('notebook/movie_rating_prediction.ipynb', 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        print("="*60)
        print(" IMDB India Movies Rating Prediction Results Summary")
        print("="*60)
        
        found_results = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                for output in cell.outputs:
                    if 'text' in output:
                        text = output['text']
                        if 'results -' in text or 'RMSE:' in text or 'R2 :' in text:
                            print(text.strip())
                            print("-" * 40)
                            found_results = True
                            
        if not found_results:
            print("No printed metrics found in notebook outputs.")
            
    except Exception as e:
        print(f"Error reading notebook: {e}")

if __name__ == '__main__':
    print_notebook_outputs()
