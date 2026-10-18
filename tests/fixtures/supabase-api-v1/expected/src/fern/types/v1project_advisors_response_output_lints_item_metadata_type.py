

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectAdvisorsResponseOutputLintsItemMetadataType(enum.StrEnum):
    TABLE = "table"
    VIEW = "view"
    MATERIALIZED_VIEW = "materialized view"
    FOREIGN_TABLE = "foreign table"
    AUTH = "auth"
    FUNCTION = "function"
    EXTENSION = "extension"
    COMPLIANCE = "compliance"
    HEALTH = "health"

    def visit(
        self,
        table: typing.Callable[[], T_Result],
        view: typing.Callable[[], T_Result],
        materialized_view: typing.Callable[[], T_Result],
        foreign_table: typing.Callable[[], T_Result],
        auth: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
        extension: typing.Callable[[], T_Result],
        compliance: typing.Callable[[], T_Result],
        health: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.TABLE:
            return table()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.VIEW:
            return view()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.MATERIALIZED_VIEW:
            return materialized_view()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.FOREIGN_TABLE:
            return foreign_table()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.AUTH:
            return auth()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.FUNCTION:
            return function()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.EXTENSION:
            return extension()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.COMPLIANCE:
            return compliance()
        if self is V1ProjectAdvisorsResponseOutputLintsItemMetadataType.HEALTH:
            return health()
