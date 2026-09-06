

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wp_contributor_dto import WpContributorDto


class WpBelongsToDto(UniversalBaseModel):
    collection: typing.List[WpContributorDto]
    series: typing.List[WpContributorDto]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
