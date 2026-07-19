

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tai import Tai


class AreaOfValidity(UniversalBaseModel):
    tai_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Tai]], FieldMetadata(alias="taiList"), pydantic.Field(alias="taiList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
