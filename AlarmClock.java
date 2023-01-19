/*
 * Author: Razvan Gorea
 * Date: 16/01/2023 
 */

import java.util.Scanner;

public class AlarmClock {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String time = input.nextLine();
        String[] timeArray = time.split(" ");
        
        String firstinput = timeArray[0];
        String secondinput = timeArray[1];
        String overall = firstinput + secondinput;
        int timeInt = Integer.parseInt(overall);


        boolean flag = true;
        int falseCount = 0;
        while(flag && input.hasNextLine()){
            String time2 = input.nextLine();
            String[] timeArray2 = time2.split(" ");
            String firstpart = timeArray2[0];
            String secondpart = timeArray2[1];
            String number = firstpart + secondpart;
            int newnum = Integer.parseInt(number);

            if (newnum < timeInt){
                falseCount++;
            }else{
                flag = false;
            }
    }
    input.close();
    System.out.println("false alarms: " + falseCount);
}
}
