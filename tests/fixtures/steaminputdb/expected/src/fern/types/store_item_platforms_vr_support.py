

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreItemPlatformsVrSupport(UniversalBaseModel):
    htc_vive: typing.Optional[bool] = None
    oculus_rift: typing.Optional[bool] = None
    valve_index: typing.Optional[bool] = None
    vrhmd: typing.Optional[bool] = None
    vrhmd_only: typing.Optional[bool] = None
    windows_mr: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
