

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilesSharingShareStatusOneOf(UniversalBaseModel):
    status: str
    message: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    clear_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="clearAt"), pydantic.Field(alias="clearAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
