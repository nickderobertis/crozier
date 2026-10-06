

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .yard_request import YardRequest


class YardRecord(YardRequest):
    opened_on: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="openedOn"), pydantic.Field(alias="openedOn")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
