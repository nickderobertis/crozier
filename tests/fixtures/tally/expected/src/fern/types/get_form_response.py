

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .block import Block
from .form import Form
from .form_settings import FormSettings


class GetFormResponse(Form):
    settings: typing.Optional[FormSettings] = None
    blocks: typing.Optional[typing.List[Block]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetFormResponse)
