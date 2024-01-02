package AOC1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class AOC1 {
    public static void main(String[] args) {
        String path = "AOC1/numbers.txt";

        part1(path);
        part2(path);
    }

    private static void part1(String path) {
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line;
            int sum = 0;

            while ((line = reader.readLine()) != null) {

                boolean isFirst = true;
                char firstNum = 0;
                char lastNum = 0;

                for (int i=0; i<line.length(); i++) {
                    char currentPos = line.charAt(i);

                    if (!isFirst && (currentPos > '0' && currentPos <= '9')) {
                        lastNum = currentPos;
                    }

                    if (isFirst && (currentPos > '0' && currentPos <= '9')) {
                        firstNum = currentPos;
                        isFirst = false;
                    }
                }

                if (lastNum == 0) {
                    lastNum = firstNum;
                }

                String result = Character.toString(firstNum) + Character.toString(lastNum);
                sum += Integer.parseInt(result);
            }

            System.out.println();
            System.out.printf("Part 1: %d", sum);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void part2(String path) {

        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line;

            int sum = 0;

            while ((line = reader.readLine()) != null) {
                int newResult = getNumberFromLine(line);
                String newLine = Integer.toString(newResult);

                String result = getString(newLine);

                sum += Integer.parseInt(result);
            }

            System.out.printf("\n\nPart 2: %d", sum);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String getString(String line) {
        boolean isFirst = true;
        char firstNum = 0;
        char lastNum = 0;

        for (int i = 0; i< line.length(); i++) {
            char currentPos = line.charAt(i);

            if (!isFirst && (currentPos > '0' && currentPos <= '9')) {
                lastNum = currentPos;
            }

            if (isFirst && (currentPos > '0' && currentPos <= '9')) {
                firstNum = currentPos;
                isFirst = false;
            }

        }

        if (lastNum == 0) {
            lastNum = firstNum;
        }

        return Character.toString(firstNum) + Character.toString(lastNum);
    }

    private static int getNumberFromLine(String text) {
        String newLine;
        String line;

        int result;

        line = text.replaceAll("zero", "0").replaceAll("oneight", "18").replaceAll("twone", "21")
                .replaceAll("eightwo", "82").replaceAll("one", "1").replaceAll("two", "2")
                .replaceAll("three", "3").replaceAll("four", "4").replaceAll("five", "5").replaceAll("six", "6")
                .replaceAll("seven", "7").replaceAll("eight", "8").replaceAll("nine", "9");
        newLine = line.replaceAll("[^0-9]", "");
        result = Integer.parseInt(newLine);

        return result;
    }
}