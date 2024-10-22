package algoritmos;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class algoritmo{
    @FunctionalInterface
    interface SortingMethod {
        void sort(int[] array);
    }
    public static void main(String[] args){
        int []testing={100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000};
        double[][] tiempos=new double[7][21];
   
        SortingMethod[] sortingMethods = new SortingMethod[]{
            algoritmo::bubblesort,
            algoritmo::countingsort,
            algoritmo::heap_sort,
            algoritmo::insertion_sort,
            algoritmo::merge_sort,
            algoritmo::quickSort,
            algoritmo::selectionSort, 
        };
        
        for(int i=0;i<testing.length;i++){
            int[] numeros=LeerArchivo(testing[i]);
            for(int j=0;j<sortingMethods.length;j++){
                int[] numeros_copia=Arrays.copyOf(numeros,numeros.length);
                long startTime=System.nanoTime();
                sortingMethods[j].sort(numeros_copia);
                long endTime=System.nanoTime();
                long duration=endTime-startTime;
                tiempos[j][i]=duration/1_000_000_000.0;
            }
        }
        imprimir(tiempos);
    }
    //algoritmos sort
    //1. bubble sort
    public static void bubblesort(int[]array){
        int size=array.length;
        boolean cambio;
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
    //2. counting sort
    public static void countingsort(int[] array){
        int max=array[0],min=array[0],range;
        for(int i=0;i<array.length;i++){
            if(array[i]>max){
            max=array[i];
            }
            if(array[i]<min){
            min=array[i];
            }
        }
        
        range=max-min+1;
        int[] conteo=new int[range];
        int[] salida=new int[array.length];
        for(int i=0;i<array.length;i++){
            conteo[array[i]-min]++;
        }
        for(int i=1;i<range;i++){
            conteo[i]+=conteo[i-1];
        }
        for(int i=array.length-1;i>=0;i--){
            salida[conteo[array[i]-min]-1]=array[i];
            conteo[array[i]-min]--;
        }
        for(int i=0;i<array.length;i++){
            array[i]=salida[i];
        }
        
    }
    //3. heap sort
    public static void heap_sort(int [] array){
        int n = array.length;

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
    private static void heapify(int[] array, int n, int i) {
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
    //4. insertion sort
    public static void insertion_sort(int[] array){
        for (int i=0;i<array.length;i++) {
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
    public static void merge_sort(int[] array){
        if(array.length < 2){
            return;
        }
        int mid=array.length / 2;
        int[] left=Arrays.copyOfRange(array, 0, mid);
        int[] right=Arrays.copyOfRange(array, mid, array.length);

        merge_sort(left);
        merge_sort(right);

        merge(array, left, right);
    }
    private static void merge(int[] arr, int[] left, int[] right) {
        int i=0,j=0,k=0;

        while (i<left.length && j<right.length) {
            if(left[i]<=right[j]) {
                arr[k++]=left[i++];
            }else{
                arr[k++]=right[j++];
            }
        }

        while (i<left.length) {
            arr[k++]=left[i++];
        }

        while (j<right.length) {
            arr[k++]=right[j++];
        }
    }
    //6. Quick sort
    public static void quickSort(int[] array){
        quickSort(array,0,array.length-1);
    }
    public static void quickSort(int[] array, int low, int high) {
        if(low<high){
            int partitionIndex=partition(array, low, high);
            quickSort(array, low, partitionIndex - 1);
            quickSort(array, partitionIndex + 1, high);
        }
    }
    private static int partition(int[] array, int low, int high) {
        int pivot=array[high];
        int i=(low-1);

        for(int j=low;j<high;j++){
            if(array[j]<=pivot){
                i++;
                int aux=array[i];
                array[i]=array[j];
                array[j]=aux;
            }
        }
        int temp=array[i+1];
        array[i+1]=array[high];
        array[high]=temp;

        return i+1;
    }
    //7. Selection sort
    public static void selectionSort(int[] array) {
        int n=array.length;

        for(int i=0;i<n-1;i++){
            int minIndex=i;
            for(int j=i+1;j<n;j++){
                if(array[j]<array[minIndex]){
                    minIndex=j;
                }
            }

            int temp=array[minIndex];
            array[minIndex]=array[i];
            array[i]=temp;
        }
    }
    //leer archivos .txt
    public static int[] LeerArchivo(int rango) {
        String ruta="C:\\Users\\User\\Documents\\Trabajo-de-Analisis-de-Dise-o-de-Algoritmos-main\\Trabajo de ADA\\Crear_numeros\\src\\crear_numeros"+"\\"+String.valueOf(rango)+".txt";
        int [] numeros=new int[rango];
        try (BufferedReader br=new BufferedReader(new FileReader(ruta))) {
            String linea;
            int i=0;
            while((linea=br.readLine())!=null && i<rango) {
                String[] numerosComoString=linea.split(" ");
                for(String numStr : numerosComoString){
                    if(i<rango) {
                        numeros[i] = Integer.parseInt(numStr);
                        i++;
                    }
                }
            }
        } catch(IOException e) {
            e.printStackTrace();
        }
        return numeros;
    }
    //imprimir matriz de tiempos
    public static void imprimir(double[][] array){
        for(int i = 0; i <array.length; i++){
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j]);
                if(j<array[0].length-1){
                    System.out.print(",");
                }
            }
            System.out.println();
        }       
    }
}
