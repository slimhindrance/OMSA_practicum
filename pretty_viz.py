import seaborn as sns
sns.set_theme(style="whitegrid")

# Let's plot market capitals over time with Seaborn
for i in range(1, 6):
    sns.lineplot(data=results[f'Equity_Type{i}_Market_Capital'], label=f'Equity_Type{i}').set(title='Market Capital Over Time', xlabel='Time', ylabel='Market Capital')

# To avoid overlapping of plots we use plt.show() after each plot
plt.show()

# Initialize a dataframe to store the results
data = {
    'Time': [],
    'Investor': [],
    'Capital': [],
}

# Run the simulation as before, but store the results in the dataframe
for t in range(100):
    # Run the agent-based model as before...
    
    # Store the results
    for investor in investor_capital:
        data['Time'].append(t)
        data['Investor'].append(investor)
        data['Capital'].append(G.nodes[investor]['capital'])

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Plot the results using seaborn
sns.lineplot(x='Time', y='Capital', hue='Investor', data=df).set(title='Investor Capital Over Time', xlabel='Time', ylabel='Capital')
plt.show()
