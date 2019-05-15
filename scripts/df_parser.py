import docx_parser
import pandas as pd

REQUIRED_REGIONS = [
    'Кемеровская область',
    'Еврейская автономная область'
]

FILES = [
    './docx_files/02-01.docx',
    './docx_files/02-08.docx',
    './docx_files/04-02.docx',
    './docx_files/12-04.docx',
    './docx_files/19-03.docx',
]

def parse_files(filepath):
    try:
        parsed_df = docx_parser.read_docx_tables(filepath)

        df = pd.concat(parsed_df, ignore_index=True)
        filtered_df = df.loc[df['Unnamed: 0'].isin(REQUIRED_REGIONS)]
        return filtered_df
    except:
        return "Произошла ошибка при обработке документа."

"""
Main function. Here we can manipulate with already parsed and filtered dataframes.
"""
def main():
    for item in FILES:
        result = parse_files(item)
        print(result)
    
if __name__ == "__main__":
    main()