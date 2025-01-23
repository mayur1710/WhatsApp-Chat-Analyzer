import re
import pandas as pd

def preprocess(data):
    # Regex pattern to match the date and time format in WhatsApp chats
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    # Splitting data into messages and extracting dates
    messages = re.split(pattern, data)[1:]  # Skip the first split as it's empty
    dates = re.findall(pattern, data)

    # Create a DataFrame
    df = pd.DataFrame({"user_message": messages, "message_dates": dates})

    # Convert date strings to datetime format
    try:
        df["message_dates"] = pd.to_datetime(df["message_dates"], format="%d/%m/%y, %H:%M - ")
    except ValueError:
        df["message_dates"] = pd.to_datetime(df["message_dates"], format="%d/%m/%Y, %H:%M - ")

    df.rename(columns={"message_dates": "date"}, inplace=True)

    # Extract users and messages
    users = []
    messages = []
    for message in df["user_message"]:
        entry = re.split(r'([\w\W]+?):\s', message)  # Split on ': ' to separate user and message
        if len(entry) > 1:  # If a user is found
            users.append(entry[1])
            messages.append(entry[2])
        else:  # System or group notifications
            users.append("group notification")
            messages.append(entry[0])

    # Add extracted users and messages to the DataFrame
    df['user'] = users
    df["messages"] = messages  # Column name is 'messages'

    # Drop the original raw user_message column
    df.drop(columns=['user_message'], inplace=True)

    # Add time-based features
    df["year"] = df['date'].dt.year
    df["month"] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date
    df["day"] = df['date'].dt.day
    df["hour"] = df['date'].dt.hour
    df["minute"] = df['date'].dt.minute
    df['day_name'] = df['date'].dt.day_name()

    period = []
    for hour in df[['day_name', "hour"]]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str("00"))
        elif hour == 0:
            period.append(str("00") + '-' + str(hour + 1))
        else:
            period.append(str(hour) + '-' + str(hour + 1))

    df['period'] = period





    return df

