

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataQueryListEntryDataExtraction(UniversalBaseModel):
    exists: typing.Optional[bool] = None
    is_valid: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isValid"), pydantic.Field(alias="isValid")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
