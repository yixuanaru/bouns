import numpy as np

# 假設的初始投資
initial_investment = 30000000

# 每股收益 (EPS) 和股數
eps = 1.862
stocks = [2000000, 1666666.667, 1500000, 1200000]

# 現金流計算
cash_flows = [[-initial_investment, eps * stock] for stock in stocks]

# 計算每種情況下的IRR
irrs = [np.irr(cash_flow) for cash_flow in cash_flows]

# 輸出結果
for pe, irr in zip([15, 18, 20, 25], irrs):
    print(f"P/E Ratio: {pe}, IRR: {irr * 100:.2f}%")
