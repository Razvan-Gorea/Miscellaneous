/**
 * Author: Razvan Gorea
 * Date: 16/1/2023
 * Write a program that asks the user for their name and age. 
 * The program then prints out the number of vowels in their name and whether they are a minor or an adult.
 */


import java.util.Scanner;

public class VowelAge {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String name = input.nextLine();
        int age = input.nextInt();
        input.close();

        int nameLength = name.length();
        int vowelCount = 0;

        for (int i = 0; i < nameLength; i++) {
            char letter = name.charAt(i);
            if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u' || letter == 'A' || letter == 'E' || letter == 'I' || letter == 'O' || letter == 'U') {
                vowelCount++;
            }
        }

        if (age < 18){
            System.out.println("Hello " + name + ", you have " + vowelCount + " vowels, and you are a minor");
        }else {
            System.out.println("Hello " + name + ", you have " + vowelCount + " vowels, and you are an adult");
        }
    }
}
