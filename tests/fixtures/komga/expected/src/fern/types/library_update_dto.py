

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .library_update_dto_scan_interval import LibraryUpdateDtoScanInterval
from .library_update_dto_series_cover import LibraryUpdateDtoSeriesCover


class LibraryUpdateDto(UniversalBaseModel):
    """
    Fields to update. You can omit fields you don't want to update.
    """

    analyze_dimensions: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="analyzeDimensions"), pydantic.Field(alias="analyzeDimensions")
    ] = None
    convert_to_cbz: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="convertToCbz"), pydantic.Field(alias="convertToCbz")
    ] = None
    empty_trash_after_scan: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="emptyTrashAfterScan"), pydantic.Field(alias="emptyTrashAfterScan")
    ] = None
    hash_files: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hashFiles"), pydantic.Field(alias="hashFiles")
    ] = None
    hash_koreader: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hashKoreader"), pydantic.Field(alias="hashKoreader")
    ] = None
    hash_pages: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hashPages"), pydantic.Field(alias="hashPages")
    ] = None
    import_barcode_isbn: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="importBarcodeIsbn"), pydantic.Field(alias="importBarcodeIsbn")
    ] = None
    import_comic_info_book: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="importComicInfoBook"), pydantic.Field(alias="importComicInfoBook")
    ] = None
    import_comic_info_collection: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="importComicInfoCollection"),
        pydantic.Field(alias="importComicInfoCollection"),
    ] = None
    import_comic_info_read_list: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="importComicInfoReadList"),
        pydantic.Field(alias="importComicInfoReadList"),
    ] = None
    import_comic_info_series: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="importComicInfoSeries"),
        pydantic.Field(alias="importComicInfoSeries"),
    ] = None
    import_comic_info_series_append_volume: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="importComicInfoSeriesAppendVolume"),
        pydantic.Field(alias="importComicInfoSeriesAppendVolume"),
    ] = None
    import_epub_book: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="importEpubBook"), pydantic.Field(alias="importEpubBook")
    ] = None
    import_epub_series: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="importEpubSeries"), pydantic.Field(alias="importEpubSeries")
    ] = None
    import_local_artwork: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="importLocalArtwork"), pydantic.Field(alias="importLocalArtwork")
    ] = None
    import_mylar_series: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="importMylarSeries"), pydantic.Field(alias="importMylarSeries")
    ] = None
    name: typing.Optional[str] = None
    oneshots_directory: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oneshotsDirectory"), pydantic.Field(alias="oneshotsDirectory")
    ] = None
    repair_extensions: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="repairExtensions"), pydantic.Field(alias="repairExtensions")
    ] = None
    root: typing.Optional[str] = None
    scan_cbx: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="scanCbx"), pydantic.Field(alias="scanCbx")
    ] = None
    scan_directory_exclusions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="scanDirectoryExclusions"),
        pydantic.Field(alias="scanDirectoryExclusions"),
    ] = None
    scan_epub: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="scanEpub"), pydantic.Field(alias="scanEpub")
    ] = None
    scan_force_modified_time: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="scanForceModifiedTime"),
        pydantic.Field(alias="scanForceModifiedTime"),
    ] = None
    scan_interval: typing_extensions.Annotated[
        typing.Optional[LibraryUpdateDtoScanInterval],
        FieldMetadata(alias="scanInterval"),
        pydantic.Field(alias="scanInterval"),
    ] = None
    scan_on_startup: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="scanOnStartup"), pydantic.Field(alias="scanOnStartup")
    ] = None
    scan_pdf: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="scanPdf"), pydantic.Field(alias="scanPdf")
    ] = None
    series_cover: typing_extensions.Annotated[
        typing.Optional[LibraryUpdateDtoSeriesCover],
        FieldMetadata(alias="seriesCover"),
        pydantic.Field(alias="seriesCover"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
