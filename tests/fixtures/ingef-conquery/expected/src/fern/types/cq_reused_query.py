

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .cq_element_base import CqElementBase
from .execution_id import ExecutionId


class CqReusedQuery(CqElementBase):
    """
    Allows the reuse of an existing query, by referencing execution of that query by its Id.
    """

    query_id: typing_extensions.Annotated[
        typing.Optional[ExecutionId], FieldMetadata(alias="queryId"), pydantic.Field(alias="queryId")
    ] = None
    exclude_from_secondary_id: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="excludeFromSecondaryId"),
        pydantic.Field(
            alias="excludeFromSecondaryId",
            description="If the query is reused within a SECONDARY_ID query, it will not be executed with the secondary-Id set.",
        ),
    ] = None
    """
    If the query is reused within a SECONDARY_ID query, it will not be executed with the secondary-Id set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
