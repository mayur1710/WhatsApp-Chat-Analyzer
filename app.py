import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
from helper import daily_timeline

# Sidebar title
st.sidebar.title("Whatsapp Chat Analysis")

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Displaying the dataframe
    #st.dataframe(df)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group notification' in user_list:
        user_list.remove('group notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

    if st.sidebar.button("Show Analysis"):

        # Fetch statistics
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics of Whatsapp Chat")

        # Create columns with proper spacing
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Messages")
            st.subheader(str(num_messages))

        with col2:
            st.header("Total Words")
            st.subheader(str(words))

        with col3:
            st.header("Media Shared")
            st.subheader(str(num_media_messages))

        with col4:
            st.header("Links Shared")
            st.subheader(str(num_links))

        # Most Busy Users Analysis (if selected user is "Overall")
        if selected_user == "Overall":
            st.title("Most Busy Users")
            x, new_df = helper.most_busy_users(df)

            # Creating a bar chart
            fig, ax = plt.subplots()
            ax.bar(x.index, x.values, color="red")
            plt.xticks(rotation="vertical")

            col1, col2 = st.columns(2)

            with col1:
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # Most Common Words Analysis
        most_common_df = helper.most_common_words(selected_user, df)
        st.title("Most Common Words")
        st.dataframe(most_common_df)

        # Plotting Most Common Words as a bar chart
        fig, ax = plt.subplots()
        ax.bar(most_common_df['Word'], most_common_df['Frequency'], color="orange")
        plt.xticks(rotation='vertical')
        st.title("Most Common Words Bar Chart")
        st.pyplot(fig)

        emoji_df=helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1,col2=st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)

        st.title("Monthly Timeline Analysis")
        timeline=helper.monthly_timeline(selected_user,df)

        fig,ax=plt.subplots()

        ax.plot(timeline['time'], timeline['messages'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title("Daily Timeline Analysis")

        #Daily Timeline Analysis

        daily_timeline=helper.daily_timeline(selected_user,df)
        fig,ax=plt.subplots()


        ax.plot(daily_timeline['only_date'], daily_timeline['messages'])

        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        st.title("Activity Map")
        col1,col2=st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user,df)

            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color="purple")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")
            busy_month=helper.month_activity_map(selected_user,df)

            fig,ax=plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color="magenta")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        st.title("Online Activity Map")
        user_heatmap=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)
        st.pyplot(fig)