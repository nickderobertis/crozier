

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionAgentReference(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Registry agent id.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Create-time snapshot of the registry agent name; null for legacy or orphan rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
