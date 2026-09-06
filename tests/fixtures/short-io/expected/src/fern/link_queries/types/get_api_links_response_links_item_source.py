

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiLinksResponseLinksItemSource(enum.StrEnum):
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
        if self is GetApiLinksResponseLinksItemSource.WEBSITE:
            return website()
        if self is GetApiLinksResponseLinksItemSource.API:
            return api()
        if self is GetApiLinksResponseLinksItemSource.PUBLIC:
            return public()
        if self is GetApiLinksResponseLinksItemSource.SPREADSHEETS:
            return spreadsheets()
        if self is GetApiLinksResponseLinksItemSource.SLACK:
            return slack()
        if self is GetApiLinksResponseLinksItemSource.TELEGRAM:
            return telegram()
        if self is GetApiLinksResponseLinksItemSource.EMPTY:
            return empty()
