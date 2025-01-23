import matplotlib.pyplot as plt
import streamlit as st
from urlextract import URLExtract
import pandas as pd
from collections import Counter
import emoji
import seaborn as sns
extract = URLExtract()


def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Number of messages
    num_messages = df.shape[0]

    # Total number of words
    words = []
    for message in df['messages']:  # Changed from 'message' to 'messages'
        words.extend(message.split())

    # Number of media messages
    num_media_messages = df[df['messages'] == '<Media omitted>\n'].shape[0]  # Changed from 'message' to 'messages'

    # Extracting links
    links = []
    for message in df['messages']:  # Changed from 'message' to 'messages'
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    # Get the count of messages per user
    user_counts = df['user'].value_counts().head()

    # Calculate percentage of messages by each user
    user_percentages = (
        round((df['user'].value_counts() / df.shape[0]) * 100, 2)
        .reset_index()
        .rename(columns={'index': 'name', 'user': 'percent'})
    )

    return user_counts, user_percentages


def most_common_words(selected_user, df):
    # Reading stop words from the file
    with open('stop_hinglish.txt', 'r', encoding='utf-8') as f:
        stop_words = f.read().splitlines()  # Read and split by line

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['messages'] != '<Media omitted>\n']  # Changed from 'message' to 'messages'

    words = []

    # Filter words based on stop words list
    for message in temp['messages']:  # Changed from 'message' to 'messages'
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    # Create DataFrame of most common words
    most_common_df = pd.DataFrame(Counter(words).most_common(25))
    most_common_df.columns = ['Word', 'Frequency']  # Rename columns for clarity




    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis = []
    for message in df['messages']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoji_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    timeline = df.groupby(['year', 'month', 'month_num']).count()['messages'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time

    return timeline
def daily_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    daily_timeline = df.groupby(['only_date']).count()['messages'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap= (df.pivot_table(index="day_name", columns="period", values="messages", aggfunc='count').fillna(0))

    return user_heatmap