public class Main {
    public static void main(String[] args) {
        Persona miPersona = new Persona();
        miPersona.setEdad(23);
        miPersona.setNombre("Santiago");
        miPersona.setTelefono(123456789);
        System.out.println("El nombre es "+miPersona.getNombre()+ " tiene "+ miPersona.getEdad() + " años y su numero es "+miPersona.getTelefono());
    }


}

class Persona{
    private int edad;
    private String nombre;
    private int telefono;

    public int getEdad() {
        return edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
}