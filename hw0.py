def test_print():
    print ("Hello world!")

def list_set_length(x):
    return len(x)

def set_intersect(S : set, T: set) -> set:
    #For every x in set S if x is in T add to intersect set
    return {x for x in S if x in T}

    # intersect = set()

    # for i in S:
    #     if i in T:
    #         intersect.add(i)
    # return intersect


def three_tuples(S : set) -> list[tuple]:

    return [(i,j,k) for i in S for j in S for k in S if i + j + k == 0]

    # for i in S:
    #     for j in S:
    #         for k in S:
    #             if i + j + k == 0:
    #                 print(f"{i} + {j} + {k} = 0") 


    
def dict_init():
    mydict = [{'Hopper':'Grace'}, {'Einstein':'Albert'}, {'Turing':'Alan'}, {'Lovelace':'Ada'}]
    return mydict

def dict_find(dlist: list[dict[str,str]], k) -> list:
    return [x.get(k,'NOT PRESENT') for x in dlist]

def file_line_count(fileloc : str) -> int:
    with open(fileloc, 'r') as file:
        return len(file.readlines())

def make_inverse_index(strlist : list[str]) :
    #strlist = folder containing documents
    inverse_index = {}

    for documentNumber in range(len(strlist)):
        words = strlist[documentNumber].split(' ')
        for word in words:
            if word in inverse_index:
                inverse_index[word].add(documentNumber)
            else:
                inverse_index[word] = {documentNumber}

    # print(inverse_index)
    return inverse_index

#Can contain atleast one word from the query
def or_search(inverseIndex , query : list[str]):
    documentNumbers = set()

    for word in query:
        if word in inverseIndex:
            documentNumbers.update(inverseIndex[word])

    return documentNumbers

#Must contain all words in query
def and_search(inverseIndex , query : list[str]):
    if len(query) == 1:
        return inverseIndex[query[0]]
    else:
        word_1 = query.pop(0)
        word_2 = query.pop(0)

        documentNumber = set_intersect(inverseIndex[word_1], inverseIndex[word_2])

        while(len(query) > 0):
            word = query.pop(0)
            documentNumber = set_intersect(documentNumber, inverseIndex[word])

        return documentNumber



#Decending order
def most_similar(inverseIndex , query : list[str]):
    #dictionary[ word, {doc # : # of occurances} ]
    #dict[str, {int : int} ]
    mapping = dict()
    sim_dict = dict()
    # indices = []

    folder.seek(0)
    stories = folder.readlines()

    for item in query:
        #get document numbers where query item is found
        doc_numbers = inverseIndex[item]

        for doc_num in doc_numbers:
            line = stories[doc_num].split(' ')

            for word in line:
                    # if word in line: #might be redundant
                        if word == item:
                            if word not in mapping:
                                mapping[word] = {doc_num : 1}
                            else: #if the word is in mapping
                                if doc_num not in mapping[word]:
                                    mapping[word].update({doc_num : 1})
                                else:
                                    similarity = mapping[word]
                                    similarity[doc_num] = similarity[doc_num] + 1
                                    mapping[word] = similarity

    for _ , similarity in mapping.items():
        for doc_num, score in similarity.items():
            if doc_num not in sim_dict:
                sim_dict[doc_num] = score
            else:
                sim_dict.update({doc_num : sim_dict[doc_num] + score})
    
    sim_dict = sorted(sim_dict.items(), key = lambda x: x[1], reverse=True)
    return sim_dict
    # for doc_num, _ in sim_dict:
    #     indices.append(doc_num)

    # return indices

if __name__ == '__main__':
    test_print()

    items_list = [2, 1, 2, 3, 4, 3, 2, 1]
    items_set = {2, 1, 2, 3, 4, 3, 2, 1}

    print(f"item list len: {list_set_length(items_list)}")
    print(f"item set len: {list_set_length(items_set)}\n")

    EX = {x*y for x in {1,2,3} for y in {2,3,4}}
    {2, 3, 4, 6, 8, 9, 12}

    print(f"{EX}\n") 

    S = {1,4,7}
    T = {1,2,3,4,5,6}

    print(f"Intersect of {S} and {T}: \n{set_intersect(S, T)}")

    S = {-4,-2, 1, 2, 5, 0}
    print(f"\n{three_tuples(S)}")

    print(f"\n{dict_init()}")
    print(f"key = Turing : {dict_find(dict_init(), 'Turing')}")

    print(f"\nNumber of lines in file: {file_line_count('stories.txt')}")

    with open('stories.txt', 'r') as folder:
        inverse_index = make_inverse_index(folder.readlines())

        query = ['WASHINGTON', 'A', 'former']


        L1 = or_search(inverse_index, query = ['other','june','all-you-can'])
        print(f"or_search results: {L1}")

        L2 = and_search(inverse_index, query = ['other','june','all-you-can'])
        print(f"and_search results: {L2}")

        L3 = most_similar(inverse_index, ['straight-A', 'survived', 'facts'])
        print(f"Most similar documents: {L3}")
