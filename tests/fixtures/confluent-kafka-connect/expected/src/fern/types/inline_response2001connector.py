

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inline_response2001connector_state import InlineResponse2001ConnectorState


class InlineResponse2001Connector(UniversalBaseModel):
    """
    The map containing connector status.
    """

    state: InlineResponse2001ConnectorState = pydantic.Field()
    """
    The state of the connector.
    """

    worker_id: str = pydantic.Field()
    """
    The worker ID of the connector.
    """

    trace: typing.Optional[str] = pydantic.Field(default=None)
    """
    The exception name in case of error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
