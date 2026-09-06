

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SharedLibrariesUpdateDto(UniversalBaseModel):
    all_: typing_extensions.Annotated[bool, FieldMetadata(alias="all"), pydantic.Field(alias="all")]
    library_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="libraryIds"), pydantic.Field(alias="libraryIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
