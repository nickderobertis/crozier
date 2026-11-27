

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PacketBase(UniversalBaseModel):
    name: typing.Optional[str] = None
    bin_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="binId"), pydantic.Field(alias="binId")
    ] = None
    grower: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
