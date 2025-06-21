#!/usr/bin/env python3
"""
Test script for yt-dlp MCP server
"""

import sys
import os

# Add the src directory to the path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from yt_dlp_mcp.server import get_transcription, search_videos, list_channel_videos


def test_search_videos():
    """Test video search functionality"""
    print("Testing video search...")
    results = search_videos("Python programming tutorial", max_results=3)
    
    if results and not results[0].get('error'):
        print(f"Found {len(results)} videos:")
        for i, video in enumerate(results, 1):
            print(f"{i}. {video['title']}")
            print(f"   URL: {video['url']}")
            print(f"   Channel: {video['channel']}")
            print()
    else:
        print("Search failed or no results found")
        if results:
            print(f"Error: {results[0].get('error', 'Unknown error')}")


def test_channel_videos():
    """Test channel video listing"""
    print("Testing channel video listing...")
    # Using a well-known tech channel
    results = list_channel_videos("TechCrunch", max_videos=3)
    
    if results and not results[0].get('error'):
        print(f"Found {len(results)} videos from channel:")
        for i, video in enumerate(results, 1):
            print(f"{i}. {video['title']}")
            print(f"   URL: {video['url']}")
            print(f"   Published: {video['published']}")
            print()
    else:
        print("Channel listing failed")
        if results:
            print(f"Error: {results[0].get('error', 'Unknown error')}")


def test_transcription():
    """Test transcription functionality"""
    print("Testing transcription (this requires a specific video URL)...")
    # Note: This would need a real YouTube URL to test properly
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll as example
    
    print(f"Attempting to get transcription for: {test_url}")
    result = get_transcription(test_url, keep_timestamps=False)
    
    if "Error" not in result:
        print("Transcription successful!")
        print(f"Preview: {result[:200]}...")
    else:
        print(f"Transcription failed: {result}")


if __name__ == "__main__":
    print("yt-dlp MCP Server Test Suite")
    print("=" * 40)
    
    test_search_videos()
    print("\n" + "=" * 40 + "\n")
    
    test_channel_videos()
    print("\n" + "=" * 40 + "\n")
    
    # Uncomment to test transcription with a real URL
    # test_transcription()
    
    print("Test suite completed!")
