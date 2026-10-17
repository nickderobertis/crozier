

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1backups_response_output_backups_item import V1BackupsResponseOutputBackupsItem
from .v1backups_response_output_physical_backup_data import V1BackupsResponseOutputPhysicalBackupData


class V1BackupsResponseOutput(UniversalBaseModel):
    region: str
    walg_enabled: bool
    pitr_enabled: bool
    backups: typing.List[V1BackupsResponseOutputBackupsItem]
    physical_backup_data: V1BackupsResponseOutputPhysicalBackupData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
