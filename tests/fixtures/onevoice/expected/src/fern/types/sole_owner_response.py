

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sole_owner_business_entry import SoleOwnerBusinessEntry
from .sole_owner_response_code import SoleOwnerResponseCode


class SoleOwnerResponse(UniversalBaseModel):
    code: SoleOwnerResponseCode
    businesses: typing.List[SoleOwnerBusinessEntry]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
