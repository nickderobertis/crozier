

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signing_keys_response_output_keys_item_algorithm import SigningKeysResponseOutputKeysItemAlgorithm
from .signing_keys_response_output_keys_item_status import SigningKeysResponseOutputKeysItemStatus


class SigningKeysResponseOutputKeysItem(UniversalBaseModel):
    id: str
    algorithm: SigningKeysResponseOutputKeysItemAlgorithm
    status: SigningKeysResponseOutputKeysItemStatus
    public_jwk: typing.Optional[typing.Any] = None
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
