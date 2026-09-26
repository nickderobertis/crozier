

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_action_target_ref import PdfActionTargetRef


class PdfActionNodeHide(UniversalBaseModel):
    subtype: str
    next: typing.List[typing.Any]
    targets: typing.List[PdfActionTargetRef]
    hide: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
