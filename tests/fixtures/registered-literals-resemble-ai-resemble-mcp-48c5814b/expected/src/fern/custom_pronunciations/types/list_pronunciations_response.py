

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.custom_pronunciation import CustomPronunciation


class ListPronunciationsResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    items: typing.Optional[typing.List[CustomPronunciation]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
