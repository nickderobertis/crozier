

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaptureRuleSource(enum.StrEnum):
    JSON_PATH = "jsonPath"
    XPATH = "xpath"
    HEADER = "header"
    QUERY_STRING_PARAMETER = "queryStringParameter"
    COOKIE = "cookie"
    PATH_PARAMETER = "pathParameter"

    def visit(
        self,
        json_path: typing.Callable[[], T_Result],
        xpath: typing.Callable[[], T_Result],
        header: typing.Callable[[], T_Result],
        query_string_parameter: typing.Callable[[], T_Result],
        cookie: typing.Callable[[], T_Result],
        path_parameter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaptureRuleSource.JSON_PATH:
            return json_path()
        if self is CaptureRuleSource.XPATH:
            return xpath()
        if self is CaptureRuleSource.HEADER:
            return header()
        if self is CaptureRuleSource.QUERY_STRING_PARAMETER:
            return query_string_parameter()
        if self is CaptureRuleSource.COOKIE:
            return cookie()
        if self is CaptureRuleSource.PATH_PARAMETER:
            return path_parameter()
