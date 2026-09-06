

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationEventName(enum.StrEnum):
    """
    The name of the event the notification will fire on.
    """

    ON_PODCAST_EPISODE_DOWNLOADED = "onPodcastEpisodeDownloaded"
    ON_BACKUP_COMPLETED = "onBackupCompleted"
    ON_BACKUP_FAILED = "onBackupFailed"
    ON_TEST = "onTest"

    def visit(
        self,
        on_podcast_episode_downloaded: typing.Callable[[], T_Result],
        on_backup_completed: typing.Callable[[], T_Result],
        on_backup_failed: typing.Callable[[], T_Result],
        on_test: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationEventName.ON_PODCAST_EPISODE_DOWNLOADED:
            return on_podcast_episode_downloaded()
        if self is NotificationEventName.ON_BACKUP_COMPLETED:
            return on_backup_completed()
        if self is NotificationEventName.ON_BACKUP_FAILED:
            return on_backup_failed()
        if self is NotificationEventName.ON_TEST:
            return on_test()
