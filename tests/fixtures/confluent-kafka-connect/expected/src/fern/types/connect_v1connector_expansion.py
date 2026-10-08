

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connector_expansion_id import ConnectV1ConnectorExpansionId
from .connect_v1connector_expansion_info import ConnectV1ConnectorExpansionInfo
from .connect_v1connector_expansion_status import ConnectV1ConnectorExpansionStatus


class ConnectV1ConnectorExpansion(UniversalBaseModel):
    """
    Name of connector
    """

    id: typing.Optional[ConnectV1ConnectorExpansionId] = None
    info: typing.Optional[ConnectV1ConnectorExpansionInfo] = None
    status: typing.Optional[ConnectV1ConnectorExpansionStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
