

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_metadata import PageMetadata
from .saved_search_response import SavedSearchResponse


class UserSavedSearchPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.Optional[typing.List[SavedSearchResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
