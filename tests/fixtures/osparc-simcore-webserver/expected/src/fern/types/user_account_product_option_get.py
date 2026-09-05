

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserAccountProductOptionGet(UniversalBaseModel):
    name: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    is_current: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCurrent"), pydantic.Field(alias="isCurrent")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
