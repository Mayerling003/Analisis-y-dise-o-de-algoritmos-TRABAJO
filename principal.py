import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np

#funcion para recuperar la matriz de tiempos de Java

"""
def Recuperar_tiempos_Java():
    ruta_archivojava="C:/Users/User/Documents/Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main/Trabajo de ADA/Algoritmos_Java/src/algoritmos"

    if os.path.exists(ruta_archivojava):
        compilar=subprocess.run(["javac", ruta_archivojava])
        if compilar.returncode==0:
            nombre_clase="algoritmos.algoritmo"
            ejecutar=subprocess.run(["java", nombre_clase],capture_output=True,text=True,cwd="C:/Users/User/Documents/Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main/Trabajo de ADA/Algoritmos_Java/src")
            resultado=ejecutar.stdout.strip().splitlines()
            resultados_java=[]
            for linea in resultado:
                fila_tiempos=[float(valor) for valor in linea.split(",")]
                resultados_java.append(fila_tiempos)

            if len(resultados_java)==7 and all(len(fila)==21 for fila in resultados_java):
                return resultados_java
            else:
                print("Tamaño incorrecto")
                    
        else:
            print("Error al compilar")
    else:
        print(f"Archivo {ruta_archivojava} no encontrado.")
    
    return None
def Recuperar_tiempos_Cpp():
    ruta_archivocpp="C:/Users/User/Documents/Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main/Trabajo de ADA/Algoritmos_C++.cpp"
    ruta_exe="D:/gersael/Trabajo de ADA/Algoritmos_C++.exe"

    if os.path.exists(ruta_archivocpp):
        compilar=subprocess.run(["g++", ruta_archivocpp,"-o",ruta_exe])
        if compilar.returncode==0:
            ejecutar=subprocess.run([ruta_exe],capture_output=True,text=True)
            resultado=ejecutar.stdout.strip().splitlines()
            resultados_cpp=[]
            for linea in resultado:
                fila_tiempos=[float(valor) for valor in linea.split()]
                resultados_cpp.append(fila_tiempos)

            if len(resultados_cpp)==7 and all(len(fila)==21 for fila in resultados_cpp):
                return resultados_cpp
            else:
                print("Tamaño incorrecto")
                    
        else:
            print("Error al compilar")
    else:
        print(f"Archivono {ruta_archivocpp} encontrado.")
    
    return None
def Recuperar_tiempos_Python():
    ruta_archivo_python = "C:/Users/User/Documents/Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main/Trabajo de ADA/Algoritmos_python.py"  # Cambia a la ruta real
    
    if os.path.exists(ruta_archivo_python):
        ejecutar=subprocess.run(["python", ruta_archivo_python],capture_output=True,text=True
        )
        resultado = ejecutar.stdout.strip().splitlines()
        resultados_python = []
        for linea in resultado:
            fila_tiempos = [float(valor) for valor in linea.replace('[','').replace(']','').split()]
            resultados_python.append(fila_tiempos)
        if len(resultados_python) == 7 and all(len(fila) == 21 for fila in resultados_python):
            return resultados_python
        else:
            print("Tamaño incorrecto")
    else:
        print(f"Archivo {ruta_archivo_python} no encontrado.")
    
    return None
"""

