#AGENT BASED
import matplotlib.pyplot as plt
import networkx as nx

# Assuming G is your network graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()


#SYS DYN
# Run the model
results = model.run()

# Plot the results
for i in range(1, 6):
    plt.plot(results[f'Equity_Type{i}_Market_Capital'], label=f'Equity_Type{i}')
plt.legend()
plt.show()


#INTERACTION

# Initialize lists to store the results
investor_capital = {investor: [] for investor in ['Risk_Averse_Investor', 'Risk_Neutral_Investor', 'Risk_Seeking_Investor', 'Balanced_Investor', 'Random_Investor']}
total_market_capital = []

# Run the simulation as before, but store the results
for t in range(100):
    # Run the agent-based model as before...
    
    # Store the results
    for investor in investor_capital:
        investor_capital[investor].append(G.nodes[investor]['capital'])
    total_market_capital.append(sum(G.nodes[asset]['market_capital'] for asset in [f'Equity_Type{i}' for i in range(1, 6)] + [f'Options_Type{i}' for i in range(1, 4)]))

# Plot the results
for investor, capital in investor_capital.items():
    plt.plot(capital, label=investor)
plt.plot(total_market_capital, label='Total Market Capital')
plt.legend()
plt.show()


