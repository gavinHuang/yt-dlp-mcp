# yt-dlp MCP Server Usage Examples

This document provides examples of how to use the yt-dlp MCP server tools.

## Tool Examples

### 1. Get Transcription

```python
# Get transcription without timestamps
result = get_transcription("https://www.youtube.com/watch?v=VIDEO_ID")

# Get transcription with timestamps
result = get_transcription("https://www.youtube.com/watch?v=VIDEO_ID", keep_timestamps=True)
```

**Example Output:**
```
Transcription for 'Python Tutorial - Variables and Data Types':

Welcome to this Python tutorial. Today we'll be learning about variables and data types.
In Python, you can create a variable by simply assigning a value to it.
For example, you can write: name = "John"
This creates a string variable called name with the value "John".
...
```

### 2. Search Videos

```python
# Search for Python tutorials
results = search_videos("Python programming tutorial", max_results=5)

# Search for specific topic
results = search_videos("machine learning basics", max_results=10)
```

**Example Output:**
```python
[
    {
        "title": "Python Programming Tutorial - Learn Python in 4 Hours",
        "url": "https://www.youtube.com/watch?v=rfscVS0vtbw",
        "description": "Learn Python programming in this complete course for beginners...",
        "duration": "4:26:52",
        "views": "2.5M views",
        "channel": "freeCodeCamp.org"
    },
    {
        "title": "Python Tutorial for Beginners - Full Course",
        "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
        "description": "Python tutorial for beginners. Learn Python programming...",
        "duration": "6:14:07",
        "views": "8.2M views",
        "channel": "Programming with Mosh"
    }
]
```

### 3. List Channel Videos

```python
# Get recent videos from a channel by name
results = list_channel_videos("TechCrunch", max_videos=5)

# Get videos from a channel by handle
results = list_channel_videos("@mkbhd", max_videos=10)

# Get videos from a channel by ID
results = list_channel_videos("UCBJycsmduvYEL83R_U4JriQ", max_videos=3)
```

**Example Output:**
```python
[
    {
        "title": "Apple's New MacBook Pro M3 - First Look",
        "url": "https://www.youtube.com/watch?v=VIDEO_ID1",
        "description": "Apple just announced the new MacBook Pro with M3 chip...",
        "duration": "10:15",
        "views": "125K views",
        "published": "2 days ago"
    },
    {
        "title": "Tesla Cybertruck Production Update",
        "url": "https://www.youtube.com/watch?v=VIDEO_ID2",
        "description": "Latest updates on Tesla Cybertruck production timeline...",
        "duration": "8:30",
        "views": "89K views",
        "published": "5 days ago"
    }
]
```

## Error Handling

All tools include error handling and will return error messages when something goes wrong:

```python
# If video is private or unavailable
result = get_transcription("https://www.youtube.com/watch?v=INVALID_ID")
# Returns: "Error getting transcription: Video unavailable"

# If channel doesn't exist
result = list_channel_videos("NonExistentChannel123")
# Returns: [{"error": "Channel 'NonExistentChannel123' not found"}]

# If search fails
result = search_videos("")
# Returns: [{"error": "Search failed: Empty search query"}]
```

## Tips

1. **For transcriptions**: Not all videos have available transcripts. The tool will automatically try to get English captions (manual or auto-generated).

2. **For channel searches**: You can use different formats:
   - Channel name: "TechCrunch"
   - Channel handle: "@mkbhd"
   - Channel ID: "UCBJycsmduvYEL83R_U4JriQ"
   - Channel URL: "https://www.youtube.com/c/TechCrunch"

3. **For video searches**: Use specific keywords for better results. The more specific your search terms, the more relevant the results will be.

4. **Rate limiting**: Be mindful of making too many requests in quick succession to avoid being rate-limited by YouTube.
