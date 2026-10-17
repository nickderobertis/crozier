

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signing_keys_response_output_keys_item import SigningKeysResponseOutputKeysItem


class SigningKeysResponseOutput(UniversalBaseModel):
    keys: typing.List[SigningKeysResponseOutputKeysItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
