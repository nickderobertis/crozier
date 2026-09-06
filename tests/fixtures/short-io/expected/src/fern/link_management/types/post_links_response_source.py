

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinksResponseSource(enum.StrEnum):
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
        if self is PostLinksResponseSource.WEBSITE:
            return website()
        if self is PostLinksResponseSource.API:
            return api()
        if self is PostLinksResponseSource.PUBLIC:
            return public()
        if self is PostLinksResponseSource.SPREADSHEETS:
            return spreadsheets()
        if self is PostLinksResponseSource.SLACK:
            return slack()
        if self is PostLinksResponseSource.TELEGRAM:
            return telegram()
        if self is PostLinksResponseSource.EMPTY:
            return empty()
