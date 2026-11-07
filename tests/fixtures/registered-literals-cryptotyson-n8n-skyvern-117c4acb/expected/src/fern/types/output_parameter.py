

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .output_parameter_parameter_type import OutputParameterParameterType


class OutputParameter(UniversalBaseModel):
    parameter_type: typing.Optional[OutputParameterParameterType] = None
    key: str
    description: typing.Optional[str] = None
    output_parameter_id: str
    workflow_id: str
    created_at: dt.datetime
    modified_at: dt.datetime
    deleted_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
