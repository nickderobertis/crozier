

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanEgressRoutesItemAdditionalCredentialHeadersItemCredentialResolverIntegrationConnection(
    UniversalBaseModel
):
    connection_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ]
    secret_type: typing_extensions.Annotated[str, FieldMetadata(alias="secretType"), pydantic.Field(alias="secretType")]
    slot_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="slotKey"), pydantic.Field(alias="slotKey")
    ] = None
    resolver_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resolverKey"), pydantic.Field(alias="resolverKey")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
