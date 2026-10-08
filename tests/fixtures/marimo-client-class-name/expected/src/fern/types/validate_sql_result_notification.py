

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sql_catalog_check_result import SqlCatalogCheckResult
from .sql_parse_result import SqlParseResult
from .validate_sql_result_notification_op import ValidateSqlResultNotificationOp


class ValidateSqlResultNotification(UniversalBaseModel):
    """
    SQL query validation result.

        Attributes:
            request_id: Request ID this responds to.
            parse_result: SQL parsing result.
            validate_result: Catalog validation result.
            error: Error message if failed.
    """

    error: typing.Optional[str] = None
    op: ValidateSqlResultNotificationOp
    parse_result: typing.Optional[SqlParseResult] = None
    request_id: str
    validate_result: typing.Optional[SqlCatalogCheckResult] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
