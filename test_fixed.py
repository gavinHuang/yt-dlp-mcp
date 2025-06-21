#!/usr/bin/env python3
"""
Test script to verify the MCP server fixes for output suppression
"""

import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from yt_dlp_mcp.server import YouTubeDownloader
from youtubesearchpython import VideosSearch, ChannelsSearch, Channel


def test_search():
    """Test search functionality"""
    print("Testing search functionality...")
    try:
        videos_search = VideosSearch("Python programming", limit=2)
        results = videos_search.result()
        
        if results and results.get('result'):
            print(f"✓ Search successful - found {len(results['result'])} videos")
            for video in results['result']:
                print(f"  - {video.get('title', 'Unknown')[:50]}...")
        else:
            print("✗ Search failed - no results")
    except Exception as e:
        print(f"✗ Search failed with error: {str(e)}")
    print()


def test_channel():
    """Test channel listing"""
    print("Testing channel listing...")
    try:
        channel_search = ChannelsSearch("TechCrunch", limit=1)
        channel_results = channel_search.result()
        
        if channel_results and channel_results.get('result'):
            channel_id = channel_results['result'][0]['id']
            channel = Channel.get(channel_id)
            
            if channel and channel.get('videos'):
                videos = list(channel['videos'])[:2]  # Get first 2 videos
                print(f"✓ Channel listing successful - found {len(videos)} videos")
                for video in videos:
                    print(f"  - {video.get('title', 'Unknown')[:50]}...")
            else:
                print("✗ Could not get channel videos")
        else:
            print("✗ Channel not found")
    except Exception as e:
        print(f"✗ Channel listing failed with error: {str(e)}")
    print()


def test_transcription_basic():
    """Test transcription with a known video that should have captions"""
    print("Testing transcription functionality...")
    # Using a TED Talk which typically has captions
    test_url = "https://www.youtube.com/watch?v=HyQmDsaoqJU"  # Example TED Talk
    
    print(f"Getting transcription for: {test_url}")
    
    try:
        downloader = YouTubeDownloader()
        result = downloader.get_transcription(test_url, keep_timestamps=False)
        
        if "Error" not in result and "No transcription available" not in result:
            print("✓ Transcription successful")
            print(f"Preview (first 100 chars): {result[:100]}...")
        else:
            print("! Transcription issue (this may be normal if video has no captions)")
            print(f"Result: {result[:200]}...")
    except Exception as e:
        print(f"✗ Transcription failed with error: {str(e)}")
    print()


if __name__ == "__main__":
    print("yt-dlp MCP Server - Fixed Output Test")
    print("=" * 45)
    
    test_search()
    test_channel()
    test_transcription_basic()
    
    print("=" * 45)
    print("Test completed!")
    print("\nIf no download progress messages appeared above,")
    print("the output suppression fix was successful!")
