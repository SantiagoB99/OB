public class Main {
    public static void main(String[] args) {

        Cliente cliente = new Cliente(23, "Jorge", 123456789, 500);
        System.out.println("El cliente tiene "+cliente.getEdad()+", se llama "+cliente.getNombre()+" su numero es: "+cliente.getTelefono()+" y su credito es "+cliente.getCredito());
        Trabajador trabajador = new Trabajador(50, "Pablo", 12348591, 2000);
        System.out.println("El trabajador tiene "+trabajador.getEdad()+" años, se llama"+trabajador.getNombre()+"su numero es: "+trabajador.getTelefono()+" y su salario es "+trabajador.getSalario());

    }

}


class Persona{
    //Atributos
    private int edad;
    private String nombre;
    private int telefono;

    //Constructor
    public Persona(int edad, String nombre, int telefono) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    //Gets y sets
    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
}

class Cliente extends Persona {
    //Atributos
    private int credito;

    //Constructor
    public Cliente(int edad, String nombre, int telefono, int credito) {
        super(edad, nombre, telefono);
        this.credito = credito;
    }

    //Gets y sets
    public int getCredito() {
        return credito;
    }

    public void setCredito(int credito) {
        this.credito = credito;
    }
}
    class Trabajador extends Persona {
        //Atributos
        private int salario;

        //Constructor
        public Trabajador(int edad, String nombre, int telefono, int salario) {
            super(edad, nombre, telefono);
            this.salario = salario;
        }

        //Gets y sets


        public int getSalario() {
            return salario;
        }

        public void setSalario(int salario) {
            this.salario = salario;
        }
    }
