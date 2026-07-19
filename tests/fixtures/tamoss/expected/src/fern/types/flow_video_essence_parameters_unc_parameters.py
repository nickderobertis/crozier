

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_video_essence_parameters_unc_parameters_unc_type import FlowVideoEssenceParametersUncParametersUncType


class FlowVideoEssenceParametersUncParameters(UniversalBaseModel):
    unc_type: FlowVideoEssenceParametersUncParametersUncType = pydantic.Field()
    """
    Uncompressed picture packing type. If codec is `video/raw`, unc_type must be set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
