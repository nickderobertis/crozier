

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ratio(UniversalBaseModel):
    """
    Ratio.
    """

    adjusted_open_spaces_list: typing.Optional[typing.List[int]] = None
    total_adjusted_open_spaces: int
    closed_spaces_list: typing.Optional[typing.List[int]] = None
    adjusted_closed_spaces_list: typing.Optional[typing.List[int]] = None
    total_adjusted_closed_spaces: int
    total_adjusted_net_open_spaces: int
    available_spaces_list: typing.Optional[typing.List[int]] = None
    adjusted_available_spaces_list: typing.Optional[typing.List[int]] = None
    total_adjusted_available_spaces: int
    ratio_available_to_open: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
