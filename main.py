import result as rs

portfolio_returns = [0.12, 0.10, 0.15, 0.09, 0.11]  # Example portfolio returns
benchmark_returns = [0.10, 0.09, 0.14, 0.08, 0.10]  # Example benchmark returns

# Calculate Information Ratio
information_ratio = rs.calculate_information_ratio(portfolio_returns, benchmark_returns)
print(information_ratio)