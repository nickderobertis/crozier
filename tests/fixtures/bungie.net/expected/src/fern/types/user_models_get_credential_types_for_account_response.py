

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserModelsGetCredentialTypesForAccountResponse(UniversalBaseModel):
    credential_as_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="credentialAsString"), pydantic.Field(alias="credentialAsString")
    ] = None
    credential_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="credentialDisplayName"),
        pydantic.Field(alias="credentialDisplayName"),
    ] = None
    credential_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="credentialType"), pydantic.Field(alias="credentialType")
    ] = None
    is_public: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPublic"), pydantic.Field(alias="isPublic")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
