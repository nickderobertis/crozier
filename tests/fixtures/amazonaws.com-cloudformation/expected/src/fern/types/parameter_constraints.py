

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .allowed_value import AllowedValue


class ParameterConstraints(UniversalBaseModel):
    """
    A set of criteria that CloudFormation uses to validate parameter values. Although other constraints might be defined in the stack template, CloudFormation returns only the <code>AllowedValues</code> property.
    """

    allowed_values: typing_extensions.Annotated[
        typing.Optional[typing.List[AllowedValue]],
        FieldMetadata(alias="AllowedValues"),
        pydantic.Field(alias="AllowedValues", description="A list of values that are permitted for a parameter."),
    ] = None
    """
    A list of values that are permitted for a parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
