import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FileParser {

    public List<String> readLines() {
        String filename = "src/input.txt";
        String filename_example = "src/example.txt";

        List<String> charArrays = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))){
            String line = reader.readLine();
            while (line != null) {
                charArrays.add(line.replaceAll("\r", ""));
                line = reader.readLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return charArrays;
    }

}