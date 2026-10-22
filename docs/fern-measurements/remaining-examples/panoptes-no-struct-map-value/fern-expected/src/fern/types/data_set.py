

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_set_data_configuration import DataSetDataConfiguration


class DataSet(UniversalBaseModel):
    name: typing.Optional[str] = None
    data_type: typing.Optional[str] = None
    data_configuration: typing.Optional[DataSetDataConfiguration] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
