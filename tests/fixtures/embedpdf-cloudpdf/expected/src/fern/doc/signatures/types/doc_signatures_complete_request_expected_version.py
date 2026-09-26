

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class DocSignaturesCompleteRequestExpectedVersion(UniversalBaseModel):
    base_sha256: typing_extensions.Annotated[str, FieldMetadata(alias="baseSha256"), pydantic.Field(alias="baseSha256")]
    edits_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="editsVersion"), pydantic.Field(alias="editsVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
