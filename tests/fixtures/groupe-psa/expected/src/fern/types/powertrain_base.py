

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .powertrain_base_status import PowertrainBaseStatus


class PowertrainBase(UniversalBaseModel):
    status: typing.Optional[PowertrainBaseStatus] = pydantic.Field(default=None)
    """
    Status of the powertrain
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
