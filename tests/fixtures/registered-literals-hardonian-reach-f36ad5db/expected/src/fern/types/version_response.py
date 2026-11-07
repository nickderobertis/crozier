

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .version_response_compatibility_policy import VersionResponseCompatibilityPolicy


class VersionResponse(UniversalBaseModel):
    api_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="apiVersion"),
        pydantic.Field(alias="apiVersion", description="The API implementation version"),
    ]
    """
    The API implementation version
    """

    spec_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="specVersion"),
        pydantic.Field(alias="specVersion", description="The OpenAPI spec version"),
    ]
    """
    The OpenAPI spec version
    """

    compatibility_policy: typing_extensions.Annotated[
        typing.Optional[VersionResponseCompatibilityPolicy],
        FieldMetadata(alias="compatibilityPolicy"),
        pydantic.Field(alias="compatibilityPolicy"),
    ] = None
    supported_versions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="supportedVersions"),
        pydantic.Field(alias="supportedVersions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
