import pandas as pd

def export_to_excel(posts, path):
    df = pd.DataFrame(posts)
    df.to_excel(path, index=False)