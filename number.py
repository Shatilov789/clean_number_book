import re

def clear_number(apart_contact_list):
    pattern_phone = r"(8|\+7)?\s*?\(?(\d{3})\)?\s*?[-\s]?(\d{3})[-\s]*(\d{2})[-\s]*(\d+)\s*\(*(\w+\.)?\s*(\d+)?\)?"
    sub = r"+7(\2)\3-\4-\5 \6\7"

    for val in apart_contact_list:
        val[5] = re.sub(pattern_phone, sub, val[5])
        apart_contact_list[5].append(val[5])
    return apart_contact_list