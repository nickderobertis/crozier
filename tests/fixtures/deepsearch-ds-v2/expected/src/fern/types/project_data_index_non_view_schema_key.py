

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectDataIndexNonViewSchemaKey(enum.StrEnum):
    DEEPSEARCH_DOC = "deepsearch-doc"
    DEEPSEARCH_DB = "deepsearch-db"
    GENERIC = "generic"

    def visit(
        self,
        deepsearch_doc: typing.Callable[[], T_Result],
        deepsearch_db: typing.Callable[[], T_Result],
        generic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectDataIndexNonViewSchemaKey.DEEPSEARCH_DOC:
            return deepsearch_doc()
        if self is ProjectDataIndexNonViewSchemaKey.DEEPSEARCH_DB:
            return deepsearch_db()
        if self is ProjectDataIndexNonViewSchemaKey.GENERIC:
            return generic()
