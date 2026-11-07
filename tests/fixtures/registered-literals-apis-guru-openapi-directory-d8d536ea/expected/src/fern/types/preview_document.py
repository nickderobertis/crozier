

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PreviewDocument(UniversalBaseModel):
    added_to_library_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addedToLibraryDate"),
        pydantic.Field(
            alias="addedToLibraryDate",
            description="Date and time when the preview document was downloaded and added to the UniCourt CrowdSourced Library.",
        ),
    ] = None
    """
    Date and time when the preview document was downloaded and added to the UniCourt CrowdSourced Library.
    """

    download_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="downloadAPI"),
        pydantic.Field(
            alias="downloadAPI",
            description="Link to get the file url for the preview document which is already present in the UniCourt CrowdSourced Library.",
        ),
    ] = None
    """
    Link to get the file url for the preview document which is already present in the UniCourt CrowdSourced Library.
    """

    in_library: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="inLibrary"),
        pydantic.Field(
            alias="inLibrary",
            description="Determines if the preview document is present in the UniCourt Library or not.",
        ),
    ]
    """
    Determines if the preview document is present in the UniCourt Library or not.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
