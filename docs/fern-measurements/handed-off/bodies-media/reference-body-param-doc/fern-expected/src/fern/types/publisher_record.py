

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credentials import Credentials


class PublisherRecord(UniversalBaseModel):
    publisher_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publisherId"), pydantic.Field(alias="publisherId")
    ] = None
    credentials: typing.Optional[Credentials] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
