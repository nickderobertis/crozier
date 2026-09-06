

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .series_progress import SeriesProgress


class SeriesWithProgressAndRssProgress(UniversalBaseModel):
    progress: typing.Optional[SeriesProgress] = None
    rss_feed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rssFeed"),
        pydantic.Field(alias="rssFeed", description="The RSS feed for the series."),
    ] = None
    """
    The RSS feed for the series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
