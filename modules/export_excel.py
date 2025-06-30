from modules.log_config import setup_logger
logger = setup_logger('export_excel')
import pandas as pd

def export_to_excel(posts, path):
    df = pd.DataFrame(posts)
    df.to_excel(path, index=False)