

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_status import ConnectorStatus
from .unified_api_id import UnifiedApiId


class ConnectorsFilter(UniversalBaseModel):
    status: typing.Optional[ConnectorStatus] = None
    unified_api: typing.Optional[UnifiedApiId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
