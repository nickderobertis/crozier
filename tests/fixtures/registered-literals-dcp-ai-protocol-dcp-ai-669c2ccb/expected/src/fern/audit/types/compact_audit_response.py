

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompactAuditResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    compacted_range: typing.Optional[typing.Dict[str, typing.Any]] = None
    merkle_root: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
