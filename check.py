import json
import sys

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'Не найден файл: {path}')
        sys.exit(1)
    except json.JSONDecodeError:
        print(f'Ошибка в файле: {path}')
        sys.exit(1)

def storage_buckets(config):
    st_resul = []
    storage = config.get('storage_buckets', [])
    for st in storage:
        name = st.get('name', 'noname')
        if st.get('public', True):
            st_resul.append(f'Бакет {name} публичен. СОВЕТ: сделать не публичным!')
        if not st.get('encrypted', False):
            st_resul.append(f'В {name} отсутствует шифрование. СОВЕТ: сделать шифрование!')
    return st_resul

check = {'port': [22, 3389], 'source': ['0.0.0.0/0']}

def firewall_rules(config):
    fw_resul = []
    
    fw = config.get('firewall_rules', [])
    for fire in fw:
        fw_name = fire.get('id', 'no id')
        port = fire.get('port', 'unknown port')
        source = fire.get('source', 'unknown source')

        if port in check['port'] and source in check['source']:
            fw_resul.append(f'Опасный порт "{fw_name}", порт {port} открыт для {source}')
    
    return fw_resul


def main():
    filename = input('Введите название файла ')

    config = read_file(filename)

    stor = storage_buckets(config)
    frwll = firewall_rules(config)

    result = (stor + frwll)

    for res in result:
        print(res)

if __name__ == '__main__':
    main()