

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inline_response2003definition import InlineResponse2003Definition
from .inline_response2003value import InlineResponse2003Value


class InlineResponse2003Configs(UniversalBaseModel):
    definition: typing.Optional[InlineResponse2003Definition] = None
    value: typing.Optional[InlineResponse2003Value] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Map of metadata details about the connector configuration, such as type of
    input, etc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
