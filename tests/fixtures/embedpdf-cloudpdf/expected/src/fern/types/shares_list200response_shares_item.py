

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SharesList200ResponseSharesItem(UniversalBaseModel):
    id: str
    tenant_id: typing_extensions.Annotated[str, FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")]
    doc_id: typing_extensions.Annotated[str, FieldMetadata(alias="docId"), pydantic.Field(alias="docId")]
    layer_name: typing_extensions.Annotated[str, FieldMetadata(alias="layerName"), pydantic.Field(alias="layerName")]
    scope: typing.List[str]
    origins: typing.Optional[typing.List[str]] = None
    password_protected: typing_extensions.Annotated[
        bool, FieldMetadata(alias="passwordProtected"), pydantic.Field(alias="passwordProtected")
    ]
    session_ttl_seconds: typing_extensions.Annotated[
        float, FieldMetadata(alias="sessionTtlSeconds"), pydantic.Field(alias="sessionTtlSeconds")
    ]
    disabled: bool
    expires_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    exchange_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="exchangeCount"), pydantic.Field(alias="exchangeCount")
    ]
    last_exchanged_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastExchangedAt"), pydantic.Field(alias="lastExchangedAt")
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    created_at: typing_extensions.Annotated[float, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[float, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
