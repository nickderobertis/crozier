

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .global_saved_search import GlobalSavedSearch
from .page_metadata import PageMetadata


class GlobalSavedSearchPage(UniversalBaseModel):
    """
    A page of global saved searches.
    """

    metadata: typing.Optional[PageMetadata] = None
    data: typing.Optional[typing.List[GlobalSavedSearch]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
