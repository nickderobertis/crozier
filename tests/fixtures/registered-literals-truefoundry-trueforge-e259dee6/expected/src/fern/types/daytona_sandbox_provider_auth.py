

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DaytonaSandboxProviderAuth(UniversalBaseModel):
    """
    Daytona authentication credentials.
    """

    api_key: str = pydantic.Field()
    """
    Daytona API key. Responses are redacted; on PUT, a real value sets/rotates and a redacted value keeps the stored key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
