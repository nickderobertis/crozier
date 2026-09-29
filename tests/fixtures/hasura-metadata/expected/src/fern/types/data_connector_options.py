

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_connector_options_uri import DataConnectorOptionsUri


class DataConnectorOptions(UniversalBaseModel):
    display_name: typing.Optional[str] = None
    uri: DataConnectorOptionsUri

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
