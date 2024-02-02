from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url,
        use_oauth=False,
        allow_oauth_cache=True)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.first()
    
    # Download the video to the current directory
    yd.download('Downloads')
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))