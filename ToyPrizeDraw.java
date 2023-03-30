import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class ToyPrizeDraw {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Toy> toys = new ArrayList<>();

        // Основное меню
        while (true) {
            System.out.println("1. Добавить игрушку");
            System.out.println("2. Изменить процент выпадения");
            System.out.println("3. Произвести розыгрыш");
            System.out.println("4. Выход");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Введите цифровой ID игрушки: ");
                    int id = 0;
                    if (scanner.hasNextInt()) {
                        id = scanner.nextInt();
                    } else {
                        System.out.println("Недопустимый ввод! Введите цифрами.");
                        scanner.next();
                        break;
                    }
            
                    System.out.print("Введите название игрушки: ");
                    String title = scanner.next();
            
                    int quantity = 0;
                    boolean validInput = false;
                    while (!validInput) {
                        System.out.print("Введите количество игрушек для розыгрыша: ");
                        if (scanner.hasNextInt()) {
                            quantity = scanner.nextInt();
                            validInput = true;
                        } else {
                            System.out.println("Недопустимый ввод! Введите цифрами.");
                            scanner.next();
                        }
                    }
            
                    double dropFrequency = 0;
                    validInput = false;
                    while (!validInput) {
                        System.out.print("Введите процент выпадения игрушки (от 1 до 100): ");
                        if (scanner.hasNextDouble()) {
                            dropFrequency = scanner.nextDouble();
                            validInput = true;
                        } else {
                            System.out.println("Недопустимый ввод! Введите цифрами.");
                            scanner.next();
                        }
                    }
            
                    toys.add(new Toy(id, title, quantity, dropFrequency));
                    System.out.println("Игрушка успешно добавлена!");
                    break;
                case 2:
                    System.out.print("Введите цифровой ID игрушки для изменения процента выпадения: ");
                    int toyId = scanner.nextInt();
                    System.out.print("Введите новый процент выпадения (от 1 до 100): ");
                    double newDropFrequency = scanner.nextDouble();

                    for (Toy toy : toys) {
                        if (toy.getId() == toyId) {
                            toy.setDropFrequency(newDropFrequency);
                            System.out.println("Процент выпадения игрушки успешно изменен!");
                            break;
                        }
                    }
                    break;
                case 3:
                    if (toys.isEmpty()) {
                        System.out.println("Нет игрушек для розыгрыша! Добавьте игрушки и попробуйте снова");
                        break;
                    }

                    Toy prizeToy = drawPrizeToy(toys);
                    System.out.println("Призовая игрушка: " + prizeToy.getTitle());

                    try {
                        FileWriter writer = new FileWriter("prize_toys.txt", true);
                        writer.write(prizeToy.getId() + " " + prizeToy.getTitle() + "\n");
                        writer.close();
                    } catch (IOException e) {
                        System.out.println("Ошибка записи в базу игрушек: " + e.getMessage());
                    }

                    break;
                case 4:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Недоступный выбор! Введите от 1 до 4");
                    break;
            }
        }
    }

    private static Toy drawPrizeToy(ArrayList<Toy> toys) {
        double totalDropFrequency = 0;
        for (Toy toy : toys) {
            totalDropFrequency += toy.getDropFrequency();
        }

        double random = new Random().nextDouble() * totalDropFrequency;

        double count = 0;
        for (Toy toy : toys) {
            count += toy.getDropFrequency();
            if (count >= random) {
                toy.decreaseQuantity();
                if (toy.getQuantity() == 0) {
                    toys.remove(toy);
                }
                return toy;
            }
        }

        return null;
    }
}

class Toy {
    private int id;
    private String title;
    private int quantity;
    private double dropFrequency;

    public Toy(int id, String title, int quantity, double dropFrequency) {
        this.id = id;
        this.title = title;
        this.quantity = quantity;
        this.dropFrequency = dropFrequency;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getDropFrequency() {
        return dropFrequency;
    }

    public void setDropFrequency(double dropFrequency) {
        this.dropFrequency = dropFrequency;
    }

    public void decreaseQuantity() {
        this.quantity--;
    }
}

       
