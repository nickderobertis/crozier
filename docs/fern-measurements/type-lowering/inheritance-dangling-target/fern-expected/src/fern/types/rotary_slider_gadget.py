

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rotary_slider_gadget_kind import RotarySliderGadgetKind


class RotarySliderGadget(UniversalBaseModel):
    kind: typing.Optional[RotarySliderGadgetKind] = None
    degrees: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
