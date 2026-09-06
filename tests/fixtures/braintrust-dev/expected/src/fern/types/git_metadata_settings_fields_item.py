

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GitMetadataSettingsFieldsItem(enum.StrEnum):
    COMMIT = "commit"
    BRANCH = "branch"
    TAG = "tag"
    DIRTY = "dirty"
    AUTHOR_NAME = "author_name"
    AUTHOR_EMAIL = "author_email"
    COMMIT_MESSAGE = "commit_message"
    COMMIT_TIME = "commit_time"
    GIT_DIFF = "git_diff"

    def visit(
        self,
        commit: typing.Callable[[], T_Result],
        branch: typing.Callable[[], T_Result],
        tag: typing.Callable[[], T_Result],
        dirty: typing.Callable[[], T_Result],
        author_name: typing.Callable[[], T_Result],
        author_email: typing.Callable[[], T_Result],
        commit_message: typing.Callable[[], T_Result],
        commit_time: typing.Callable[[], T_Result],
        git_diff: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GitMetadataSettingsFieldsItem.COMMIT:
            return commit()
        if self is GitMetadataSettingsFieldsItem.BRANCH:
            return branch()
        if self is GitMetadataSettingsFieldsItem.TAG:
            return tag()
        if self is GitMetadataSettingsFieldsItem.DIRTY:
            return dirty()
        if self is GitMetadataSettingsFieldsItem.AUTHOR_NAME:
            return author_name()
        if self is GitMetadataSettingsFieldsItem.AUTHOR_EMAIL:
            return author_email()
        if self is GitMetadataSettingsFieldsItem.COMMIT_MESSAGE:
            return commit_message()
        if self is GitMetadataSettingsFieldsItem.COMMIT_TIME:
            return commit_time()
        if self is GitMetadataSettingsFieldsItem.GIT_DIFF:
            return git_diff()
