

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolApprovalPolicyAllowSession(UniversalBaseModel):
    expire_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp when this session allow expires. Omit to allow for the whole session.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
