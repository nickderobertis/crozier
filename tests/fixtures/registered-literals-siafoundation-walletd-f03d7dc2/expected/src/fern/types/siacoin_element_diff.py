

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .siacoin_element import SiacoinElement


class SiacoinElementDiff(UniversalBaseModel):
    siacoin_element: typing_extensions.Annotated[
        SiacoinElement, FieldMetadata(alias="siacoinElement"), pydantic.Field(alias="siacoinElement")
    ]
    created: bool
    spent: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
