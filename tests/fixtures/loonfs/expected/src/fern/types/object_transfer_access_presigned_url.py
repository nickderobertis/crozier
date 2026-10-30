

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ObjectTransferAccessPresignedUrl(UniversalBaseModel):
    """
    A short-lived URL, with the headers that one object store read or write requires.
    """

    expires_at_ms: int = pydantic.Field()
    """
    The time the URL expires, in Unix milliseconds.
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    The headers that the signature covers, which the client must send.
    """

    method: str = pydantic.Field()
    """
    The HTTP method that the client must use.
    """

    url: str = pydantic.Field()
    """
    The full presigned URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
