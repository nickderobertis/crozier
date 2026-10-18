

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssistantVersionsSearchRequest(UniversalBaseModel):
    """
    Payload for listing assistant versions.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Metadata to filter versions by. Exact match filter for each KV pair.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of versions to return.
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of versions to skip.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
