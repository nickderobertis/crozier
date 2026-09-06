

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_out import MessageOut


class ListResponseMessageOut(UniversalBaseModel):
    data: typing.List[MessageOut]
    done: bool
    iterator: typing.Optional[str] = None
    prev_iterator: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="prevIterator"), pydantic.Field(alias="prevIterator")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
