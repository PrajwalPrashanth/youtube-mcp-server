# server.py
from mcp.server.fastmcp import FastMCP
from mcp.types import AnyUrl
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

# Create an MCP server
mcp = FastMCP("youtube-mcp-server")

@mcp.tool()
def get_youtube_transcript(url: AnyUrl) -> str:
    """
    Get transcript for a YouTube video URL in full text format.
    """
    # Extract video ID from URL using path and query components
    video_id = dict(url.query_params())["v"]
    if not video_id:
        raise ValueError("Invalid YouTube URL - missing video ID")
    
    # Get transcript and convert to full text
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    return full_text