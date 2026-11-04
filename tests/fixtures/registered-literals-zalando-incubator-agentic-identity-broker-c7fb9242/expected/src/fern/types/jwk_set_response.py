

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jwk_set_response_keys_item import JwkSetResponseKeysItem


class JwkSetResponse(UniversalBaseModel):
    keys: typing.List[JwkSetResponseKeysItem] = pydantic.Field()
    """
    Array of JSON Web Keys (RFC 7517). Each key contains only public
    key material — private keys are never exposed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
