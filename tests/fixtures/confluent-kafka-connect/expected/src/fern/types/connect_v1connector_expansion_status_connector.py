

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connector_expansion_status_connector_state import ConnectV1ConnectorExpansionStatusConnectorState


class ConnectV1ConnectorExpansionStatusConnector(UniversalBaseModel):
    """
    A map containing connector status.
    """

    state: ConnectV1ConnectorExpansionStatusConnectorState = pydantic.Field()
    """
    The state of the connector.
    """

    worker_id: str = pydantic.Field()
    """
    The worker ID of the connector.
    """

    trace: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exception message in case of an error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
