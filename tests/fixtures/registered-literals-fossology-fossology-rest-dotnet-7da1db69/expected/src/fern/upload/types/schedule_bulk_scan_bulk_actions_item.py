

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .schedule_bulk_scan_bulk_actions_item_license_action import ScheduleBulkScanBulkActionsItemLicenseAction


class ScheduleBulkScanBulkActionsItem(UniversalBaseModel):
    license_short_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="licenseShortName"), pydantic.Field(alias="licenseShortName")
    ] = None
    license_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="licenseText"), pydantic.Field(alias="licenseText")
    ] = None
    acknowledgement: typing.Optional[str] = None
    comment: typing.Optional[str] = None
    license_action: typing_extensions.Annotated[
        typing.Optional[ScheduleBulkScanBulkActionsItemLicenseAction],
        FieldMetadata(alias="licenseAction"),
        pydantic.Field(alias="licenseAction"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
