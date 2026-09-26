

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_action_node_submit_form_payload import PdfActionNodeSubmitFormPayload


class PdfActionNodeSubmitForm(UniversalBaseModel):
    subtype: str
    next: typing.List[typing.Any]
    payload: typing.Optional[PdfActionNodeSubmitFormPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
