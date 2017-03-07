import praw

basePlaylistURL = "http://www.youtube.com/watch_videos?video_ids="

reddit = praw.Reddit(client_id= 'Ja128FF6XxyzWg',
                    client_secret='Lw1VYSTkFGP6VG8VavKgovG18cQ',
                    password= 'YTPlaylists',
                    user_agent= 'test crawler',
                    username= 'youTubePlaylistMaker')

print(reddit.user.me())

listenToThis = reddit.subreddit('listentothis')

for submission in listenToThis.hot(limit=100):
    print(submission.title)  # Output: the submission's title
    print(submission.url)    # Output: the URL the submission points to
    if "youtube" in submission.url:
        if "v=" in submission.url:
            urlSplit = submission.url.split("v=");
            basePlaylistURL = basePlaylistURL + urlSplit[1] + ','


print(basePlaylistURL)
