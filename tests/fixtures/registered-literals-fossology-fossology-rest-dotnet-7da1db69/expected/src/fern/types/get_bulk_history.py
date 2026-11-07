

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetBulkHistory(UniversalBaseModel):
    bulk_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bulkId"), pydantic.Field(alias="bulkId", description="The bulk id")
    ] = None
    """
    The bulk id
    """

    clearing_event_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="clearingEventId"),
        pydantic.Field(alias="clearingEventId", description="The event id associated with the bulk"),
    ] = None
    """
    The event id associated with the bulk
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Scan reference text
    """

    matched: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether matched or not
    """

    tried: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether tried or not
    """

    added_licenses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="addedLicenses"),
        pydantic.Field(alias="addedLicenses", description="List of license shortnames added to the scan"),
    ] = None
    """
    List of license shortnames added to the scan
    """

    removed_licenses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="removedLicenses"),
        pydantic.Field(alias="removedLicenses", description="List of license shortnames removed from the scan"),
    ] = None
    """
    List of license shortnames removed from the scan
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
