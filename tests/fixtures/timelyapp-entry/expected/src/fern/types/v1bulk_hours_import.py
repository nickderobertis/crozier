

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1bulk_hours_import_create_item import V1BulkHoursImportCreateItem
from .v1bulk_hours_import_update_item import V1BulkHoursImportUpdateItem


class V1BulkHoursImport(UniversalBaseModel):
    create: typing.Optional[typing.List[V1BulkHoursImportCreateItem]] = pydantic.Field(default=None)
    """
    Array of time entries to create. Each item accepts all standard event/time entry fields from PayloadSchema.
    """

    update: typing.Optional[typing.List[V1BulkHoursImportUpdateItem]] = pydantic.Field(default=None)
    """
    Array of time entries to update. Must include id field. All other fields from UpdatePayloadSchema are optional.
    """

    delete: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of time entry IDs to delete
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
