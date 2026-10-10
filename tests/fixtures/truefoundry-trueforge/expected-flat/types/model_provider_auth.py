

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModelProviderAuth(UniversalBaseModel):
    """
    Provider authentication credentials.
    """

    api_key: str = pydantic.Field()
    """
    Provider API key. Responses are redacted; on PUT, a real value sets/rotates and a redacted value keeps the stored key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
