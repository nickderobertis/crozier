

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .eutra_location import EutraLocation
from .n3ga_location import N3GaLocation
from .nr_location import NrLocation


class UserLocation(UniversalBaseModel):
    eutra_location: typing_extensions.Annotated[
        typing.Optional[EutraLocation], FieldMetadata(alias="eutraLocation"), pydantic.Field(alias="eutraLocation")
    ] = None
    nr_location: typing_extensions.Annotated[
        typing.Optional[NrLocation], FieldMetadata(alias="nrLocation"), pydantic.Field(alias="nrLocation")
    ] = None
    n3ga_location: typing_extensions.Annotated[
        typing.Optional[N3GaLocation], FieldMetadata(alias="n3gaLocation"), pydantic.Field(alias="n3gaLocation")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
