

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .key_to_multi_value import KeyToMultiValue


class HttpOverrideForwardedRequestRequestModifierRequestModifierQueryStringParameters(UniversalBaseModel):
    add: typing.Optional[KeyToMultiValue] = None
    replace: typing.Optional[KeyToMultiValue] = None
    remove: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
