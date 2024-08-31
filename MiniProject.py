import java.util.Scanner;

class Student {
    int id;
    String name;
    Student next;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
        this.next = null;
    }
}

class StudentDatabase {
    private Student head;
    private int size;

    public StudentDatabase() {
        head = null;
        size = 0;
    }

    public void addStudent(int id, String name) {
        if (size >= 1000) {
            System.out.println("Database is full. Cannot add more students.");
            return;
        }

        Student newStudent = new Student(id, name);
        if (head == null) {
            head = newStudent;
        } else {
            Student current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newStudent;
        }
        size++;
        System.out.println("Student added successfully.");
    }

    public void displayAllStudents() {
        if (head == null) {
            System.out.println("No students in the database.");
            return;
        }

        Student current = head;
        while (current != null) {
            System.out.println("ID: " + current.id + ", Name: " + current.name);
            current = current.next;
        }
    }

    public void searchStudent(int id) {
        Student current = head;
        while (current != null) {
            if (current.id == id) {
                System.out.println("Student found - ID: " + current.id + ", Name: " + current.name);
                return;
            }
            current = current.next;
        }
        System.out.println("Student with ID " + id + " not found.");
    }
}

public class StudentDatabaseSystem {
    public static void main(String[] args) {
        StudentDatabase database = new StudentDatabase();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Student");
            System.out.println("2. Display All Students");
            System.out.println("3. Search Student by ID");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter student ID: ");
                    int id = scanner.nextInt();
                    scanner.nextLine(); // Consume newline
                    System.out.print("Enter student name: ");
                    String name = scanner.nextLine();
                    database.addStudent(id, name);
                    break;
                case 2:
                    database.displayAllStudents();
                    break;
                case 3:
                    System.out.print("Enter student ID to search: ");
                    int searchId = scanner.nextInt();
                    database.searchStudent(searchId);
                    break;
                case 4:
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}