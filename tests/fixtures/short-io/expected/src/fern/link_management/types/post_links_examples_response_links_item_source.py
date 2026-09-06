

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinksExamplesResponseLinksItemSource(enum.StrEnum):
    """
    Link source
    """

    WEBSITE = "website"
    API = "api"
    PUBLIC = "public"
    SPREADSHEETS = "spreadsheets"
    SLACK = "slack"
    TELEGRAM = "telegram"
    EMPTY = ""

    def visit(
        self,
        website: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
        spreadsheets: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
        telegram: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostLinksExamplesResponseLinksItemSource.WEBSITE:
            return website()
        if self is PostLinksExamplesResponseLinksItemSource.API:
            return api()
        if self is PostLinksExamplesResponseLinksItemSource.PUBLIC:
            return public()
        if self is PostLinksExamplesResponseLinksItemSource.SPREADSHEETS:
            return spreadsheets()
        if self is PostLinksExamplesResponseLinksItemSource.SLACK:
            return slack()
        if self is PostLinksExamplesResponseLinksItemSource.TELEGRAM:
            return telegram()
        if self is PostLinksExamplesResponseLinksItemSource.EMPTY:
            return empty()