#crear grafico de Java
matrices_algoritmo=[]
resultado_java=[
    [1.926E-4,0.0029181,0.00134,0.0037905,0.0083703,0.014875,0.0232991,0.039013,0.0488532,0.068958,0.0939672,0.1366736,0.5046406,1.1821146,2.186768,3.6180897,5.2856686,7.0808021,9.4983839,13.1845632,14.6187165],
    [3.32E-5,6.94E-5,1.667E-4,2.08E-4,2.991E-4,4.398E-4,5.557E-4,5.017E-4,2.289E-4,3.255E-4,3.128E-4,6.5E-5,1.055E-4,1.685E-4,1.538E-4,3.755E-4,3.009E-4,3.398E-4,3.236E-4,4.303E-4,5.327E-4],
    [8.3E-5,8.66E-5,2.601E-4,3.461E-4,4.564E-4,5.927E-4,7.328E-4,0.0011069,0.0011212,0.0013247,0.0020469,9.377E-4,0.0018774,0.0029283,0.0038996,0.0060373,0.0061328,0.0069722,0.0082847,0.0095465,0.012132],
    [7.14E-5,0.0019199,9.396E-4,3.738E-4,6.702E-4,0.0011884,0.001851,0.003487,0.0036536,0.0051357,0.0113415,0.007325,0.0293456,0.064366,0.1176024,0.2306302,0.2729781,0.3796075,0.5345576,0.6428879,0.7401669],
    [9.05E-5,6.842E-4,2.195E-4,3.59E-4,5.343E-4,6.48E-4,7.899E-4,0.0010909,0.0014349,0.0015195,0.0020498,0.0016885,0.0032647,0.0074661,0.0049341,0.0061565,0.0095191,0.0116336,0.0098239,0.0132144,0.0157106],
    [3.42E-5,2.672E-4,8.4E-5,1.402E-4,1.874E-4,2.457E-4,2.801E-4,3.37E-4,3.944E-4,4.96E-4,7.17E-4,6.448E-4,0.0012802,0.0022659,0.0030313,0.0046466,0.0052851,0.0069874,0.0080287,0.0116129,0.011736],
    [1.03E-4,0.0014339,0.0013608,0.0018994,0.0020245,0.0035427,0.0054213,0.0077961,0.0106056,0.0182019,0.0240185,0.0261308,0.0899276,0.194011,0.4344218,0.580124,0.8213969,1.1154939,1.5438871,1.9072015,2.2256126]
]
resultado_cpp=[
    [0, 0.001, 0.003001, 0.013012, 0.026011, 0.04902, 0.080032, 0.120058, 0.179071, 0.207082, 0.259103, 0.322137, 1.37855, 3.18627, 5.92837, 9.02082, 12.9748, 17.3905, 22.7836, 29.2441, 36.4314], 
    [0, 0, 0, 0, 0, 0, 0, 0.000992, 0, 0, 0, 0.001001, 0, 0.001009, 0.001, 0.001009, 0.001, 0.001001, 0.002, 0.001999, 0.002001], 
    [0, 0, 0, 0, 0.001001, 0.001225, 0.001001, 0.001001, 0.002003, 0.002001, 0.002001, 0.002, 0.004001, 0.005994, 0.009003, 0.011996, 0.014013, 0.020007, 0.020007, 0.022, 0.026008], 
    [0, 0, 0, 0.003001, 0.006002, 0.01078, 0.018007, 0.026017, 0.035019, 0.043023, 0.058029, 0.072026, 0.2851, 0.625218, 1.15243, 1.79363, 2.57989, 3.52423, 6.69185, 5.84455, 9.50609], 
    [0, 0, 0.001, 0, 0.001, 0.001, 0.001, 0.000991, 0.002992, 0.002001, 0.002992, 0.003001, 0.005993, 0.009013, 0.012004, 0.016006, 0.018006, 0.021017, 0.024146, 0.029019, 0.03301], 
    [0, 0, 0, 0.001, 0, 0.000992, 0.001, 0.001001, 0.001001, 0.001, 0.002, 0.002001, 0.005011, 0.007995, 0.012996, 0.021007, 0.030011, 0.031002, 0.049889, 0.049007, 0.059019],
    [0, 0, 0.001001, 0.004002, 0.011004, 0.018007, 0.033012, 0.042014, 0.064022, 0.075035, 0.094042, 0.11504, 0.455151, 1.04437, 1.81314, 2.84601, 4.11795, 5.66192, 7.48561, 9.5204, 11.7322]
]
resultado_python=[
    [0.00000000e+00, 1.56257153e-02, 4.69267368e-02, 2.30518103e-01,
    5.01944542e-01, 9.05662537e-01, 1.38176894e+00, 1.99803042e+00,
    2.70447922e+00, 3.52774048e+00, 4.54441500e+00, 5.73008585e+00,
    2.21260002e+01, 5.17758090e+01, 8.89954815e+01, 1.43525966e+02,
    1.98997158e+02, 2.80856373e+02, 3.56218605e+02, 4.50912164e+02,
    5.55684031e+02],
    [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 9.98258591e-04,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    1.56240463e-02, 1.56219006e-02, 1.56280994e-02, 1.56228542e-02,
    3.12445164e-02, 1.56772137e-02, 2.39198208e-02, 2.69045830e-02,
    3.08969021e-02],
    [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 5.97953796e-03,
    0.00000000e+00, 1.56233311e-02, 1.80084705e-02, 3.12466621e-02,
    3.12292576e-02, 1.56230927e-02, 3.55217457e-02, 3.12469006e-02,
    9.31251049e-02, 1.25024557e-01, 1.71806574e-01, 2.19347239e-01,
    2.90744543e-01, 3.12468529e-01, 3.83722067e-01, 4.83337402e-01,
    4.89367723e-01],
    [0.00000000e+00, 0.00000000e+00, 1.56297684e-02, 1.02324486e-01,
    2.49690294e-01, 4.55706596e-01, 6.90638304e-01, 9.99198437e-01,
    1.36985087e+00, 1.76438975e+00, 2.26423597e+00, 2.82991290e+00,
    1.12059011e+01, 2.53226099e+01, 4.54007187e+01, 7.09822209e+01,
    1.04037443e+02, 1.38776112e+02, 1.82618368e+02, 2.28714460e+02,
    2.83626488e+02],
    [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    1.56242847e-02, 0.00000000e+00, 0.00000000e+00, 1.56216621e-02,
    1.56238079e-02, 3.21872234e-02, 3.12447548e-02, 3.12471390e-02,
    4.68714237e-02, 7.81240463e-02, 1.24988317e-01, 1.40601397e-01,
    1.71808720e-01, 2.11305141e-01, 2.42140293e-01, 2.74088144e-01,
    3.07026863e-01],
    [0.00000000e+00, 0.00000000e+00, 1.56173706e-02, 1.56238079e-02,
    0.00000000e+00, 1.56321526e-02, 1.63121223e-02, 1.56230927e-02,
    1.15544796e-02, 1.56230927e-02, 1.56235695e-02, 1.56238079e-02,
    4.68819141e-02, 9.36980247e-02, 1.41101837e-01, 1.80535793e-01,
    2.52150536e-01, 2.95016289e-01, 3.79733562e-01, 4.54482317e-01,
    5.64116478e-01],
    [1.56655312e-02, 1.56219006e-02, 1.56202316e-02, 7.81700611e-02,
    1.87481642e-01, 3.08452368e-01, 4.97750044e-01, 7.31855392e-01,
    9.54062700e-01, 1.26771402e+00, 1.58076668e+00, 1.96320724e+00,
    7.86725283e+00, 1.77597535e+01, 3.17364285e+01, 4.91117587e+01,
    7.18987072e+01, 9.72151854e+01, 1.26917149e+02, 1.59406486e+02,
    1.99318351e+02]
]

