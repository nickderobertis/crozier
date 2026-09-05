

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ike_crypto_profiles_set import IkeCryptoProfilesSet


class GetV1IkeCryptoProfilesReadResponse(UniversalBaseModel):
    data: typing.Optional[IkeCryptoProfilesSet] = None
    limit: typing.Optional[float] = None
    offset: typing.Optional[float] = None
    total: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
