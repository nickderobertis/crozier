

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .driver_attributes import DriverAttributes


class Driver(UniversalBaseModel):
    attributes: typing.Optional[DriverAttributes] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    unique_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uniqueId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
