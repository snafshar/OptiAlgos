def kmeans(points,k=2,steps=20):
    centroids=[list(p) for p in points[:k]]
    for _ in range(steps):
        groups=[[] for _ in range(k)]
        for point in points:
            index=min(range(k),key=lambda i:sum((point[j]-centroids[i][j])**2 for j in range(len(point))))
            groups[index].append(point)
        updated=[([sum(p[j] for p in group)/len(group) for j in range(len(group[0]))] if group else centroids[i]) for i,group in enumerate(groups)]
        if updated==centroids:return centroids
        centroids=updated
    return centroids
if __name__=='__main__':print(kmeans([[1,1],[1,2],[8,8],[9,8]]))