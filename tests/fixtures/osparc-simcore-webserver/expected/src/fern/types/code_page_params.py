

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CodePageParams(UniversalBaseModel):
    message: str
    expiration2fa: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="expiration_2fa"), pydantic.Field(alias="expiration_2fa")
    ] = None
    next_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
