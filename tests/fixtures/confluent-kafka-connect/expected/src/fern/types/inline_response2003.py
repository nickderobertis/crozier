

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inline_response2003configs import InlineResponse2003Configs


class InlineResponse2003(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The class name of the connector plugin.
    """

    groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of groups used in configuration definitions.
    """

    error_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of errors encountered during configuration validation.
    """

    configs: typing.Optional[typing.List[InlineResponse2003Configs]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
