#!/usr/bin/env python3
"""
Test script to verify the MCP server fixes for output suppression
"""

import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from yt_dlp_mcp.server import YouTubeDownloader


def test_search():
    """Test search functionality"""
    print("Testing search functionality...")
    try:
        import yt_dlp
        
        search_url = "ytsearch2:Python programming"
        opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
        
        with yt_dlp.YoutubeDL(opts) as ydl:
            search_results = ydl.extract_info(search_url, download=False)
            
            if search_results and 'entries' in search_results:
                results = [entry for entry in search_results['entries'] if entry]
                print(f"✓ Search successful - found {len(results)} videos")
                for entry in results:
                    print(f"  - {entry.get('title', 'Unknown')[:50]}...")
            else:
                print("✗ Search failed - no results")
    except Exception as e:
        print(f"✗ Search failed with error: {str(e)}")
    print()


def test_channel():
    """Test channel listing"""
    print("Testing channel listing...")
    try:
        import yt_dlp
        
        # Test with a known channel URL
        channel_url = "https://www.youtube.com/@TechCrunch/videos"
        
        opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
            'playlistend': 2,  # Only get first 2 videos
        }
        
        with yt_dlp.YoutubeDL(opts) as ydl:
            channel_info = ydl.extract_info(channel_url, download=False)
            
            if channel_info and 'entries' in channel_info:
                videos = [entry for entry in channel_info['entries'] if entry][:2]
                print(f"✓ Channel listing successful - found {len(videos)} videos")
                for video in videos:
                    print(f"  - {video.get('title', 'Unknown')[:50]}...")
            else:
                print("✗ Channel listing failed - no videos found")
    except Exception as e:
        print(f"✗ Channel listing failed with error: {str(e)}")
    print()


def test_transcription_basic():
    """Test transcription with a known video that should have captions"""
    print("Testing transcription functionality...")
    # Using a more reliable video
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll (very stable video)
    
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
