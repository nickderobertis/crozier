

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .claim_id_token import ClaimIdToken
from .claim_userinfo import ClaimUserinfo


class Claim(UniversalBaseModel):
    """
    The userinfo and id_token members of the claims request both are JSON object. if null, Indicates that this Claim is being requested as Voluntary Claim.

    **Note:** Unknown claim names either in userinfo or id_token are ignored.
    """

    userinfo: typing.Optional[ClaimUserinfo] = None
    id_token: typing.Optional[ClaimIdToken] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
