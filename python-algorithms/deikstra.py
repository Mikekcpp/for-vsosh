"""
5
0 20 5 0 0
20 0 0 10 1000
5 0 0 100 0
0 10 100 0 20
0 1000 0 20 0
0 4

output: {0: 0, 1: 20, 2: 5, 3: 30, 4: 50}
"""

def way_d(n,  a, start, end):
    red = set(range(n))
    yellow = {start: 0}
    green = dict()

    while yellow:
        now = list(yellow.keys())[0]
        now_distance = yellow[now]
        green[now] = now_distance #(1)
        del yellow[now]

        for neighbor in range(n):
            if neighbor not in green and a[now][neighbor] != 0: # (2) 
                lenn = a[neighbor][now]
                possible_fastest = now_distance + lenn  # (3)
                
                if neighbor in yellow and possible_fastest < yellow[neighbor]: # (4):
                    yellow[neighbor] = possible_fastest
                elif neighbor not in yellow: # (5):
                    yellow[neighbor] = possible_fastest
                    red.remove(neighbor)
    
    st = 0
    i = end
    nw = []
    while i != start:
        nw.append(i + 1)
        for g in range(n):
            if a[i][g] != 0 and a[g][i] == green[i] - green[g]: # 1) точка g связана с точкой i. 2) Расстояние g == (расстоянию до i) - 1
                i = g
                break
        print(nw)
                
    nw.append(st + 1)
    return nw[::-1]

                
n = int(input())
a = [[int(i) for i in input().split()] for j in range(n)]
start, end = [int(i) for i in input().split()]    


print(way_d(n, a, start, end))


'''
Алгоритм дейкстры:
входные данные: a (матрица смежности n на n); start, finish: начальная и конечные точки

Алгоритм:
Задаем множество red, и два словаря, yellow и green
изначально в red - все вершины кроме start,
green - ни одной
yellow - точка старт, расстояние до которой 0. (кодируется как {start: 0}) где ключ - номер
    и вершины и значение - минимальное расстояние

Пока желтое не пустое:
    берем вершину now из множества желтых (любую) и ее расстояние now_distance
    закидываем в зеленый (1)
    удаляем из желтого

    Проход от 0 до n:       # проход по всем вершиным для выявление соседей
        если вершина i соседствует с now и не зеленая:  (2)
            находим расстояние от now до i. назовем его lenn.
            тогда можно предположить минимальное расстояние от start до i (через точку now)
            которое будет равно lenn + new_distance. назовем его possible_fastest (3)

            если i желтая и possible_fastest меньше его значения в желтом: (4)
                обновляем значение i в желтом на possible_fastest
            если i еще нет в желтом:  (5)
                записываем в желтый
                удаляем из красного'''
