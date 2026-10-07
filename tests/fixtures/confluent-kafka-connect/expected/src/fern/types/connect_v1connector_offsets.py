

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connector_offsets_metadata import ConnectV1ConnectorOffsetsMetadata
from .connect_v1connector_offsets_offsets_item import ConnectV1ConnectorOffsetsOffsetsItem


class ConnectV1ConnectorOffsets(UniversalBaseModel):
    """
    Offsets for a connector
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the connector.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the connector.
    """

    offsets: typing.Optional[typing.List[ConnectV1ConnectorOffsetsOffsetsItem]] = pydantic.Field(default=None)
    """
    Array of offsets which are categorised into partitions.
    """

    metadata: typing.Optional[ConnectV1ConnectorOffsetsMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
