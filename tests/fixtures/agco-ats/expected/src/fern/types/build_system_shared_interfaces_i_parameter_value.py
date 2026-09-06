

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_interfaces_i_parameter_value_direction import (
    BuildSystemSharedInterfacesIParameterValueDirection,
)


class BuildSystemSharedInterfacesIParameterValue(UniversalBaseModel):
    """
    Declares members that must be implemented by parameter value objects.
    """

    direction: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedInterfacesIParameterValueDirection],
        FieldMetadata(alias="Direction"),
        pydantic.Field(
            alias="Direction",
            description="Gets or sets a value indicating whether the parameter value is an \r\n            input to the build part or an output from the build part.",
        ),
    ] = None
    """
    Gets or sets a value indicating whether the parameter value is an 
                input to the build part or an output from the build part.
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="Gets or sets the name of the parameter."),
    ] = None
    """
    Gets or sets the name of the parameter.
    """

    value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Value"),
        pydantic.Field(alias="Value", description="Gets or sets the value of the parameter."),
    ] = None
    """
    Gets or sets the value of the parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
