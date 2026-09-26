

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .realm_export_export_type import RealmExportExportType


class RealmExport(UniversalBaseModel):
    """
    Object containing details about a
    [data export](/help/export-your-organization).
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the data export.
    """

    acting_user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who created the data export.
    """

    export_time: typing.Optional[float] = pydantic.Field(default=None)
    """
    The UNIX timestamp of when the data export was started.
    """

    deleted_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The UNIX timestamp of when the data export was deleted.
    
    Will be `null` if the data export has not been deleted.
    """

    failed_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The UNIX timestamp of when the data export failed.
    
    Will be `null` if the data export succeeded, or if it's
    still being generated.
    """

    export_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to download the generated data export.
    
    Will be `null` if the data export failed, or if it's
    still being generated.
    """

    pending: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the data export is pending, which indicates it
    is still being generated, or if it succeeded, failed or
    was deleted before being generated.
    
    Depending on the size of the organization, it can take
    anywhere from seconds to an hour to generate the data
    export.
    """

    export_type: typing.Optional[RealmExportExportType] = pydantic.Field(default=None)
    """
    Whether the data export is public, full with consent, or full without consent.
    
    - `public` = Public data export.
    - `full_with_consent` = Public and private data export (with consent), which includes private data
      for users who have granted consent.
    - `full_without_consent` = All public and private data, which includes private data for all users.
    
    **Changes**: Zulip 12.0 (feature level 449) changed the type of
    this field from int to string with `1` being replaced by `public` and
    `2` being replaced by `full_with_consent`. The option `full_without_consent`
    was added for full exports without member consent.
    
    **Changes**: New in Zulip 10.0 (feature level 304). Previously,
    the export type was not included in these objects because only
    public data exports could be created or listed via the API or UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
