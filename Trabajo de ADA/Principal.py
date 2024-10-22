import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np

#funcion para recuperar la matriz de tiempos de Java

"""
def Recuperar_tiempos_Java():
    ruta_archivojava="D:/gersael/Trabajo de ADA/Algoritmos_Java/src/algoritmos/algoritmo.java"

    if os.path.exists(ruta_archivojava):
        compilar=subprocess.run(["javac", ruta_archivojava])
        if compilar.returncode==0:
            nombre_clase="algoritmos.algoritmo"
            ejecutar=subprocess.run(["java", nombre_clase],capture_output=True,text=True,cwd="D:/gersael/Trabajo de ADA/Algoritmos_Java/src")
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
    ruta_archivocpp="D:/gersael/Trabajo de ADA/Algoritmos_C++.cpp"
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
    ruta_archivo_python = "D:/gersael/Trabajo de ADA/Algoritmos_python.py"  # Cambia a la ruta real
    
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
    [1.938E-4,0.0052466,0.0019102,0.0033435,0.00756,0.0182686,0.0310904,0.0458611,0.1694462,0.1456742,0.1068609,0.1218712,0.5882881,1.4120705,2.5066909,3.910809,5.7167568,7.9613456,10.2269335,13.0583245,16.5934335],
    [4.82E-5,8.28E-5,1.477E-4,2.535E-4,3.389E-4,4.952E-4,6.049E-4,8.997E-4,2.599E-4,2.325E-4,1.926E-4,4.95E-5,8.25E-5,8.38E-5,1.596E-4,1.926E-4,1.847E-4,2.166E-4,3.147E-4,3.576E-4,2.908E-4],
    [9.82E-5,1.252E-4,7.215E-4,6.04E-4,0.0034017,7.469E-4,8.62E-4,0.0010608,0.0013233,0.0020899,0.0015766,0.0010235,0.0026338,0.0032856,0.0044329,0.0055629,0.0068137,0.0079103,0.0145751,0.0111748,0.0122198],
    [7.51E-5,0.0017098,0.004813,7.13E-4,0.0014505,0.0025567,0.0034699,0.0037654,0.0065304,0.0113495,0.0098525,0.0072307,0.032786,0.0744814,0.1276205,0.2018817,0.2802187,0.3742836,0.5036482,0.626857,0.7833399],
    [1.069E-4,5.449E-4,2.937E-4,4.328E-4,0.004513,7.808E-4,9.918E-4,0.0011652,0.0012765,0.0013764,0.0044043,0.0012917,0.0023942,0.003163,0.0050708,0.008667,0.0071439,0.0082791,0.0116453,0.0117112,0.0115384],
    [3.51E-5,2.494E-4,1.501E-4,2.499E-4,0.0011097,3.412E-4,0.0010325,0.0013077,5.49E-4,5.915E-4,7.253E-4,5.945E-4,0.0012494,0.0020551,0.002999,0.0042619,0.0052183,0.0083029,0.0077096,0.0185676,0.013429],
    [1.032E-4,0.0017503,9.688E-4,0.0019033,0.003021,0.005599,0.0119343,0.0378161,0.0227534,0.0313945,0.0273526,0.0260107,0.1040738,0.2458172,0.4537899,0.6387729,0.9261224,1.2553659,1.6705828,2.1714559,2.5882197]
]
resultado_cpp=[
    [5.1e-05, 0.000895, 0.001999, 0.006897, 0.015624, 0.027715, 0.048263, 0.06145, 0.093108, 0.116891, 0.145785, 0.205865, 1.07046, 3.035, 6.08519, 7.34785, 10.788, 16.4769, 20.0166, 27.4799, 35.105], 
    [1e-05, 1.7e-05, 1.6e-05, 3.3e-05, 4.8e-05, 7e-05, 9.4e-05, 8.1e-05, 0.000131, 0.000101, 0.000112, 0.000134, 0.000335, 0.000574, 0.000507, 0.00059, 0.000699, 0.001071, 0.000945, 0.001399, 0.00118], 
    [2.3e-05, 0.000101, 0.000147, 0.000261, 0.00039, 0.000724, 0.001113, 0.000846, 0.001946, 0.001149, 0.001435, 0.001737, 0.004005, 0.005924, 0.007463, 0.011972, 0.011844, 0.024467, 0.01628, 0.026597, 0.029002], 
    [1.7e-05, 0.000343, 0.000756, 0.002736, 0.006325, 0.010934, 0.023192, 0.023856, 0.035036, 0.042897, 0.056109, 0.067696, 0.291069, 0.681393, 1.1476, 1.75028, 2.71887, 3.94584, 4.33925, 5.84094, 7.63002], 
    [0.000692, 0.002457, 0.004415, 0.012983, 0.021476, 0.034222, 0.070327, 0.054044, 0.024959, 0.014907, 0.242166, 0.204689, 1.39013, 0.834906, 3.03014, 0.08031, 2.35224, 15.8345, 0.098109, 14.9677, 10.8174], 
    [1.5e-05, 6.9e-05, 0.000108, 0.000223, 0.000353, 0.000486, 0.00089, 0.000806, 0.00092, 0.001127, 0.002709, 0.00148, 0.003437, 0.006382, 0.010957, 0.014118, 0.019319, 0.024315, 0.034413, 0.0353, 0.045908],
    [3.6e-05, 0.000503, 0.001355, 0.005289, 0.012503, 0.021077, 0.035123, 0.048005, 0.073991, 0.084943, 0.112187, 0.137571, 0.581428, 1.46434, 2.50922, 3.33035, 5.9876, 6.9184, 8.58591, 12.8355, 14.7765]
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
    plt.plot(indices, tiempo_bubble, label='Bubble sort', color='blue', linewidth=2)
    plt.plot(indices, tiempo_counting, label='Counting sort', color='orange', linewidth=2)
    plt.plot(indices, tiempo_heap, label='Heap sort', color='purple', linewidth=2)
    plt.plot(indices, tiempo_insertion, label='Insertion sort', color='green', linewidth=2)
    plt.plot(indices, tiempo_merge, label='Merge sort', color='red', linewidth=2)
    plt.plot(indices, tiempo_quick, label='Quick sort', color='brown', linewidth=2)
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