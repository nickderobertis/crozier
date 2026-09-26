

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolsGetResponseDataToolsItemParametersItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Parameter name
    """

    type: str = pydantic.Field()
    """
    Parameter type (string, number, boolean, object, array)
    """

    description: str = pydantic.Field()
    """
    Parameter description
    """

    required: bool = pydantic.Field()
    """
    Whether the parameter is required
    """

    default: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Default value if not provided
    """

    enum: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Allowed values for enum parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
