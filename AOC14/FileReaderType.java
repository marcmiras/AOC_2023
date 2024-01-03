package AOC14;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class FileReaderType {

    public void readFile() {
        //String exampleFile = "AOC14/example.txt";
        String inputFile = "AOC14/input.txt";

        Path path = Paths.get(inputFile);

        try (BufferedReader reader = Files.newBufferedReader(path)){
            List<String>lines = Files.readAllLines(path);
            tiltFile(lines);

        } catch (IOException e){
            e.printStackTrace();
        }

    }

    private char[][] convertToMatrix(List<String> lines, int rows, int cols) {
        char[][] charArray = new char[rows][cols];

        for (int i = 0; i < rows; i++) {
            String currentString = lines.get(i);
            for (int j = 0; j < cols; j++) {
                charArray[i][j] = currentString.charAt(j);
            }
        }

        return charArray;
    }

    private void tiltFile(List<String> lines) {
        int rows = lines.size();
        int cols = lines.get(0).length();

        char[][] matrix = convertToMatrix(lines, rows, cols);

        int i, j;

        boolean ongoing;

        do {
            ongoing = false;
            for (i = 0; i < rows; i++) {
                for (j = 0; j < cols; j++) {
                    if (i+1 < rows && matrix[i+1][j] == 'O' && matrix[i][j] == '.') {
                        matrix[i+1][j] = '.';
                        matrix[i][j] = 'O';
                        ongoing = true;
                    }
                }
            }
        } while (ongoing);

        int result = 0;

        for (i = 0; i < rows; i++) {
            int nums = 0;
            for (j = 0; j < cols; j++) {
                if (matrix[i][j] == 'O') {
                    nums++;
                }
            }
            result += (nums * (rows-i));
        }
        System.out.println();
        System.out.printf("Part 1: %d", result);
        System.out.println();
    }
}
