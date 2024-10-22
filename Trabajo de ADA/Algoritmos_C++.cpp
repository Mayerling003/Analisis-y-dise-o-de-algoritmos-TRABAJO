#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <chrono>
using namespace std;

typedef void (*Sorteo)(int[], int);
void Bubble_sort(int array[], int size);
void Counting_sort(int array[],int size);
void heap_sort(int array[],int size);
void heapify(int array[],int n,int i);
void insertion_sort(int array[], int size);
void merge_sort(int array[], int size);
void merge(int array[], int left[], int leftSize, int right[], int rightSize);
void quickSort(int array[],int size);
void quickSort(int array[], int low, int high);
void selectionSort(int array[], int size);
int partition(int array[], int low, int high);

void imprimir(double tiempos[][21], int filas,int columnas);
int* LeerArchivo(int rango);

int main(){
	int testing[]={100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    const int cant_testing=sizeof(testing)/sizeof(testing[0]);
    double tiempos[7][21];

	Sorteo sortingMethods[] = {
        Bubble_sort,
        Counting_sort,
        heap_sort,
        insertion_sort,
        merge_sort,
        quickSort,
        selectionSort
    };
    int cant_metodos=sizeof(sortingMethods)/sizeof(sortingMethods[0]);

	for (int i=0;i<cant_testing;++i) {
        int* numeros=LeerArchivo(testing[i]);
        if(numeros==nullptr){
            cerr<<"Error al leer el archivo del tamaño: "<<testing[i]<<endl;
            continue;
        }
        for (int j=0;j<7;++j) {
            int* numeros_copia=new int[testing[i]];
            memcpy(numeros_copia, numeros, testing[i]*sizeof(int));
            auto start=chrono::high_resolution_clock::now();
            sortingMethods[j](numeros_copia, testing[i]);
            auto end=chrono::high_resolution_clock::now();
            chrono::duration<double> duration=end-start;
            tiempos[j][i]=duration.count();
            delete[] numeros_copia;
        }
        delete[] numeros;  // Liberamos la memoria del arreglo original
    }
	imprimir(tiempos,cant_metodos,cant_testing);

	return 0;	
}
//1. Bubble sort
void Bubble_sort(int array[], int size){	
	bool cambio;
	for(int i=0;i<size-1;i++){
		cambio=false;
		for(int j=0;j<size-1-i;j++){
			if(array[j]>array[j+1]){
				int aux=array[j];
				array[j]=array[j+1];
				array[j+1]=aux;
				cambio=true;
			}
		}
		if(!cambio) break;
	}
}
//2. Counting sort
void Counting_sort(int array[], int size){
    int max=array[0],min=array[0],range;
    for(int i=0;i<size;i++){
        if(array[i]>max){
            max=array[i];
        }
        if(array[i]<min){
            min=array[i];
        }
    }
    range=max-min+1;
    int conteo[range]={0};
    int salida[size];

    for(int i=0;i<size;i++){
        conteo[array[i]-min]++;
    }
    for(int i=1;i<range;i++){
        conteo[i]+=conteo[i-1];
    }
    for(int i=size-1;i>=0;i--){
        salida[conteo[array[i]-min]-1]=array[i];
        conteo[array[i]-min]--;
    }
    for(int i=0;i<size;i++){
        array[i]=salida[i];
    }
    
}
//3. Heap sort
void heap_sort(int array[],int size){
    int n=size;
    for(int i=n/2-1;i>=0;i--) {
            heapify(array,n,i);
        }

    for (int i=n-1;i>0;i--) {
        int aux=array[0];
        array[0]=array[i];
        array[i]=aux;
        heapify(array, i, 0);
    }
}
void heapify(int array[],int n,int i){
    int indice_mayor= i;
    int hijo_izquierdo=2*i+1;
    int hijo_derecho=2*i+2;

    if (hijo_izquierdo<n && array[hijo_izquierdo]>array[indice_mayor]) {
        indice_mayor=hijo_izquierdo;
    }
    if (hijo_derecho<n && array[hijo_derecho] > array[indice_mayor]) {
        indice_mayor=hijo_derecho;
    }

    if (indice_mayor!=i) {
        int aux=array[i];
        array[i]=array[indice_mayor];
        array[indice_mayor]=aux;
        heapify(array, n, indice_mayor);
    }
}
//4. Insertion sort
void insertion_sort(int array[], int size){
    for (int i=0;i<size;i++) {
        int pos=i;
        int aux=array[i];
            
        while((pos>0 && (array[pos-1]>aux))){
            array[pos]=array[pos-1];
            pos--;
        }
        array[pos]=aux;
    }
}
//5. Merge sort
void merge_sort(int array[], int size){
    if (size< 2) {
        return;
    }
    int mid=size/2;
    int* left=new int[mid];
    int* right=new int[size-mid];

    for (int i=0;i<mid;i++) {
        left[i]=array[i];
    }

    for (int i=mid;i<size;i++) {
        right[i-mid]=array[i];
    }

    merge_sort(left,mid);
    merge_sort(right,size-mid);

    merge(array,left,mid,right,size-mid);
    delete[] left;
    delete[] right;
}
void merge(int array[], int left[], int leftSize, int right[], int rightSize) {
    int i=0,j=0,k=0;

    while(i<leftSize && j<rightSize){
        if(left[i]<=right[j]) {
            array[k++]=left[i++];
        }else{
            array[k++]=right[j++];
        }
    }
    while (i<leftSize) {
        array[k++]=left[i++];
    }

    while (j<rightSize) {
        array[k++]=right[j++];
    }
}
//6. Quick sort
void quickSort(int array[],int size){
    quickSort(array,0,size-1);
}
void quickSort(int array[],int low,int high){
    if(low<high){
        int partitionIndex=partition(array,low,high);
        quickSort(array,low, partitionIndex-1);
        quickSort(array,partitionIndex+1, high);
    }
}
int partition(int array[], int low, int high){
    int pivot=array[high];
    int i=low-1;

    for (int j=low;j<high;j++){
        if(array[j]<=pivot) {
            i++;
            swap(array[i],array[j]);
        }
    }

    swap(array[i+1],array[high]);
    return i+1;
}
//7. Selection sort
void selectionSort(int array[], int size){
    for(int i=0;i<size-1;i++){
        int minIndex=i;
        for(int j=i+1;j<size;j++){
            if(array[j]<array[minIndex]){
                minIndex=j;
            }
        }
        swap(array[i],array[minIndex]);
    }
}
//Imprimir la matriz de tiempos
void imprimir(double tiempos[][21], int filas,int columnas){
	for(int i=0;i<filas;i++){
		for(int j=0;j<columnas;j++){
			cout<<tiempos[i][j]<<" ";
		}
		cout<<endl;
	}
}
int* LeerArchivo(int rango) {
	string ruta="C:/Users/User/Documents/Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main/Trabajo de ADA/Crear_numeros/"+to_string(rango) + ".txt";
    ifstream archivo(ruta);
    if (!archivo.is_open()){
        cerr<<"Error al abrir el archivo: "<<ruta<<endl;
        return nullptr;
    }
    int* numeros=new int[rango];
	string linea;
    int i=0;
    while(getline(archivo, linea) && i<rango) {
        istringstream iss(linea);
        int numero;
        while (iss>>numero && i<rango){
            numeros[i]=numero;
            i++;
        }
    }

    archivo.close();
    return numeros;
}
