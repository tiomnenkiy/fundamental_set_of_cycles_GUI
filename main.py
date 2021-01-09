import networkx
import matplotlib.pyplot as plt

def Circl_start(Matrix, size):
    # getting karkas and its edges
    ans = []
    list = dfs_start(Matrix, size)
    karkas = list[0]
    karkasSize = list[1]
    print(karkas)
    print(karkasSize)

    i = 0
    for list in karkas:
        if (karkasSize[i] < 3):
            i += 1
            continue
        ans.append(Circl(Matrix, karkas[i], karkasSize[i]))
        i += 1

    return ans


def Circl(Matrix, karkas, size):
    ans = []
    edges = []
    for c in range(size - 1):
        if Matrix[karkas[c]][karkas[c + 1]]:
            edges.append([karkas[c], karkas[c + 1]])
        else:
            for l in range(1, c):
                if (Matrix[karkas[c - l]][karkas[c + 1]]):
                    edges.append([karkas[c - l], karkas[c + 1]])
                    break
    print(edges)
    i = 2
    v = karkas[i]

    # check first cycle
    if Matrix[v][karkas[0]]:
        cur = []
        for j in range(0, 3):
            cur.append(karkas[j])
        cur.append(karkas[0])
        ans.append(cur)
    i += 1

    while i != size:
        v = karkas[i]
        for j in range(size):
            # important to iterate by karkas vertexes
            if Matrix[v][karkas[j]] and (edges.count([karkas[j], v]) == 0) and (edges.count([v, karkas[j]]) == 0):
                cur = []
                curSize = 0
                for c in range(j, i + 1):
                    cur.append(karkas[c])
                    curSize += 1
                cur.append(karkas[j])
                curSize += 1
                for c in range(1, curSize - 1):
                    # if karkas is tree -
                    # we remove redundant vertexes from cycle
                    if not Matrix[cur[c - 1]][cur[c]]:
                        cur.remove(cur[c - 1])
                        curSize -= 1
                ans.append(cur)
        i += 1
    return ans


def dfs_start(Matrix, size):
    visitedAll = []
    visitedSize = []
    vSize = 0
    curSize = 0

    visitedAll.append(dfs(0, Matrix, [], 0, size))
    for i in visitedAll[0]:
        curSize += 1
    visitedSize.append(curSize)
    vSize += curSize

    # if graph consists of connectivity components
    i = 1
    while vSize < size:
        visitedAll.append(dfs(vSize, Matrix, [], 0, size))
        curSize = 0
        for j in visitedAll[i]:
            curSize += 1
        visitedSize.append(curSize)
        vSize += curSize
        i += 1
    return [visitedAll, visitedSize]

def dfs(v, Matrix, visited, vSize, size):

    if(visited.count(v) == 0):
        visited.append(v)
        vSize += 1
    else:
        return visited
    for i in range(size):
        if Matrix[v][i] and visited.count(i) == 0:
            dfs(i, Matrix, visited, vSize, size)
            if vSize == size:
                break
        if i == size-1 and vSize != size and vSize > 1:
            dfs(visited[-2], Matrix, visited, vSize, size)
            if vSize == size:
                break
        if vSize == size:
            break
    return visited

def getEdges(Matrix, size):
    edges = []
    for i in range(size):
        for j in range(size):
            if Matrix[i][j]:
                edges.append((i, j))
    return edges


if __name__ == '__main__':
    Matrix = [[0, 1, 1, 1, 0, 0],
              [1, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 0, 0, 1, 0]]
    Matrixm = [[0, 0, 1, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 0, 0, 1, 0]]
    MatrixK = [[0, 0, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 0]]
    MatrixKk = [[0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0]]
    Matrixmm = [[0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 0, 0, 1, 0]]
    Matrix_K5m = [[0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 0, 0 ,0],
                 [0, 1, 1, 0, 0]]
    Matrix_K5 = [[0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0 ,1],
                 [1, 1, 1, 1, 0]]
    Matrix_СHN = [[0, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 0, 1, 1],
                [0, 0, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 1, 0]]
    Matrix_СHN_Bad = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]
    Matrix_N = [[0, 0 ,0],
                [0, 0, 0],
                [0, 0, 0]]
    Matrix_T = [[0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]]
    Matrix_D = [[0, 1],
                [1, 0]]

    print(Circl_start(MatrixKk, 6))
    # edges = getEdges(Matrixmm, 6)
    # graph = networkx.Graph()
    # graph.add_edges_from(edges)
    # networkx.draw(graph)
    # plt.show()

# def Circl(v, Matrix, Karkas, ptr, num, Gnum, size):
#     Karkas[ptr] = v
#     ptr += 1
#
#     num += 1
#     Gnum[v] = num
#     for j in range(size):
#         if Matrix[v][j]:
#             if Gnum[j] == 0:
#                 Circl(j, Matrix, Karkas, ptr, num, Gnum, size)
#             elif (j != Karkas[ptr]) and (Gnum[j] < Gnum[v]) and (v-j > 1):
#                 ans = []
#                 for i in range(j, ptr+1):
#                     ans.append(Karkas[i]+1)
#                 ans.append(j+1)
#                 print(ans)
#     ptr -= 1


