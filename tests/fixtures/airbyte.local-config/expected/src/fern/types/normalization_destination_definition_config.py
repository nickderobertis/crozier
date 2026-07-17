

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NormalizationDestinationDefinitionConfig(UniversalBaseModel):
    """
    describes a normalization config for destination definition
    """

    normalization_integration_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="normalizationIntegrationType"),
        pydantic.Field(
            alias="normalizationIntegrationType",
            description="a field indicating the type of integration dialect to use for normalization.",
        ),
    ] = None
    """
    a field indicating the type of integration dialect to use for normalization.
    """

    normalization_repository: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="normalizationRepository"),
        pydantic.Field(
            alias="normalizationRepository",
            description="a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used.",
        ),
    ] = None
    """
    a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used.
    """

    normalization_tag: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="normalizationTag"),
        pydantic.Field(
            alias="normalizationTag",
            description="a field indicating the tag of the docker repository to be used for normalization.",
        ),
    ] = None
    """
    a field indicating the tag of the docker repository to be used for normalization.
    """

    supported: bool = pydantic.Field()
    """
    whether the destination definition supports normalization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
