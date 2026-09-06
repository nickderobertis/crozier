

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LibrarySettings(UniversalBaseModel):
    """
    The settings for the library.
    """

    cover_aspect_ratio: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="coverAspectRatio"),
        pydantic.Field(
            alias="coverAspectRatio",
            description="Whether the library should use square book covers. Must be 0 (for false) or 1 (for true).",
        ),
    ] = None
    """
    Whether the library should use square book covers. Must be 0 (for false) or 1 (for true).
    """

    disable_watcher: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="disableWatcher"),
        pydantic.Field(alias="disableWatcher", description="Whether to disable the folder watcher for the library."),
    ] = None
    """
    Whether to disable the folder watcher for the library.
    """

    skip_matching_media_with_asin: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="skipMatchingMediaWithAsin"),
        pydantic.Field(
            alias="skipMatchingMediaWithAsin", description="Whether to skip matching books that already have an ASIN."
        ),
    ] = None
    """
    Whether to skip matching books that already have an ASIN.
    """

    skip_matching_media_with_isbn: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="skipMatchingMediaWithIsbn"),
        pydantic.Field(
            alias="skipMatchingMediaWithIsbn", description="Whether to skip matching books that already have an ISBN."
        ),
    ] = None
    """
    Whether to skip matching books that already have an ISBN.
    """

    auto_scan_cron_expression: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="autoScanCronExpression"),
        pydantic.Field(
            alias="autoScanCronExpression",
            description="The cron expression for when to automatically scan the library folders. If null, automatic scanning will be disabled.",
        ),
    ] = None
    """
    The cron expression for when to automatically scan the library folders. If null, automatic scanning will be disabled.
    """

    audiobooks_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="audiobooksOnly"),
        pydantic.Field(
            alias="audiobooksOnly",
            description="Whether the library should ignore ebook files and only allow ebook files to be supplementary.",
        ),
    ] = None
    """
    Whether the library should ignore ebook files and only allow ebook files to be supplementary.
    """

    hide_single_book_series: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hideSingleBookSeries"),
        pydantic.Field(alias="hideSingleBookSeries", description="Whether to hide series with only one book."),
    ] = None
    """
    Whether to hide series with only one book.
    """

    only_show_later_books_in_continue_series: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="onlyShowLaterBooksInContinueSeries"),
        pydantic.Field(
            alias="onlyShowLaterBooksInContinueSeries",
            description="Whether to only show books in a series after the highest series sequence.",
        ),
    ] = None
    """
    Whether to only show books in a series after the highest series sequence.
    """

    metadata_precedence: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="metadataPrecedence"),
        pydantic.Field(
            alias="metadataPrecedence",
            description="The precedence of metadata sources. See Metadata Providers for a list of possible providers.",
        ),
    ] = None
    """
    The precedence of metadata sources. See Metadata Providers for a list of possible providers.
    """

    podcast_search_region: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="podcastSearchRegion"),
        pydantic.Field(alias="podcastSearchRegion", description="The region to use when searching for podcasts."),
    ] = None
    """
    The region to use when searching for podcasts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
