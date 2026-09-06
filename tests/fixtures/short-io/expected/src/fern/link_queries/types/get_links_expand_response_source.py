

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLinksExpandResponseSource(enum.StrEnum):
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
        if self is GetLinksExpandResponseSource.WEBSITE:
            return website()
        if self is GetLinksExpandResponseSource.API:
            return api()
        if self is GetLinksExpandResponseSource.PUBLIC:
            return public()
        if self is GetLinksExpandResponseSource.SPREADSHEETS:
            return spreadsheets()
        if self is GetLinksExpandResponseSource.SLACK:
            return slack()
        if self is GetLinksExpandResponseSource.TELEGRAM:
            return telegram()
        if self is GetLinksExpandResponseSource.EMPTY:
            return empty()
