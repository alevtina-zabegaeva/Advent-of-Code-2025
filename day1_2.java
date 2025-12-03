import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

public class day1_2 {
    public static void main(String[] args) {
        String filename = "1.1input.txt";
//        String filename = "1.1test.txt";

        List<Integer> instructions = new ArrayList<>();

        try(BufferedReader br = new BufferedReader(new FileReader(filename))) {
            for(String line; (line = br.readLine()) != null; ) {
                int direction = line.charAt(0) == 'R'? 1 : -1;
                instructions.add(direction * Integer.parseInt(line.substring(1)));
            }
        }
        catch(IOException ex){
            ex.printStackTrace();
        }
        
        //System.out.println(instructions);

        int dial = 50;
        int password = 0;
        for (int instruction : instructions){
            int dialPrev = dial;
            dial += instruction;

            int counter = dial / 100;
            int r = dial % 100;
            if (r != 0 && dial < 0) counter -= 1;

            dial %= 100;
            if (dial < 0) dial += 100;
            password += Math.abs(counter);
        
            if (dial == 0 && dialPrev != 0 && counter <= 0) password += 1;
            if (dial != 0 && dialPrev == 0 && counter < 0) password -= 1;
        }

        System.out.println(password);
    }
}
