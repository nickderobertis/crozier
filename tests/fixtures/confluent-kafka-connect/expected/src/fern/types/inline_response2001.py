

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inline_response2001connector import InlineResponse2001Connector
from .inline_response2001tasks import InlineResponse2001Tasks
from .inline_response2001type import InlineResponse2001Type


class InlineResponse2001(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the connector.
    """

    type: InlineResponse2001Type = pydantic.Field()
    """
    Type of connector, sink or source.
    """

    connector: InlineResponse2001Connector
    tasks: typing.Optional[typing.List[InlineResponse2001Tasks]] = pydantic.Field(default=None)
    """
    The map containing the task status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
