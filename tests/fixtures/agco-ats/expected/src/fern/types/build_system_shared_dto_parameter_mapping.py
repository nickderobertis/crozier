

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_parameter_mapping_source_type import BuildSystemSharedDtoParameterMappingSourceType


class BuildSystemSharedDtoParameterMapping(UniversalBaseModel):
    """
    A DTO for an IParameterMapping
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the parameter this mapping applies to"),
    ] = None
    """
    The name of the parameter this mapping applies to
    """

    source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Source"),
        pydantic.Field(
            alias="Source",
            description="The source of the value.  The meaning of this value is determined by the source type.  When the source type is “Constant” then source is the value formatted as a string.  When the source type is “Variable” then the source is the name of the variable",
        ),
    ] = None
    """
    The source of the value.  The meaning of this value is determined by the source type.  When the source type is “Constant” then source is the value formatted as a string.  When the source type is “Variable” then the source is the name of the variable
    """

    source_type: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedDtoParameterMappingSourceType],
        FieldMetadata(alias="SourceType"),
        pydantic.Field(alias="SourceType", description="The source type used for supplying the parameter"),
    ] = None
    """
    The source type used for supplying the parameter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
