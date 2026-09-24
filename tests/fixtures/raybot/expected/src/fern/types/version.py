

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Version(UniversalBaseModel):
    version: str
    build_date: typing_extensions.Annotated[str, FieldMetadata(alias="buildDate"), pydantic.Field(alias="buildDate")]
    go_version: typing_extensions.Annotated[str, FieldMetadata(alias="goVersion"), pydantic.Field(alias="goVersion")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
