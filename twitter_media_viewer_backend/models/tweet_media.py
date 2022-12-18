class TweetMedia:
    def __init__(self, tweet_id, attached_media_id, attached_media=None) -> None:
        self.tweet_id: int = tweet_id
        self.attached_media_id: str = attached_media_id
        self.attached_media: AttachedMedia | None = attached_media



class AttachedMedia:
    def __init__(self, media_id=None, medias=None) -> None:
        self.media_id: str = media_id
        self.medias = medias