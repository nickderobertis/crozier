

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreOcsGetCapabilities200ResponseOcsDataVersion(UniversalBaseModel):
    major: int
    minor: int
    micro: int
    string: str
    edition: str
    extended_support: typing_extensions.Annotated[
        bool, FieldMetadata(alias="extendedSupport"), pydantic.Field(alias="extendedSupport")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
