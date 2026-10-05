

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415(UniversalBaseModel):
    name: typing.Optional[str] = None
    children: typing.Optional[typing.List["HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415"]] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415)
