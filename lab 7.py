// ComplexNumber Class
class ComplexNumber {
    private double real;
    private double imaginary;

    // Constructor to initialize the complex number
    public ComplexNumber(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    // Method to add another complex number and return the result
    public ComplexNumber add(ComplexNumber c) {
        double newReal = this.real + c.real;
        double newImaginary = this.imaginary + c.imaginary;
        return new ComplexNumber(newReal, newImaginary);
    }

    // Method to calculate the magnitude of the complex number
    public double magnitude() {
        return Math.sqrt(real * real + imaginary * imaginary);
    }

    // Method to display the complex number in "a + bi" format
    public String toString() {
        return real + " + " + imaginary + "i";
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {
        // Creating two ComplexNumber objects
        ComplexNumber c1 = new ComplexNumber(3, 4);
        ComplexNumber c2 = new ComplexNumber(1, 2);

        // Adding the two complex numbers
        ComplexNumber sum = c1.add(c2);

        // Displaying the results
        System.out.println("First Complex Number: " + c1);
        System.out.println("Second Complex Number: " + c2);
        System.out.println("Sum of Complex Numbers: " + sum);

        // Calculating and displaying magnitudes
        System.out.println("Magnitude of First Complex Number: " + c1.magnitude());
        System.out.println("Magnitude of Second Complex Number: " + c2.magnitude());
        System.out.println("Magnitude of Sum: " + sum.magnitude());
    }
}
