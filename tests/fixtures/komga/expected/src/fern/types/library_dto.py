

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .library_dto_scan_interval import LibraryDtoScanInterval
from .library_dto_series_cover import LibraryDtoSeriesCover


class LibraryDto(UniversalBaseModel):
    analyze_dimensions: typing_extensions.Annotated[
        bool, FieldMetadata(alias="analyzeDimensions"), pydantic.Field(alias="analyzeDimensions")
    ]
    convert_to_cbz: typing_extensions.Annotated[
        bool, FieldMetadata(alias="convertToCbz"), pydantic.Field(alias="convertToCbz")
    ]
    empty_trash_after_scan: typing_extensions.Annotated[
        bool, FieldMetadata(alias="emptyTrashAfterScan"), pydantic.Field(alias="emptyTrashAfterScan")
    ]
    hash_files: typing_extensions.Annotated[bool, FieldMetadata(alias="hashFiles"), pydantic.Field(alias="hashFiles")]
    hash_koreader: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hashKoreader"), pydantic.Field(alias="hashKoreader")
    ]
    hash_pages: typing_extensions.Annotated[bool, FieldMetadata(alias="hashPages"), pydantic.Field(alias="hashPages")]
    id: str
    import_barcode_isbn: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importBarcodeIsbn"), pydantic.Field(alias="importBarcodeIsbn")
    ]
    import_comic_info_book: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importComicInfoBook"), pydantic.Field(alias="importComicInfoBook")
    ]
    import_comic_info_collection: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importComicInfoCollection"), pydantic.Field(alias="importComicInfoCollection")
    ]
    import_comic_info_read_list: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importComicInfoReadList"), pydantic.Field(alias="importComicInfoReadList")
    ]
    import_comic_info_series: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importComicInfoSeries"), pydantic.Field(alias="importComicInfoSeries")
    ]
    import_comic_info_series_append_volume: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="importComicInfoSeriesAppendVolume"),
        pydantic.Field(alias="importComicInfoSeriesAppendVolume"),
    ]
    import_epub_book: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importEpubBook"), pydantic.Field(alias="importEpubBook")
    ]
    import_epub_series: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importEpubSeries"), pydantic.Field(alias="importEpubSeries")
    ]
    import_local_artwork: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importLocalArtwork"), pydantic.Field(alias="importLocalArtwork")
    ]
    import_mylar_series: typing_extensions.Annotated[
        bool, FieldMetadata(alias="importMylarSeries"), pydantic.Field(alias="importMylarSeries")
    ]
    name: str
    oneshots_directory: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oneshotsDirectory"), pydantic.Field(alias="oneshotsDirectory")
    ] = None
    repair_extensions: typing_extensions.Annotated[
        bool, FieldMetadata(alias="repairExtensions"), pydantic.Field(alias="repairExtensions")
    ]
    root: str
    scan_cbx: typing_extensions.Annotated[bool, FieldMetadata(alias="scanCbx"), pydantic.Field(alias="scanCbx")]
    scan_directory_exclusions: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="scanDirectoryExclusions"),
        pydantic.Field(alias="scanDirectoryExclusions"),
    ]
    scan_epub: typing_extensions.Annotated[bool, FieldMetadata(alias="scanEpub"), pydantic.Field(alias="scanEpub")]
    scan_force_modified_time: typing_extensions.Annotated[
        bool, FieldMetadata(alias="scanForceModifiedTime"), pydantic.Field(alias="scanForceModifiedTime")
    ]
    scan_interval: typing_extensions.Annotated[
        LibraryDtoScanInterval, FieldMetadata(alias="scanInterval"), pydantic.Field(alias="scanInterval")
    ]
    scan_on_startup: typing_extensions.Annotated[
        bool, FieldMetadata(alias="scanOnStartup"), pydantic.Field(alias="scanOnStartup")
    ]
    scan_pdf: typing_extensions.Annotated[bool, FieldMetadata(alias="scanPdf"), pydantic.Field(alias="scanPdf")]
    series_cover: typing_extensions.Annotated[
        LibraryDtoSeriesCover, FieldMetadata(alias="seriesCover"), pydantic.Field(alias="seriesCover")
    ]
    unavailable: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
