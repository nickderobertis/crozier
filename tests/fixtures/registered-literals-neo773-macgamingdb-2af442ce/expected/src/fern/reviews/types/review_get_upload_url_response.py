

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ReviewGetUploadUrlResponse(UniversalBaseModel):
    signed_url: typing_extensions.Annotated[str, FieldMetadata(alias="signedUrl"), pydantic.Field(alias="signedUrl")]
    public_url: typing_extensions.Annotated[str, FieldMetadata(alias="publicUrl"), pydantic.Field(alias="publicUrl")]
    key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
