

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.composite_signature import CompositeSignature


class MultiPartyAuthorizeRequestAuthorizationAuthorizationsItem(UniversalBaseModel):
    party_id: typing.Optional[str] = None
    role: typing.Optional[str] = None
    composite_sig: typing.Optional[CompositeSignature] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
