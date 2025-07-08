# mapping_utils.py

def get_nested_value(data, path):
    """
    Extrai valor de um caminho como 'Pessoa.Empresa.Nome'.
    Funciona para dicts diretos e listas de pares chave-valor.
    """
    keys = path.split('.')
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)

        elif isinstance(current, list):
            # Tenta achar par com 'chave' == key
            match = next(
                (item for item in current if isinstance(item, dict) and item.get('chave') == key),
                None
            )
            if match:
                current = match.get('valor')
            else:
                return None
        else:
            return None

    return current


def apply_mapper(data, mapper):
    """
    Usa o mapper para transformar os campos de entrada.
    Funciona com dados mistos (dict + lista de pares).
    Retorna dict organizado por objeto (Contact, Account etc).
    """
    result = {}

    for source_field, target_path in mapper.items():
        value = get_nested_value(data, source_field)

        if value is None:
            continue

        target_object, target_field = target_path.split('.', 1)

        if target_object not in result:
            result[target_object] = {}

        result[target_object][target_field] = value

    return result
