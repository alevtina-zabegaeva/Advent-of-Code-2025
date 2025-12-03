import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class day1_1 {
    public static void main(String[] args) {
        String filename = "1.1input.txt";
        // String filename = "1.1test.txt";

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
            dial = (dial + instruction) % 100;
            if (dial == 0) password += 1;
        }

        System.out.println(password);
    }
}
