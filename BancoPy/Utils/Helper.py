from datetime import date
from datetime import datetime

formato_de_data_usado = '%d/%m/%Y'

def date_para_string(data: date) -> str:
    return data.strftime(formato_de_data_usado)

def string_para_date(data: str) -> date:
    return datetime.strptime(data, formato_de_data_usado)

def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'