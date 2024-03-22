from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# Example list of RSS/XML feed URLs
feed_urls = [
    'http://example.com/feed1.xml',
    'http://example.com/feed2.xml',
    # Add more feed URLs as needed
]

@app.route('/')
def index():
    # Initialize an empty list to store aggregated feed entries
    aggregated_entries = []

    # Iterate through each feed URL
    for url in feed_urls:
        # Parse the feed
        feed = feedparser.parse(url)

        # Extract relevant information from each entry
        for entry in feed.entries:
            # Extract title, publish date, and any other relevant information
            title = entry.title
            publish_date = entry.published
            author = "Unknown"  # You can assign a default author if it's not provided in the feed

            # Append the extracted information to the aggregated list
            aggregated_entries.append({
                'title': title,
                'publish_date': publish_date,
                'author': author
            })

    # Sort the aggregated entries by publish date
    aggregated_entries = sorted(aggregated_entries, key=lambda x: x['publish_date'], reverse=True)

    # Render the template with the aggregated entries
    return render_template('index.html', entries=aggregated_entries)

if __name__ == '__main__':
    app.run(debug=True)
