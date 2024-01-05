package AOC13;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class AOC13 {

    public static int parsePatterns(List<String> pattern, int skipLine) {
        int verticalResult = findVerticalLines(pattern, skipLine);
        if (verticalResult != 0) {
            return verticalResult;
        }

        return findHorizontalLines(pattern, skipLine);
    }

    private static int findVerticalLines(List<String> pattern, int skipLine) {
        for (int i = 0; i < pattern.size() - 1; i++) {
            boolean lineFound = true;
            int height = Math.min(i + 1, pattern.size() - 1 - i);

            for (int j = 0; j < height; j++) {
                if (!pattern.get(i - j).equals(pattern.get(i + 1 + j))) {
                    lineFound = false;
                    break;
                }
            }

            if (lineFound) {
                int result = (i + 1) * 100;
                if (result != skipLine) {
                    return result;
                }
            }
        }

        return 0;
    }


    private static int findHorizontalLines(List<String> pattern, int skipLine) {
        for (int i = 0; i < pattern.get(0).length() - 1; i++) {
            boolean lineFound = true;
            int width = Math.min(i + 1, pattern.get(0).length() - 1 - i);

            for (int k = 0; k < width; k++) {
                for (String s : pattern) {
                    if (s.charAt(i - k) != s.charAt(i + 1 + k)) {
                        lineFound = false;
                        break;
                    }
                }
                if (!lineFound) {
                    break;
                }
            }

            if (lineFound) {
                int result = i + 1;
                if (result != skipLine) {
                    return result;
                }
            }
        }

        return 0;
    }

    public static List<List<String>> readInput(String filename) throws IOException {
        List<List<String>> patterns = new ArrayList<>();
        List<String> currentPattern = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim();
                if (line.isEmpty()) {
                    patterns.add(new ArrayList<>(currentPattern));
                    currentPattern.clear();
                } else {
                    currentPattern.add(line);
                }
            }
        }

        if (!currentPattern.isEmpty()) {
            patterns.add(new ArrayList<>(currentPattern));
        }

        return patterns;
    }

    public static void main(String[] args) {
        try {
            List<List<String>> patterns = readInput("AOC13/input.txt");

            int part1 = 0;
            List<Integer> answers = new ArrayList<>();

            for (List<String> pattern : patterns) {
                int result = parsePatterns(pattern, 0);
                answers.add(result);
                part1 += result;
            }

            int part2 = 0;

            for (int n = 0; n < patterns.size(); n++) {
                int skip = answers.get(n);
                int width = patterns.get(n).get(0).length();
                int height = patterns.get(n).size();

                for (int j = 0; j < height; j++) {
                    boolean moveOn = false;
                    for (int k = 0; k < width; k++) {
                        List<String> newPattern = new ArrayList<>(patterns.get(n));
                        char[] row = newPattern.get(j).toCharArray();
                        row[k] = (row[k] == '.') ? '#' : '.';
                        newPattern.set(j, new String(row));

                        int result = parsePatterns(newPattern, skip);

                        if (result != 0 && result != answers.get(n)) {
                            part2 += result;
                            moveOn = true;
                            break;
                        }
                    }

                    if (moveOn) {
                        break;
                    }
                }
            }

            System.out.println("Part 1: " + part1);
            System.out.println("Part 2: " + part2);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
