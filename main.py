def clusterization(filename):
    from math import dist

    clusters = [[] for _ in range(10**4)]
    data = [[float(i) for i in l.split()] for l in open(filename)]
    radius = max(min(dist(i, j) for i in data if i != j) for j in data)

    def f(x, n):
        for p in data:
            if dist(x, p) <= radius and p not in clusters[n]:
                clusters[n].append(p)
                f(p, n)

    k = 0
    while data:
        f(data[0], k)

        for i in clusters[k]:
            data.remove(i)

        k += 1

    return [i for i in clusters if i]

print(clusterization("1.txt"))
