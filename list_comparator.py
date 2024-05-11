"""Module for comparing averages of two lists."""

class ListComparator:
    """Comparator class to compare averages of two number lists."""
    def __init__(self, list1, list2):
        """
        Initialize the ListComparator with two lists.

        Args:
            list1 (list): The first list of numbers.
            list2 (list): The second list of numbers.
        """
        self.list1 = list1
        self.list2 = list2

    def average(self, data_list):
        """
        Calculate the average of the given list.

        Args:
            data_list (list): List of numbers to calculate the average.

        Returns:
            float: Average of the list.
        """
        return sum(data_list) / len(data_list) if data_list else 0

    def compare_averages(self):
        """
        Compare the averages of the two lists and return a descriptive message.

        Returns:
            str: A message describing which list has a greater average or if they are equal.
        """
        avg1 = self.average(self.list1)
        avg2 = self.average(self.list2)
        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
