

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .store_ids import StoreIds


class KilnPlate(StoreIds):
    plate_type: typing_extensions.Annotated[str, FieldMetadata(alias="plateType"), pydantic.Field(alias="plateType")]
    serial: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
