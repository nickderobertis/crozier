

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .config import Config as types_config_Config
from .data_connector_conn_source_config_timeout import DataConnectorConnSourceConfigTimeout
from .template_variable_source import TemplateVariableSource


class DataConnectorConnSourceConfig(UniversalBaseModel):
    template: typing.Optional[str] = None
    template_variables: typing.Optional[typing.Dict[str, TemplateVariableSource]] = None
    timeout: typing.Optional[DataConnectorConnSourceConfigTimeout] = None
    value: types_config_Config

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
