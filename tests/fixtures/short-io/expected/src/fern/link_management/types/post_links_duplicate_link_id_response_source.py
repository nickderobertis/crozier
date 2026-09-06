

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinksDuplicateLinkIdResponseSource(enum.StrEnum):
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
        if self is PostLinksDuplicateLinkIdResponseSource.WEBSITE:
            return website()
        if self is PostLinksDuplicateLinkIdResponseSource.API:
            return api()
        if self is PostLinksDuplicateLinkIdResponseSource.PUBLIC:
            return public()
        if self is PostLinksDuplicateLinkIdResponseSource.SPREADSHEETS:
            return spreadsheets()
        if self is PostLinksDuplicateLinkIdResponseSource.SLACK:
            return slack()
        if self is PostLinksDuplicateLinkIdResponseSource.TELEGRAM:
            return telegram()
        if self is PostLinksDuplicateLinkIdResponseSource.EMPTY:
            return empty()
