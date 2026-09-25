

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .item3 import Item3


class Ok8(UniversalBaseModel):
    items: typing_extensions.Annotated[typing.List[Item3], FieldMetadata(alias="Items"), pydantic.Field(alias="Items")]
    next_page_link: typing_extensions.Annotated[
        str, FieldMetadata(alias="NextPageLink"), pydantic.Field(alias="NextPageLink")
    ]
    count: typing_extensions.Annotated[str, FieldMetadata(alias="Count"), pydantic.Field(alias="Count")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
