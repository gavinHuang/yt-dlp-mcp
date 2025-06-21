#!/usr/bin/env python3
"""
Simple test for transcription functionality with a known working video
"""

import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from yt_dlp_mcp.server import YouTubeDownloader


def test_transcription_simple():
    """Test transcription with a popular video that likely has captions"""
    print("Testing transcription functionality...")
    # Using a very popular, likely captioned video
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll - very popular, likely has captions
    
    print(f"Getting transcription for: {test_url}")
    print("This should complete without showing download progress...")
    print("-" * 50)
    
    try:
        downloader = YouTubeDownloader()
        result = downloader.get_transcription(test_url, keep_timestamps=False)
        
        print("-" * 50)
        if "Error" not in result and "No transcription available" not in result:
            print("✓ Transcription successful!")
            print(f"Length: {len(result)} characters")
            print(f"Preview: {result[:150]}...")
        else:
            print("! Transcription result:")
            print(f"  {result[:200]}...")
    except Exception as e:
        print(f"✗ Transcription failed with error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("Key success indicator: No yt-dlp download progress should have appeared!")


if __name__ == "__main__":
    print("yt-dlp MCP Server - Output Suppression Test")
    print("=" * 50)
    test_transcription_simple()
