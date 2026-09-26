

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SessionRevert(UniversalBaseModel):
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    part_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="partID"), pydantic.Field(alias="partID")
    ] = None
    snapshot: typing.Optional[str] = None
    diff: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
