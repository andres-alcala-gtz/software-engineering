# Developer: Hector Alcala
# Purpose: Calculate the normal distributions of a list of decimals
# Project: 5



import random
import pandas



class Configuration:

    E = 2.718281828
    PI = 3.141592654

    INTEGER_LOWER = 50
    INTEGER_UPPER = None

    DECIMAL_LOWER = 41.0
    DECIMAL_UPPER = 300.0



class Input:


    @staticmethod
    def integer(prompt: str, lower: int, upper: int) -> int:
        """
        Enter, validate and return the integer if it is in the allowed range
        Arguments:
            prompt: str = The message to be displayed
            lower: int = The lower bound of the allowed range
            upper: int = The upper bound of the allowed range
        Returns:
            int = The validated integer
        Raises:
            ValueError = If the integer is not in the allowed range
            Exception = If another error occurs
        """

        while True:

            try:

                value = input(prompt)
                value = int(value)

                if lower is not None and value < lower:
                    raise ValueError(f"The value must be greater than or equal to {lower}")
                if upper is not None and value > upper:
                    raise ValueError(f"The value must be less than or equal to {upper}")

                break

            except Exception as exception:

                print(exception)

        return value


    @staticmethod
    def decimal(prompt: str, lower: float, upper: float) -> float:
        """
        Enter, validate and return the decimal if it is in the allowed range
        Arguments:
            prompt: str = The message to be displayed
            lower: float = The lower bound of the allowed range
            upper: float = The upper bound of the allowed range
        Returns:
            float = The validated decimal
        Raises:
            ValueError = If the decimal is not in the allowed range
            Exception = If another error occurs
        """

        while True:

            try:

                value = input(prompt)
                value = float(value)

                if lower is not None and value < lower:
                    raise ValueError(f"The value must be greater than or equal to {lower}")
                if upper is not None and value > upper:
                    raise ValueError(f"The value must be less than or equal to {upper}")

                break

            except Exception as exception:

                print(exception)

        return value



class Math:


    @staticmethod
    def mean(numbers: list[float]) -> float:
        """
        Calculate and return the mean of a list of decimals
        Arguments:
            numbers: list[float] = The list of decimals
        Returns:
            float = The mean of the list of decimals
        """

        length = len(numbers)
        summation = 0

        for number in numbers:
            summation += number

        mean = summation / length

        return mean


    @staticmethod
    def standard_deviation(numbers: list[float]) -> float:
        """
        Calculate and return the standard deviation of a list of decimals
        Arguments:
            numbers: list[float] = The list of decimals
        Returns:
            float = The standard deviation of the list of decimals
        """

        length = len(numbers)
        mean = Math.mean(numbers)
        summation = 0

        for number in numbers:
            summation += (number - mean) ** (2)

        standard_deviation = ((summation) / (length - 1)) ** (0.5)

        return standard_deviation


    @staticmethod
    def standard_scores(numbers: list[float]) -> list[float]:
        """
        Calculate and return the standard scores of a list of decimals
        Arguments:
            numbers: list[float] = The list of decimals
        Returns:
            list[float] = The standard scores of the list of decimals
        """

        mean = Math.mean(numbers)
        standard_deviation = Math.standard_deviation(numbers)

        standard_scores = []

        for number in numbers:
            standard_score = (number - mean) / (standard_deviation)
            standard_scores.append(standard_score)

        return standard_scores


    @staticmethod
    def sample_size(numbers: list[float], acceptable_error: float, standard_score: float) -> int:
        """
        Calculate and return the sample size of a list of decimals
        Arguments:
            numbers: list[float] = The list of decimals
            acceptable_error: float = The acceptable error
            standard_score: float = The standard score
        Returns:
            int = The sample size of the list of decimals
        """

        standard_deviation = Math.standard_deviation(numbers)

        sample_size = int(((standard_score * standard_deviation) / (acceptable_error)) ** (2))

        return sample_size


    @staticmethod
    def normal_distributions(numbers: list[float]) -> list[float]:
        """
        Calculate and return the normal distributions of a list of decimals
        Arguments:
            numbers: list[float] = The list of decimals
        Returns:
            list[float] = The normal distributions of the list of decimals
        """

        mean = Math.mean(numbers)
        standard_deviation = Math.standard_deviation(numbers)

        normal_distributions = []

        for number in numbers:
            normal_distribution = ((1) / ((2.0 * Configuration.PI * standard_deviation) ** (0.5))) * ((Configuration.E) ** -(((number - mean) ** (2)) / ((2.0) * (standard_deviation ** 2))))
            normal_distributions.append(normal_distribution)

        return normal_distributions



if __name__ == "__main__":

    print(f"\nThis program collects a set of numbers with the following conditions:\n- You must enter the quantity of numbers, must be at least {Configuration.INTEGER_LOWER}.\n- Each number will be between {Configuration.DECIMAL_LOWER} and {Configuration.DECIMAL_UPPER}.\nOnce all numbers have been collected, the program will calculate the normal distributions.\n")

    quantity = Input.integer("Quantity of numbers: ", Configuration.INTEGER_LOWER, Configuration.INTEGER_UPPER)

    numbers = random.sample(range(int(Configuration.DECIMAL_LOWER), int(Configuration.DECIMAL_UPPER) + 1), quantity)

    normal_distributions = Math.normal_distributions(numbers)

    print(f"\n{normal_distributions=}\n")

    data = pandas.DataFrame({"x": numbers, "y": normal_distributions})
    data.to_excel("normal_distributions.xlsx", index=False)
