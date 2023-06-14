import pysd

# Define the model in a string
model = """
    'Stocks':
    'Equity_Type1_Market_Capital' = INTEG ('Investment_into_Equity_Type1'-'Withdrawal_from_Equity_Type1', 'Initial_Equity_Type1_Market_Capital')
    'Equity_Type2_Market_Capital' = INTEG ('Investment_into_Equity_Type2'-'Withdrawal_from_Equity_Type2', 'Initial_Equity_Type2_Market_Capital')
    'Equity_Type3_Market_Capital' = INTEG ('Investment_into_Equity_Type3'-'Withdrawal_from_Equity_Type3', 'Initial_Equity_Type3_Market_Capital')
    'Equity_Type4_Market_Capital' = INTEG ('Investment_into_Equity_Type4'-'Withdrawal_from_Equity_Type4', 'Initial_Equity_Type4_Market_Capital')
    'Equity_Type5_Market_Capital' = INTEG ('Investment_into_Equity_Type5'-'Withdrawal_from_Equity_Type5', 'Initial_Equity_Type5_Market_Capital')
    'Options_Type1_Market_Capital' = INTEG ('Investment_into_Options_Type1'-'Withdrawal_from_Options_Type1', 'Initial_Options_Type1_Market_Capital')
    'Options_Type2_Market_Capital' = INTEG ('Investment_into_Options_Type2'-'Withdrawal_from_Options_Type2', 'Initial_Options_Type2_Market_Capital')
    'Options_Type3_Market_Capital' = INTEG ('Investment_into_Options_Type3'-'Withdrawal_from_Options_Type3', 'Initial_Options_Type3_Market_Capital')

    'Flows':
    'Investment_into_Equity_Type1' = 'Equity_Type1_Investment_Rate' * 'Risk_Averse_Investor_Capital'
    'Withdrawal_from_Equity_Type1' = 'Equity_Type1_Withdrawal_Rate' * 'Equity_Type1_Market_Capital'
    'Investment_into_Equity_Type2' = 'Equity_Type2_Investment_Rate' * 'Risk_Neutral_Investor_Capital'
    'Withdrawal_from_Equity_Type2' = 'Equity_Type2_Withdrawal_Rate' * 'Equity_Type2_Market_Capital'
    'Investment_into_Equity_Type3' = 'Equity_Type3_Investment_Rate' * 'Risk_Seeking_Investor_Capital'
    'Withdrawal_from_Equity_Type3' = 'Equity_Type3_Withdrawal_Rate' * 'Equity_Type3_Market_Capital'
    'Investment_into_Equity_Type4' = 'Equity_Type4_Investment_Rate' * 'Risk_Averse_Investor_Capital'
    'Withdrawal_from_Equity_Type4' = 'Equity_Type4_Withdrawal_Rate' * 'Equity_Type4_Market_Capital'
    'Investment_into_Equity_Type5' = 'Equity_Type5_Investment_Rate' * 'Risk_Seeking_Investor_Capital'
    'Withdrawal_from_Equity_Type5' = 'Equity_Type5_Withdrawal_Rate' * 'Equity_Type5_Market_Capital'
    'Investment_into_Options_Type1' = 'Options_Type1_Investment_Rate' * 'Balanced_Investor_Capital'
    'Withdrawal_from_Options_Type1' = 'Options_Type1_Withdrawal_Rate' * 'Options_Type1_Market_Capital'
    'Investment_into_Options_Type2' = 'Options_Type2_Investment_Rate' * 'Risk_Neutral_Investor_Capital'
    'Withdrawal_from_Options_Type2' = 'Options_Type2_Withdrawal_Rate' * 'Options_Type2_Market_Capital'
    'Investment_into_Options_Type3' = 'Options_Type3_Investment_Rate' * 'Risk_Seeking_Investor_Capital'
    'Withdrawal_from_Options_Type3' = 'Options_Type3_Withdrawal_Rate' * 'Options_Type3_Market_Capital'
    
    'Variables':
    'Equity_Type1_Performance' = 'Equity_Type1_Market_Capital' / 'Initial_Equity_Type1_Market_Capital'

    'Constants':
    'Risk_Averse_Investment_Function' = 1 / (1 + EXP(-('Equity_Type1_Performance' - 1)))
    'Risk_Neutral_Investment_Function' = 1 / (1 + EXP(-('Equity_Type2_Performance' - 1)))
    'Risk_Seeking_Investment_Function' = 1 / (1 + EXP(-('Equity_Type3_Performance' - 1)))
    'Random_Investment_Function' = 1 / (1 + EXP(-('Equity_Type4_Performance' - 1))) + RANDOM UNIFORM(0, 1)
    'Initial_Equity_Type1_Market_Capital' = 5000000 # initial values, modify as needed
    'Initial_Equity_Type2_Market_Capital' = 6000000
    'Initial_Equity_Type3_Market_Capital' = 7000000
    'Initial_Equity_Type4_Market_Capital' = 8000000
    'Initial_Equity_Type5_Market_Capital' = 9000000
    'Initial_Options_Type1_Market_Capital' = 5000000
    'Initial_Options_Type2_Market_Capital' = 6000000
    'Initial_Options_Type3_Market_Capital' = 7000000
    'Risk_Averse_Investor_Capital' = 10000000
    'Risk_Neutral_Investor_Capital' = 15000000
    'Risk_Seeking_Investor_Capital' = 20000000
    'Balanced_Investor_Capital' = 25000000
    'Equity_Type1_Investment_Rate' = IF THEN ELSE('Equity_Type1_Performance' > 1, 0.03, 0.02)
    'Equity_Type1_Withdrawal_Rate' = 0.01
    'Equity_Type2_Investment_Rate' = 'Risk_Neutral_Investment_Function' * 0.03
    'Equity_Type2_Withdrawal_Rate' = 0.015
    'Equity_Type3_Investment_Rate' = 'Risk_Seeking_Investment_Function' * 0.04
    'Equity_Type3_Withdrawal_Rate' = 0.02
    'Equity_Type4_Investment_Rate' = 'Random_Investment_Function' * 0.05
    'Equity_Type4_Withdrawal_Rate' = 0.025
    'Equity_Type5_Investment_Rate' = 0.06
    'Equity_Type5_Withdrawal_Rate' = 0.03
    'Options_Type1_Investment_Rate' = 0.04
    'Options_Type1_Withdrawal_Rate' = 0.02
    'Options_Type2_Investment_Rate' = 0.05
    'Options_Type2_Withdrawal_Rate' = 0.025
    'Options_Type3_Investment_Rate' = 0.06
    'Options_Type3_Withdrawal_Rate' = 0.03
"""

# Save the model to a file
with open("financial_model_complex.mdl", "w") as file:
    file.write(model)

# Load the model
model = pysd.read_vensim("financial_model_complex.mdl")

# Run the model
results = model.run()

# Print the results
print(results)
