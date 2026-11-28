

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .free_form_text_form_field_canned_responses_behavior import FreeFormTextFormFieldCannedResponsesBehavior


class FreeFormTextFormFieldCannedResponses(UniversalBaseModel):
    behavior: typing.Optional[FreeFormTextFormFieldCannedResponsesBehavior] = None
    values: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
