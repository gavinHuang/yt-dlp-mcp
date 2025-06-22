#!/usr/bin/env python3
"""
Test to isolate the proxies issue with youtube-search-python
"""

try:
    from youtubesearchpython import VideosSearch, ChannelsSearch, Channel
    print("Import successful")
    
    # Test search
    print("Testing VideosSearch...")
    try:
        videos_search = VideosSearch("test", limit=1)
        results = videos_search.result()
        print("VideosSearch succeeded")
    except Exception as e:
        print(f"VideosSearch failed: {e}")
    
    # Test channel search
    print("Testing ChannelsSearch...")
    try:
        channel_search = ChannelsSearch("test", limit=1)
        results = channel_search.result()
        print("ChannelsSearch succeeded")
    except Exception as e:
        print(f"ChannelsSearch failed: {e}")
    
    # Test channel get
    print("Testing Channel.get...")
    try:
        channel = Channel.get("UC_x5XG1OV2P6uZZ5FSM9Ttw")  # Google Developers channel
        print("Channel.get succeeded")
    except Exception as e:
        print(f"Channel.get failed: {e}")
        
except Exception as e:
    print(f"Import failed: {e}")