matrices_algoritmo.append(("Java",resultado_java))
matrices_algoritmo.append(("C++",resultado_cpp))
matrices_algoritmo.append(("Python",resultado_python))
print(matrices_algoritmo)
n_elementos=np.array([100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000])
for lengua,matriz in matrices_algoritmo:    
    tiempo_bubble=np.array(matriz[0]) 
    tiempo_counting=np.array(matriz[1])
    tiempo_heap=np.array(matriz[2])
    tiempo_insertion=np.array(matriz[3])
    tiempo_merge=np.array(matriz[4])
    tiempo_quick=np.array(matriz[5])
    tiempo_selection=np.array(matriz[6])


    indices = np.arange(len(n_elementos))
    plt.figure()
    plt.plot(indices, tiempo_bubble, label='Bubble sort', color='red', linewidth=2)
    plt.plot(indices, tiempo_counting, label='Counting sort', color='purple', linewidth=2)
    plt.plot(indices, tiempo_heap, label='Heap sort', color='yellow', linewidth=2)
    plt.plot(indices, tiempo_insertion, label='Insertion sort', color='green', linewidth=2)
    plt.plot(indices, tiempo_merge, label='Merge sort', color='Turquoise', linewidth=2)
    plt.plot(indices, tiempo_quick, label='Quick sort', color='Sky blue', linewidth=2)
    plt.plot(indices, tiempo_selection, label='Selection sort', color='pink', linewidth=2)

    plt.xlabel('Número de elementos', fontsize=10)
    plt.ylabel('Tiempo de ejecución (s)', fontsize=10)
    plt.title(f'Comparacion de los algoritmos de ordenamiento en {lengua}', fontsize=12)

    plt.xticks(indices, n_elementos, rotation=45)

    plt.legend(loc='best', fontsize=10)

    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)

    plt.tight_layout()
    plt.show()

def graficar_tiempos(algoritmos, resultados, n_elementos):
    # Asegúrate de que resultados tenga la forma adecuada (lenguajes x algoritmos x n_elementos)
    for i, algoritmo in enumerate(algoritmos):
        plt.figure()
        for j, (resultado, nombre_lenguaje) in enumerate(resultados):
            tiempos = np.array(resultado[i])  # Asegúrate de obtener el tiempo para el algoritmo i
            # Verifica que la longitud de tiempos coincida con n_elementos
            if len(tiempos) != len(n_elementos):
                print(f"Warning: La longitud de los tiempos para {nombre_lenguaje} con {algoritmo} no coincide con n_elementos.")
                continue
            
            plt.plot(np.arange(len(n_elementos)), tiempos, label=nombre_lenguaje, linewidth=2)

        plt.xlabel('Número de elementos', fontsize=10)
        plt.ylabel('Tiempo de ejecución (s)', fontsize=10)
        plt.title(f'Tiempos de ejecución de {algoritmo}', fontsize=12)

        plt.xticks(np.arange(len(n_elementos)), n_elementos, rotation=45)
        plt.legend(loc='best', fontsize=10)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.tight_layout()
        plt.show()

algoritmos = [
    'Bubble Sort',
    'Counting Sort',
    'Heap Sort',
    'Insertion Sort',
    'Merge Sort',
    'Quick Sort',
    'Selection Sort'
]

resultados = [
    [resultado_java, "Java"],
    [resultado_cpp, "C++"],
    [resultado_python, "Python"]
]
n_elementos=np.array([100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000])
graficar_tiempos(algoritmos, resultados, n_elementos)