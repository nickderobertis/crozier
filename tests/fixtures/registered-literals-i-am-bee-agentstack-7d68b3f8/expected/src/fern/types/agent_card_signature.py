

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentCardSignature(UniversalBaseModel):
    """
    AgentCardSignature represents a JWS signature of an AgentCard.
    This follows the JSON format of an RFC 7515 JSON Web Signature (JWS).
    """

    header: typing.Optional[typing.Dict[str, typing.Any]] = None
    protected: str
    signature: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
