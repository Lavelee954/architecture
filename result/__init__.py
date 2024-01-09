import numpy as np

def calculate_information_ratio(portfolio_returns, benchmark_returns):
    """
    Calculate the Information Ratio of a portfolio.

    :param portfolio_returns: A list or numpy array of portfolio returns.
    :param benchmark_returns: A list or numpy array of benchmark returns.
    :return: The Information Ratio.
    """
    # Calculate the difference in returns
    return_differences = np.array(portfolio_returns) - np.array(benchmark_returns)

    # Calculate the average of the differences
    average_difference = np.mean(return_differences)

    # Calculate the standard deviation of the differences (Tracking Error)
    tracking_error = np.std(return_differences, ddof=1)

    # Calculate the Information Ratio
    information_ratio = average_difference / tracking_error

    return information_ratio

# Example data
portfolio_returns = [0.12, 0.10, 0.15, 0.09, 0.11]  # Example portfolio returns
benchmark_returns = [0.10, 0.09, 0.14, 0.08, 0.10]  # Example benchmark returns

# Calculate Information Ratio
information_ratio = calculate_information_ratio(portfolio_returns, benchmark_returns)
information_ratio