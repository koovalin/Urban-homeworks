import pandas as pd
import os

article_col_name = 'vendor_article'
region_col_name = 'rf_subject'
city_col_name = 'city'
qty_col_name = 'sellout'
sum_col_name = 'sales'
GROUP_COLS = [region_col_name, city_col_name, article_col_name]
SUM_COLS = [qty_col_name, sum_col_name]


def get_db_from_excel(df, group_by_cols: list, sum_by_cols: list):
    excel_db = df[group_by_cols + sum_by_cols].copy()
    for col in sum_by_cols:
        excel_db[col] = excel_db[col].astype(float)
    excel_db = excel_db.groupby(group_by_cols)[sum_by_cols].sum().reset_index()
    return excel_db


def save_table_to_csv(prepared_table, output_file_path: str):
    csv_folder = f".\\csv"
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
    output_file_path = f"{csv_folder}\\{output_file_path}.csv"
    prepared_table.to_csv(output_file_path, sep=';', index=False, encoding='CP1251', decimal=',')


def creat_sales_csv_file(new_db, group_cols: list, sum_cols: list[str], file_name: str):
    new_db = get_db_from_excel(new_db, group_cols, sum_cols)
    save_table_to_csv(new_db, file_name)


if __name__ == "__main__":
    file_path = "sales.xlsb"
    output_file_name = "sales"
    db = pd.read_excel(file_path)
    creat_sales_csv_file(db, GROUP_COLS, SUM_COLS, output_file_name)
