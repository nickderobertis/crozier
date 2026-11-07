

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilesSharingShareeValue(UniversalBaseModel):
    share_type: typing_extensions.Annotated[int, FieldMetadata(alias="shareType"), pydantic.Field(alias="shareType")]
    share_with: typing_extensions.Annotated[str, FieldMetadata(alias="shareWith"), pydantic.Field(alias="shareWith")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
