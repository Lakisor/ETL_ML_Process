def get_data_query(table_name: str = "input_data") -> str:
    return f"SELECT * FROM {table_name};"
