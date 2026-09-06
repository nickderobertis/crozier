

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreGameRating(UniversalBaseModel):
    descriptors: typing.Optional[typing.List[str]] = None
    image_target: typing.Optional[str] = None
    image_url: typing.Optional[str] = None
    interactive_elements: typing.Optional[str] = None
    rating: typing.Optional[str] = None
    required_age: typing.Optional[int] = None
    type: typing.Optional[str] = None
    use_age_gate: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
