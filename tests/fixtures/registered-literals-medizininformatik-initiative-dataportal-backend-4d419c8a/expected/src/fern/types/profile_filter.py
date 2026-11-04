

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .profile_filter_value import ProfileFilterValue


class ProfileFilter(UniversalBaseModel):
    name: typing.Optional[str] = None
    values: typing.Optional[typing.List[ProfileFilterValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
