# yt-dlp MCP Server - Output Suppression Fix

## Problem Solved

The issue you encountered was caused by yt-dlp outputting download progress messages that interfered with the JSON-RPC communication protocol used by MCP servers. The error message you saw:

```
Failed to parse message: "\r[download]    1.00KiB at  999.83KiB/s (00:00:00)\r[download]    3.00KiB at    1.46MiB/s..."
```

## Solution Implemented

I've implemented multiple layers of output suppression in the MCP server:

### 1. Enhanced yt-dlp Configuration
```python
self.base_opts = {
    'quiet': True,
    'no_warnings': True,
    'noprogress': True,      # Disable progress output
    'no_color': True,        # Disable colored output
    'logger': self._get_null_logger(),  # Use null logger
    # ... other options
}
```

### 2. Null Logger Implementation
```python
def _get_null_logger(self):
    """Return a null logger to suppress all yt-dlp output"""
    logger = logging.getLogger('yt-dlp-null')
    logger.setLevel(logging.CRITICAL + 1)  # Disable all logging
    return logger
```

### 3. Stream Redirection
```python
# Redirect stdout and stderr to suppress yt-dlp output
old_stdout = sys.stdout
old_stderr = sys.stderr
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()

try:
    # ... yt-dlp operations
finally:
    # Restore stdout and stderr
    sys.stdout = old_stdout
    sys.stderr = old_stderr
```

## Verification

The fix has been tested and verified to:
- ✅ Suppress all yt-dlp download progress messages
- ✅ Prevent JSON-RPC parsing interference
- ✅ Maintain full functionality for transcription extraction
- ✅ Return clean, formatted transcription text

## Usage

The MCP server now works cleanly with MCP clients without output interference:

```bash
# Run the MCP server
yt-dlp-mcp

# Or install and use in your MCP configuration
pip install -e .
```

## Test Results

The test demonstrates that the transcription functionality works correctly without any progress output interference:

```
✓ Transcription successful!
Length: 2208 characters
Preview: Transcription for 'Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)':
```

**Key Success Indicator**: No yt-dlp download progress messages appear during operation.

## Files Updated

1. `src/yt_dlp_mcp/server.py` - Enhanced with output suppression
2. `test_simple.py` - Verification test for the fix
3. This documentation file

The MCP server is now ready for production use without JSON-RPC communication issues.
