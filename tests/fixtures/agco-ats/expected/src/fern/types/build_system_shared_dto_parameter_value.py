

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_parameter_value_direction import BuildSystemSharedDtoParameterValueDirection


class BuildSystemSharedDtoParameterValue(UniversalBaseModel):
    """
    A DTO for an IParameterValue
    """

    direction: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedDtoParameterValueDirection],
        FieldMetadata(alias="Direction"),
        pydantic.Field(alias="Direction", description="The parameter direction (Input or Output)"),
    ] = None
    """
    The parameter direction (Input or Output)
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the parameter this value is for"),
    ] = None
    """
    The name of the parameter this value is for
    """

    value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Value"),
        pydantic.Field(alias="Value", description="The parameter value in string representation"),
    ] = None
    """
    The parameter value in string representation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
