

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApi2ThesaurusLevelIntRequestLevel(enum.StrEnum):
    DOMAIN = "domain"
    SUBDOMAIN = "subdomain"
    CONCEPT = "concept"

    def visit(
        self,
        domain: typing.Callable[[], T_Result],
        subdomain: typing.Callable[[], T_Result],
        concept: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApi2ThesaurusLevelIntRequestLevel.DOMAIN:
            return domain()
        if self is GetApi2ThesaurusLevelIntRequestLevel.SUBDOMAIN:
            return subdomain()
        if self is GetApi2ThesaurusLevelIntRequestLevel.CONCEPT:
            return concept()
