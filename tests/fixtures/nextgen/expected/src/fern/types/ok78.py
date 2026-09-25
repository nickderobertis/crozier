

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .item34 import Item34


class Ok78(UniversalBaseModel):
    count: typing_extensions.Annotated[str, FieldMetadata(alias="Count"), pydantic.Field(alias="Count")]
    items: typing_extensions.Annotated[typing.List[Item34], FieldMetadata(alias="Items"), pydantic.Field(alias="Items")]
    next_page_link: typing_extensions.Annotated[
        str, FieldMetadata(alias="NextPageLink"), pydantic.Field(alias="NextPageLink")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
