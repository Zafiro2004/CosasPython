import java.util.Scanner;

public class Nombre {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Introduce tu nombre: ");
        String nombre = entrada.nextLine();

        System.out.print("Introduce tu primer apellido: ");
        String apellido1 = entrada.nextLine();

        System.out.print("Introduce tu segundo apellido: ");
        String apellido2 = entrada.nextLine();

        System.out.println("Hola " + nombre + " " + apellido1 + " " + apellido2 + "!");

        entrada.close();
    }
}

