

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_parameter_direction import BuildSystemSharedDtoParameterDirection
from .build_system_shared_dto_parameter_type import BuildSystemSharedDtoParameterType


class BuildSystemSharedDtoParameter(UniversalBaseModel):
    """
    A DTO for an IParameter
    """

    direction: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedDtoParameterDirection],
        FieldMetadata(alias="Direction"),
        pydantic.Field(alias="Direction", description="The parameter direction (Input or Output)"),
    ] = None
    """
    The parameter direction (Input or Output)
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the parameter"),
    ] = None
    """
    The name of the parameter
    """

    type: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedDtoParameterType],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The data type of the parameter"),
    ] = None
    """
    The data type of the parameter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
