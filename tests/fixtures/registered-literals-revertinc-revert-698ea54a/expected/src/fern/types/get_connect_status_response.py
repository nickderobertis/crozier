

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_status import ConnectionStatus


class GetConnectStatusResponse(UniversalBaseModel):
    public_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="publicToken"), pydantic.Field(alias="publicToken")
    ]
    status: ConnectionStatus
    integration_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="integrationName"), pydantic.Field(alias="integrationName")
    ]
    tenant_id: typing_extensions.Annotated[str, FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")]
    tenant_secret_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tenantSecretToken"), pydantic.Field(alias="tenantSecretToken")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
