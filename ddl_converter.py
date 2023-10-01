import re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='pl', target='en')

def translate(ddl_code):
    output_string = ""
    ddl_code = ddl_code.replace(" ", "")
    ddl_code = ddl_code.lower()
    tables = ddl_code.split('\n')
    for table in tables:
        splitted = table.split(':')
        columns_all = splitted[1]
        columns = columns_all.split(',')
        output_string += f'{splitted[0]}:'
        for column in columns:
            if len(column) > 3:
                column = column.replace("_", " ")
                column = f'{column}({translator.translate(column).lower()})'
                column = column.replace(" ", "_")
                output_string += f',{column}'
            else:
                output_string += f',{column}'
        output_string += '\n'
        output_string = output_string.replace(":,", ":")

    return output_string