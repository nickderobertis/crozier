

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .display_entry import DisplayEntry


class ProfileDataField(UniversalBaseModel):
    id: typing.Optional[str] = None
    display: typing.Optional[DisplayEntry] = None
    description: typing.Optional[DisplayEntry] = None
    type: typing.Optional[str] = None
    recommended: typing.Optional[bool] = None
    required: typing.Optional[bool] = None
    children: typing.Optional[typing.List["ProfileDataField"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ProfileDataField)
