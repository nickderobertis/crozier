

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tel_input_strategy import TelInputStrategy


class TelInputOutcome(UniversalBaseModel):
    flag_enabled: bool
    final_element_id: str
    strategy: TelInputStrategy
    expected_digit_count: int
    actual_digit_count: typing.Optional[int] = None
    browser_valid: typing.Optional[bool] = None
    attempt_count: int
    retargeted: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
