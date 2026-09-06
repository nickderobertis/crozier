

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentSubmissionSharedBusinessEntitiesRelease(UniversalBaseModel):
    """
    Release class
    """

    build_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="BuildDate"),
        pydantic.Field(alias="BuildDate", description="Build Date"),
    ] = None
    """
    Build Date
    """

    bundle_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="BundleIDs"),
        pydantic.Field(alias="BundleIDs", description="IDs of AUC Bundles associated with this Release."),
    ] = None
    """
    IDs of AUC Bundles associated with this Release.
    """

    release_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="ReleaseDate"),
        pydantic.Field(alias="ReleaseDate", description="Release Date"),
    ] = None
    """
    Release Date
    """

    release_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ReleaseID"),
        pydantic.Field(alias="ReleaseID", description="Release ID"),
    ] = None
    """
    Release ID
    """

    release_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ReleaseNumber"),
        pydantic.Field(alias="ReleaseNumber", description="Release Number"),
    ] = None
    """
    Release Number
    """

    visible: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="Visible"), pydantic.Field(alias="Visible", description="Visible")
    ] = None
    """
    Visible
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
