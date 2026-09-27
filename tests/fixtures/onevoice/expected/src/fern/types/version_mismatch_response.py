

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .version_mismatch_response_code import VersionMismatchResponseCode


class VersionMismatchResponse(UniversalBaseModel):
    code: VersionMismatchResponseCode
    current_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentVersion"), pydantic.Field(alias="currentVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
