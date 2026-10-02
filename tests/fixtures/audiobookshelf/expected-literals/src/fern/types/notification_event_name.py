

import typing

NotificationEventName = typing.Union[
    typing.Literal["onPodcastEpisodeDownloaded", "onBackupCompleted", "onBackupFailed", "onTest"], typing.Any
]
