

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_anything_request_arr_mix_item_arr_mix_nested_arr_mix_nested import (
    PostAnythingRequestArrMixItemArrMixNestedArrMixNested,
)


class PostAnythingRequestArrMixItemArrMixNested(UniversalBaseModel):
    arr_mix_nested: typing.Optional[PostAnythingRequestArrMixItemArrMixNestedArrMixNested] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
