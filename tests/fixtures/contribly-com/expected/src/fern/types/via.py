

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authority import Authority
from .place import Place


class Via(UniversalBaseModel):
    authority: typing.Optional[Authority] = None
    ip_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ipAddress"), pydantic.Field(alias="ipAddress")
    ] = None
    ip_address_place: typing_extensions.Annotated[
        typing.Optional[Place], FieldMetadata(alias="ipAddressPlace"), pydantic.Field(alias="ipAddressPlace")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
