

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.third_party_service_with_session import ThirdPartyServiceWithSession


class ListThirdPartySessionsResponse(UniversalBaseModel):
    data: typing.List[ThirdPartyServiceWithSession]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
