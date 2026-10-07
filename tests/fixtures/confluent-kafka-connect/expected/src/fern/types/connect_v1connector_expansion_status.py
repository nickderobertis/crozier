

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connector_expansion_status_connector import ConnectV1ConnectorExpansionStatusConnector
from .connect_v1connector_expansion_status_type import ConnectV1ConnectorExpansionStatusType
from .inline_response2001tasks import InlineResponse2001Tasks


class ConnectV1ConnectorExpansionStatus(UniversalBaseModel):
    """
    Status of the connector and its tasks.
    """

    name: str = pydantic.Field()
    """
    The name of the connector.
    """

    type: ConnectV1ConnectorExpansionStatusType = pydantic.Field()
    """
    Type of connector, sink or source.
    """

    connector: ConnectV1ConnectorExpansionStatusConnector
    tasks: typing.Optional[typing.List[InlineResponse2001Tasks]] = pydantic.Field(default=None)
    """
    A map containing the task status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
