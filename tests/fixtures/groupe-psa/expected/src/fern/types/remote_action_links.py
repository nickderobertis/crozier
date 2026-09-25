

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class RemoteActionLinks(UniversalBaseModel):
    fleet: typing.Optional[Link] = None
    callback: typing.Optional[Link] = None
    self_: typing_extensions.Annotated[Link, FieldMetadata(alias="self"), pydantic.Field(alias="self")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
