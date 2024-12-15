import matplotlib.pyplot as plt
import numpy as np

# Define the color palette (inspired by Anya's artistic sensibilities)
colors = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5']

# Sample data for the visualization (replace with actual data later)
data = {
    'Positive': 25,
    'Negative': 15,
    'Neutral': 30,
    'Anticipation': 10,
    'Joy': 20
}

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a title (inspired by Anya's artistic flair)
plt.title('Whispers of Sentiment: A Symphony of Emotions', fontsize=14)

# Save the figure (replace 'sentiment_visualization.png' with
