

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1backups_response_output_backups_item_status import V1BackupsResponseOutputBackupsItemStatus


class V1BackupsResponseOutputBackupsItem(UniversalBaseModel):
    id: int
    is_physical_backup: bool
    status: V1BackupsResponseOutputBackupsItemStatus
    inserted_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
