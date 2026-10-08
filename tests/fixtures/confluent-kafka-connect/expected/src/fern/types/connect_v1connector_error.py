

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1connector_error_error import ConnectV1ConnectorErrorError


class ConnectV1ConnectorError(UniversalBaseModel):
    error: typing.Optional[ConnectV1ConnectorErrorError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
