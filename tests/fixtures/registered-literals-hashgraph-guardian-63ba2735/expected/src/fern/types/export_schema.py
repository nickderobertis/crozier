

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExportSchema(UniversalBaseModel):
    name: typing.Optional[str] = None
    version: typing.Optional[str] = None
    message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
