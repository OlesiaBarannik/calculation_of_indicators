import argparse

class NumberStatistics:
    def __init__(self, file_path):
        self.file_path = file_path
        self.numbers = []
        self.min_num = None
        self.max_num = None
        self.median = None
        self.average = None
        self.max_increasing_sequence = []
        self.max_decreasing_sequence = []

    def _read_numbers_from_file(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                self.numbers.extend(map(int, line.split()))

    def calculate_statistics(self):
        self._read_numbers_from_file()
        self._find_min_max()
        self._calculate_average()
        self._find_max_increasing_sequence()
        self._find_max_decreasing_sequence()
        self._calculate_median()

    def _find_min_max(self):
        self.min_num = min(self.numbers)
        self.max_num = max(self.numbers)

    def _calculate_average(self):
        self.average = sum(self.numbers) / len(self.numbers) if self.numbers else None

    def _find_max_increasing_sequence(self):
        max_increasing_sequence = []
        current_sequence = []

        for num in self.numbers:
            if not current_sequence or num > current_sequence[-1]:
                current_sequence.append(num)
            else:
                if len(current_sequence) > len(max_increasing_sequence):
                    max_increasing_sequence = current_sequence[:]
                current_sequence = [num]

        if len(current_sequence) > len(max_increasing_sequence):
            max_increasing_sequence = current_sequence[:]

        self.max_increasing_sequence = max_increasing_sequence

    def _find_max_decreasing_sequence(self):
        max_decreasing_sequence = []
        current_sequence = []

        for num in self.numbers:
            if not current_sequence or num < current_sequence[-1]:
                current_sequence.append(num)
            else:
                if len(current_sequence) > len(max_decreasing_sequence):
                    max_decreasing_sequence = current_sequence[:]
                current_sequence = [num]

        if len(current_sequence) > len(max_decreasing_sequence):
            max_decreasing_sequence = current_sequence[:]

        self.max_decreasing_sequence = max_decreasing_sequence

    def _calculate_median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:
            self.median = sorted_numbers[n // 2]
        else:
            self.median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    def print_statistics(self):
        print(f"The minimum number in the file is: {self.min_num}")
        print(f"The maximum number in the file is: {self.max_num}")
        print(f"Median of numbers in the file: {self.median}")
        print(f"Average of numbers in the file: {self.average}")
        print(f"Largest increasing sequence: {self.max_increasing_sequence}")
        print(f"Largest decreasing sequence: {self.max_decreasing_sequence}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate statistics for a file of integers.")
    parser.add_argument('file_path', type=str, help="Path to the file containing integers")
    args = parser.parse_args()

    stats = NumberStatistics(args.file_path)
    stats.calculate_statistics()
    stats.print_statistics()
