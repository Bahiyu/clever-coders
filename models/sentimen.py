import requests
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

# Function to fetch news articles from GNews API
def fetch_gnews(api_key, query):
    url = f"https://gnews.io/api/v4/search?q={query}&token={api_key}&lang=en"  # Adding language filter
    print(f"Fetching articles from URL: {url}")  # Debugging line
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")  # Debugging line
    if response.status_code == 200:
        # Print the raw response to debug
        print("Raw API response:", response.json())  # Debugging line
        articles = response.json().get('articles', [])
        if not articles:
            print(f"No articles found for query: {query}")  # Debugging line
        return articles
    else:
        print("Error fetching articles:", response.status_code)
        return []

# Function to analyze sentiment of the articles
def analyze_sentiment(articles):
    sentiments = []
    for article in articles:
        text = article.get('description') or article.get('content')
        if text:
            blob = TextBlob(text)
            sentiments.append({
                'title': article['title'],
                'sentiment': blob.sentiment.polarity  # Value between -1 (negative) and 1 (positive)
            })
        else:
            print(f"No valid text found for article titled: {article.get('title')}")
    return sentiments

# Function to visualize the results
def visualize_sentiment(sentiments, crop_name):
    if not sentiments:  # Check if the list is empty
        print("No sentiments to visualize.")
        return
    
    # Create a DataFrame for easier manipulation
    df = pd.DataFrame(sentiments)
    
    # Sort by sentiment polarity
    df_sorted = df.sort_values(by='sentiment', ascending=False)

    # Limit to top N articles for visualization
    top_n = 10  # Number of articles to display
    top_articles = df_sorted.head(top_n)

    # Bar chart of sentiment for top articles
    plt.figure(figsize=(10, 6))
    plt.barh(top_articles['title'], top_articles['sentiment'], color='skyblue')
    plt.xlabel('Sentiment Polarity')
    plt.title(f'Top {top_n} Articles Related to {crop_name.capitalize()} (Sentiment Analysis)')
    plt.axvline(0, color='red', linestyle='--')  # Line to indicate neutral sentiment
    plt.xlim(-1, 1)  # Set limits for x-axis
    plt.show()

# Main function to execute the analysis
def main(api_key, crop_name):
    print(f"Fetching articles for: {crop_name}")
    articles = fetch_gnews(api_key, crop_name)
    sentiments = analyze_sentiment(articles)

    # Print the results
    if sentiments:
        for sentiment in sentiments:
            print(f"Title: {sentiment['title']}, Sentiment Polarity: {sentiment['sentiment']}")
    else:
        print(f"No valid sentiments for articles related to {crop_name}.")

    # Visualize the results
    visualize_sentiment(sentiments, crop_name)

# Use your actual GNews API key and query
if __name__ == "_main_":
    api_key = 'f9aac976717adb0c2ad9cc98bfd6348e'  # Your actual GNews API key
    crop_name = 'rice agriculture'  # Refined query for better results
    main(api_key, crop_name)

    # You can also call main again for 'crop' or other queries if needed
    # main(api_key, 'crop')