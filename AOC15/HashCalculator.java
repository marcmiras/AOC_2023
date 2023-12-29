import java.util.List;

public class HashCalculator {

    public int calculateHash(String[] input) {
        int totalAsciiValue = 0;
        int result = 0;

        for (String strs : input) {
            totalAsciiValue = 0;
            for (char ch : strs.toCharArray()) {
                totalAsciiValue += ch;
                totalAsciiValue *= 17;
                totalAsciiValue %= 256;
            }
            result += totalAsciiValue;
        }

        return result;
    }
}