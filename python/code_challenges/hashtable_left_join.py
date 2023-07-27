from data_structures.hashtable import Hashtable


def left_join(synonym_map, antonym_map):
    results_list = []
    synonym_hashtable = Hashtable()
    for key, value in synonym_map.items():
        synonym_hashtable.put(key, value)

    antonym_hashtable = Hashtable()
    for key, value in antonym_map.items():
        antonym_hashtable.put(key, value)

    for key, synonym in synonym_hashtable.table.items():
        antonym = antonym_hashtable.get(key)
        results_list.append((key, synonym, antonym))
        
    return results_list
