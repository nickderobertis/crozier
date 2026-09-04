

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SwissBankingMetadataSupport(UniversalBaseModel):
    technical_contact: typing.Optional[str] = None
    business_contact: typing.Optional[str] = None
    documentation: typing.Optional[str] = None
    github: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
