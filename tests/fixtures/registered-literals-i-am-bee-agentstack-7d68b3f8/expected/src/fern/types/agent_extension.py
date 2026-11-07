

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentExtension(UniversalBaseModel):
    """
    A declaration of a protocol extension supported by an Agent.
    """

    description: typing.Optional[str] = None
    params: typing.Optional[typing.Dict[str, typing.Any]] = None
    required: typing.Optional[bool] = None
    uri: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
