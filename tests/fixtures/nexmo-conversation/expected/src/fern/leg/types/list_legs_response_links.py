

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_legs_response_links_self import ListLegsResponseLinksSelf


class ListLegsResponseLinks(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        ListLegsResponseLinksSelf, FieldMetadata(alias="self"), pydantic.Field(alias="self")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
