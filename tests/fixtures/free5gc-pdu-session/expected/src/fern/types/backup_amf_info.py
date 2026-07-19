

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .guami import Guami


class BackupAmfInfo(UniversalBaseModel):
    backup_amf: typing_extensions.Annotated[str, FieldMetadata(alias="backupAmf"), pydantic.Field(alias="backupAmf")]
    guami_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Guami]], FieldMetadata(alias="guamiList"), pydantic.Field(alias="guamiList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
