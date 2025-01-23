# WhatsApp Chat Analyzer
![image](https://github.com/user-attachments/assets/87855ade-6f2d-4429-82a6-6162461db808)

Welcome to the **WhatsApp Chat Analyzer** project! This tool provides an in-depth analysis of WhatsApp chat data, including user activity, word usage, emoji analysis, and more. It is built using **Python** and **Streamlit** for the frontend interface.

## Features

1. **Upload WhatsApp Chat Data**: Analyze chat data by uploading the exported `.txt` file from WhatsApp.
2. **User Statistics**:
   - Total messages
   - Number of words
   - Media shared
   - Links shared
3. **Most Active Users**: Identify the most active users in group chats.
4. **Most Common Words**: Visualize the most commonly used words, excluding stop words.
5. **Emoji Analysis**: Analyze and visualize the usage of emojis in chats.
6. **Timeline Analysis**:
   - Monthly timeline
   - Daily timeline
7. **Activity Maps**:
   - Most active days and months
   - Heatmap showing activity by hour and day of the week.
8. **Interactive Visualizations**:
   - Bar charts
   - Line charts
   - Pie charts
   - Heatmaps

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/mayur1710/WhatsApp-Chat-Analyzer.git
cd WhatsApp-Chat-Analyzer
```

### Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. Export your WhatsApp chat as a `.txt` file:
   - Open a chat on WhatsApp.
   - Click on the three dots in the top right corner.
   - Select **More > Export Chat**.
   - Choose **Without Media** (recommended).
2. Upload the exported `.txt` file in the app.
3. Select a user or choose "Overall" for a complete analysis.
4. View interactive charts and insights.

## File Structure

```
WhatsApp-Chat-Analyzer/
├── app.py               # Main Streamlit app
├── helper.py            # Helper functions for analysis
├── preprocessor.py      # Preprocessing functions for chat data
├── stop_hinglish.txt    # Stop words list for Hinglish filtering
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Screenshots

### Home Page
![image](https://github.com/user-attachments/assets/8a1bc177-4993-4b0c-9d35-5c8d613433b1)


### Statistics
![image](https://github.com/user-attachments/assets/53163bf9-f8b9-4b98-86b5-8d7910fb91a3)


### Activity Heatmap
![image](https://github.com/user-attachments/assets/f00e6ec9-ba13-4628-90a9-7443e7ee4a95)


## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python (pandas, matplotlib, seaborn)
- **Data Processing**: pandas,  urlextract

## Contributing

Contributions are welcome! If you'd like to improve the project or add new features, feel free to fork the repository and submit a pull request.



Enjoy analyzing your WhatsApp chats! 🚀
