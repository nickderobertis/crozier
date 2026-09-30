

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_organization import ApiOrganization
from .search_header import SearchHeader


class OrganizationSearchResponse(UniversalBaseModel):
    header: typing.Optional[SearchHeader] = None
    results: typing.Optional[typing.List[ApiOrganization]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
