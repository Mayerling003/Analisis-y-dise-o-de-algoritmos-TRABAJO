package crear_numeros;
import java.io.*;
import javax.swing.JOptionPane;
import java.util.Random;
public class crear_numeros {
    public static void main(String[] args){
        Random random=new Random();
        int []rangos={100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000};
        for(int i=0;i<21;i++){
            StringBuilder numeros=new StringBuilder();
            int cantidad=rangos[i];
            for(int j=0;j<cantidad;j++){
                numeros.append(random.nextInt(0,1000)).append(" ");
            }
            String nombre=String.valueOf(cantidad)+".txt";
            CrearArchivo(nombre, numeros.toString());
            
        }
    }
    private static void CrearArchivo(String nombre,String contenido ){
         try(BufferedWriter escribir=new BufferedWriter(new FileWriter(nombre))) {
            escribir.write(contenido);
            JOptionPane.showMessageDialog(null, "Se creo el Archivo",nombre, 0);
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(null, "No se pudo crear el Archivo", nombre,0);       
        }
    }
    public static int [] LeerArchivo(int rango) {
        String ruta="D:\\gersael\\ALGORITMOS\\Crear_numeros"+"\\"+String.valueOf(rango)+".txt";
        int [] numeros=new int[rango];
        try (BufferedReader br=new BufferedReader(new FileReader(ruta))) {
            String linea;
            int i=0;
            while((linea=br.readLine())!=null && i<rango) {
                String[] numerosComoString=linea.split(" ");
                for(String numStr : numerosComoString){
                    if(i<rango) { // Asegúrate de que i no exceda el rango
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
}
