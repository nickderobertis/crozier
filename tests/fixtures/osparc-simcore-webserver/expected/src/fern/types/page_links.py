

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PageLinks(UniversalBaseModel):
    self_: typing_extensions.Annotated[str, FieldMetadata(alias="self"), pydantic.Field(alias="self")]
    first: str
    prev: typing.Optional[str] = None
    next: typing.Optional[str] = None
    last: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
