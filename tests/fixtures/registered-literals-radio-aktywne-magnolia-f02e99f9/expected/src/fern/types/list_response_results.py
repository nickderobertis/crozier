

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recording import Recording


class ListResponseResults(UniversalBaseModel):
    """
    List of recordings.
    """

    count: int = pydantic.Field()
    """
    Total number of recordings that match the request.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of returned recordings.
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of skipped recordings.
    """

    recordings: typing.List[Recording] = pydantic.Field()
    """
    List of recordings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
