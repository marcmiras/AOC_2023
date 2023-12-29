import java.util.List;

public class AOC15 {

    public static void main(String[] args) {
        FileParser reader = new FileParser();
        HashCalculator hash = new HashCalculator();

        String[] lines = reader.readLines().get(0).split(",");

        int total = hash.calculateHash(lines);

        System.out.printf("Part 1: %d", total);
        System.out.println();
    }


}