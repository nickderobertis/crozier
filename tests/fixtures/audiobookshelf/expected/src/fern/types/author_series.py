

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .library_item_minified import LibraryItemMinified
from .series_id import SeriesId
from .series_name import SeriesName


class AuthorSeries(UniversalBaseModel):
    """
    Series and the included library items that an author has written.
    """

    id: typing.Optional[SeriesId] = None
    name: typing.Optional[SeriesName] = None
    items: typing.Optional[typing.List[LibraryItemMinified]] = pydantic.Field(default=None)
    """
    The items in the series. Each library item's media's metadata will have a `series` attribute, a `Series Sequence`, which is the matching series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
