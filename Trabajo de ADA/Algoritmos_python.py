import time
import copy
import numpy as np
def bubblesort(array):
    size=len(array)
    cambio=False

    for i in range(size-1):
        cambio=False

        for j in range(size-1-i):
            if array[j]>array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                cambio=True

        if not cambio:
            break
def counting_sort(array):
    mx=max(array)
    mn=min(array)
    rng=mx-mn+1
    conteo=[0]*rng
    salida=[0]*len(array)
    for i in range(len(array)):
        conteo[array[i]-mn]+=1
    
    for i in range(1,rng):
        conteo[i]+=conteo[i-1]

    for i in range(len(array)-1,-1,-1):
        salida[conteo[array[i]-mn]-1]=array[i]
        conteo[array[i]-mn]-=1

    for i in range(len(array)):
        array[i]=salida[i]
def heap_sort(array):
    n=len(array)
    for i in range(n//2-1,-1,-1):
        heapify(array,n,i)
    
    for i in range(n-1,0,-1):
        aux=array[0]
        array[0]=array[i]
        array[i]=aux
        heapify(array, i, 0)
def heapify(array,n,i):
    indice_mayor=i
    hijo_derecho=2*i+1
    hijo_izquierdo=2*i+2
    if hijo_izquierdo<n and array[hijo_izquierdo]>array[indice_mayor]:
        indice_mayor=hijo_izquierdo
    
    if hijo_derecho<n and array[hijo_derecho] > array[indice_mayor]:
        indice_mayor=hijo_derecho
    
    if  indice_mayor!=i:
        aux=array[i]
        array[i]=array[indice_mayor]
        array[indice_mayor]=aux
        heapify(array, n, indice_mayor)
def insertion_sort(array):
    for i in range(len(array)):
        pos=i
        aux=array[i]

        while pos>0 and array[pos-1]>aux:
            array[pos]=array[pos-1]
            pos-=1
        array[pos]=aux
def merge_sort(array):
    if len(array)<2:
        return array
    mid=len(array)//2
    left=merge_sort(array[:mid])
    right=merge_sort(array[mid:]) 

    return merge(left, right)
def merge(left, right):
    merged=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def quick_sort(array):
    if len(array) < 2:
        return array

    pivot=array[-1]
    left=[]
    right=[]

    for i in range(len(array) - 1):
        if array[i]<=pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    return quick_sort(left)+[pivot]+quick_sort(right)
def selection_sort(array):
    n=len(array)

    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index=j

        array[i],array[min_index]=array[min_index],array[i]
def leer_archivo(rango):
    ruta=f"C:/Users/User/Documents/Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main/Trabajo de ADA/Crear_numeros{rango}.txt"
    numeros=[]
    try:
        with open(ruta, 'r') as archivo:
            for linea in archivo:
                numeros_como_string=linea.split()
                for num_str in numeros_como_string:
                    if len(numeros)<rango:
                        numeros.append(int(num_str))
    except IOError as e:
        print(f"Error en el archivo: {ruta}")
        print(e)

    return numeros

testing=[100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
tiempos=np.zeros((7,len(testing)))

sorteo_metodos=[
    bubblesort,
    counting_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort
]

for i in range(len(testing)):
    numeros=leer_archivo(testing[i])
    for j in range (len(sorteo_metodos)):
        numeros_copia=copy.deepcopy(numeros)
        start_time=time.time()
        sorteo_metodos[j](numeros_copia)
        end_time=time.time()
        duracion=end_time-start_time
        tiempos[j][i]=duracion

print(tiempos)
