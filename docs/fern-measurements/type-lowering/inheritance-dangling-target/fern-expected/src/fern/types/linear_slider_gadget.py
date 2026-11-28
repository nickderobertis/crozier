

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .linear_slider_gadget_kind import LinearSliderGadgetKind


class LinearSliderGadget(UniversalBaseModel):
    kind: typing.Optional[LinearSliderGadgetKind] = None
    travel: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
