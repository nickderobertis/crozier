

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .disclosure_content_type import DisclosureContentType
from .disclosure_type import DisclosureType


class Disclosure(UniversalBaseModel):
    type: DisclosureType
    content_type: DisclosureContentType
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
