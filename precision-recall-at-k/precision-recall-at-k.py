def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = recommended[:k]

    tp = len(set(top_k) & set(relevant))
    
    precision = tp/k
    recall = tp/len(relevant)

    return [precision, recall]

recommended = [1,3,5,7,9]
relevant = [1,2,3,4,5]
k = 3

print(precision_recall_at_k(recommended, relevant, k))
    

    
    