types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(tickets_dict):
    for key in tickets_dict:
        tickets_dict[key] = list(set(tickets_dict[key]))

def map_types_to_tickets(types_dict, tickets_dict):
    result = {}
    for type_id, type_name in types_dict.items():
        result[type_name] = tickets_dict.get(type_id, [])
    return result


remove_duplicates(tickets)
result = map_types_to_tickets(types, tickets)

for types, tickets in result.items():
    print(f'{types}: {tickets}')