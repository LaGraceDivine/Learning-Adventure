import java.io.*;
import java.util.Scanner;

public class StringMatch {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide 'interactive' or 'file' mode as command line argument");
            return;
        }

        String mode = args[0];

        if (mode.equals("interactive")) {
            //the interactive mode
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the text: ");
            String text = sc.nextLine();
            System.out.println("Enter the pattern to search for: ");
            String pattern = sc.nextLine();
            
            int n = text.length();
            int m = pattern.length();
            int result = -1;
            
            //Brute force algorithm matching strings
            for (int i = 0; i <= n - m; i++) {
                int j = 0;
                while (j < m && pattern.charAt(j) == text.charAt(i + j)) {
                    j++;
                }
                if (j == m) {
                    result = i;  //found the pattern
                    break;
                }
            }
            
            if (result != -1) {
                System.out.println("Pattern found at index: " + result);
            } else {
                System.out.println("Pattern not found");
            }
            sc.close();

        } else if (mode.equals("file")) {
            //the file mode
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            BufferedWriter writer = new BufferedWriter(new FileWriter("result.txt"));
            int numCases = Integer.parseInt(reader.readLine().trim());

            for (int i = 0; i < numCases; i++) {
                String text = reader.readLine().trim();
                String pattern = reader.readLine().trim();
                int n = text.length();
                int m = pattern.length();
                int result = -1;
                
                //Brute force algorithm that matches strings
                for (int j = 0; j <= n - m; j++) {
                    int k = 0;
                    while (k < m && pattern.charAt(k) == text.charAt(j + k)) {
                        k++;
                    }
                    if (k == m) {
                        result = j;  //found the pattern
                        break;
                    }
                }
                
                writer.write(result + "\n");
            }

            reader.close();
            writer.close();
        } else {
            System.out.println("Invalid mode. Use 'interactive' or 'file'.");//if the mode is not specified
        }
    }
}
