

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_status_status import QueryStatusStatus


class QueryResponse_StoreQueryV1(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Literal["store.query.v1"], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = "store.query.v1"
    scope_id: str
    rows: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QueryResponse_StoreStatusV1(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Literal["store.status.v1"], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = "store.status.v1"
    scope_id: str
    status: QueryStatusStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


QueryResponse = typing_extensions.Annotated[
    typing.Union[QueryResponse_StoreQueryV1, QueryResponse_StoreStatusV1], pydantic.Field(discriminator="schema")
]
