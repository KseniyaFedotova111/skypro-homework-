import pandas as pd


def read_csv_transactions(file_path):
    """
    Считывает финансовые операции из CSV-файла
    """
    df = pd.read_csv(file_path)
    transactions = df.to_dict(orient='records')
    return transactions


def read_excel_transactions(file_path):
    """
    Считывает финансовые операции из Excel-файла
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient='records')
    return transactions
