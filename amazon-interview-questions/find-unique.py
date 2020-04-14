def find_unique(delivery_id_confirmations):
    id_set = set()
    for id in delivery_id_confirmations:
        if id in id_set:
            id_set.remove(id)
        else:
            id_set.add(id)
    for id in id_set:
        return id