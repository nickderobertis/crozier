

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .siafund_element import SiafundElement


class SiafundElementDiff(UniversalBaseModel):
    siafund_element: typing_extensions.Annotated[
        SiafundElement, FieldMetadata(alias="siafundElement"), pydantic.Field(alias="siafundElement")
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
