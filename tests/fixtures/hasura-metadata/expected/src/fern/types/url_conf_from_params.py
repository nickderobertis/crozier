

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .url_conf_from_params_connection_parameters import UrlConfFromParamsConnectionParameters


class UrlConfFromParams(UniversalBaseModel):
    connection_parameters: UrlConfFromParamsConnectionParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
