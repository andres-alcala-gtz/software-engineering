# Developer: Hector Alcala
# Purpose: Calculate the sample size of a list of decimals
# Project: 4



class Configuration:

    INTEGER_LOWER = 11
    INTEGER_UPPER = 20

    DECIMAL_LOWER = 3_000.0
    DECIMAL_UPPER = 15_000.0



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



if __name__ == "__main__":

    print(f"\nThis program collects a set of numbers with the following conditions:\n- You must enter the acceptable error.\n- You must enter between {Configuration.INTEGER_LOWER} and {Configuration.INTEGER_UPPER} numbers.\n- Each number must be between {Configuration.DECIMAL_LOWER} and {Configuration.DECIMAL_UPPER}.\nOnce all numbers have been collected, the program will calculate the sample size.\n")

    error = Input.decimal("Acceptable error: ", None, None)

    quantity = Input.integer("Quantity of numbers: ", Configuration.INTEGER_LOWER, Configuration.INTEGER_UPPER)

    numbers = []

    for index in range(1, quantity + 1):
        number = Input.decimal(f"Number {index}: ", Configuration.DECIMAL_LOWER, Configuration.DECIMAL_UPPER)
        numbers.append(number)

    sample_size_95 = Math.sample_size(numbers, error, 1.96)
    sample_size_99 = Math.sample_size(numbers, error, 2.58)

    print(f"\n{sample_size_95=}, {sample_size_99=}\n")
