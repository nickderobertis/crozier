

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DidDocumentStatusDto(UniversalBaseModel):
    valid: bool
    error: typing.Optional[str] = None
    did_document: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="didDocument"), pydantic.Field(alias="didDocument")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
