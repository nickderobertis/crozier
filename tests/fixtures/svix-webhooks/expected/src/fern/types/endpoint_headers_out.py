

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EndpointHeadersOut(UniversalBaseModel):
    """
    The value of the headers is returned in the `headers` field.

    Sensitive headers that have been redacted are returned in the sensitive field.
    """

    headers: typing.Dict[str, str]
    sensitive: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
