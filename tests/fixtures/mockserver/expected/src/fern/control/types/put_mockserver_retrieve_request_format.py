

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverRetrieveRequestFormat(enum.StrEnum):
    JAVA = "java"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    GO = "go"
    CSHARP = "csharp"
    RUBY = "ruby"
    RUST = "rust"
    PHP = "php"
    JSON = "json"
    LOG_ENTRIES = "log_entries"
    HAR = "har"
    OPENAPI = "openapi"
    POSTMAN = "postman"
    BRUNO = "bruno"
    CURL = "curl"

    def visit(
        self,
        java: typing.Callable[[], T_Result],
        javascript: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
        go: typing.Callable[[], T_Result],
        csharp: typing.Callable[[], T_Result],
        ruby: typing.Callable[[], T_Result],
        rust: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        log_entries: typing.Callable[[], T_Result],
        har: typing.Callable[[], T_Result],
        openapi: typing.Callable[[], T_Result],
        postman: typing.Callable[[], T_Result],
        bruno: typing.Callable[[], T_Result],
        curl: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverRetrieveRequestFormat.JAVA:
            return java()
        if self is PutMockserverRetrieveRequestFormat.JAVASCRIPT:
            return javascript()
        if self is PutMockserverRetrieveRequestFormat.PYTHON:
            return python()
        if self is PutMockserverRetrieveRequestFormat.GO:
            return go()
        if self is PutMockserverRetrieveRequestFormat.CSHARP:
            return csharp()
        if self is PutMockserverRetrieveRequestFormat.RUBY:
            return ruby()
        if self is PutMockserverRetrieveRequestFormat.RUST:
            return rust()
        if self is PutMockserverRetrieveRequestFormat.PHP:
            return php()
        if self is PutMockserverRetrieveRequestFormat.JSON:
            return json()
        if self is PutMockserverRetrieveRequestFormat.LOG_ENTRIES:
            return log_entries()
        if self is PutMockserverRetrieveRequestFormat.HAR:
            return har()
        if self is PutMockserverRetrieveRequestFormat.OPENAPI:
            return openapi()
        if self is PutMockserverRetrieveRequestFormat.POSTMAN:
            return postman()
        if self is PutMockserverRetrieveRequestFormat.BRUNO:
            return bruno()
        if self is PutMockserverRetrieveRequestFormat.CURL:
            return curl()
