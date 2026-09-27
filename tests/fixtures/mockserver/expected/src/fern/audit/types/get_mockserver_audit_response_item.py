

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_mockserver_audit_response_item_principal_source import GetMockserverAuditResponseItemPrincipalSource


class GetMockserverAuditResponseItem(UniversalBaseModel):
    epoch_time_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="epochTimeMs"), pydantic.Field(alias="epochTimeMs")
    ] = None
    method: typing.Optional[str] = None
    path: typing.Optional[str] = None
    operation: typing.Optional[str] = None
    source_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceAddress"), pydantic.Field(alias="sourceAddress")
    ] = None
    principal: typing.Optional[str] = None
    principal_source: typing_extensions.Annotated[
        typing.Optional[GetMockserverAuditResponseItemPrincipalSource],
        FieldMetadata(alias="principalSource"),
        pydantic.Field(alias="principalSource"),
    ] = None
    outcome: typing.Optional[str] = None
    summary: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
