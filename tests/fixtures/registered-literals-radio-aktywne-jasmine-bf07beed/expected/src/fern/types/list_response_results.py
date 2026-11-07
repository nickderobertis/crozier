

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prerecording import Prerecording


class ListResponseResults(UniversalBaseModel):
    """
    List of prerecordings.
    """

    count: int = pydantic.Field()
    """
    Total number of prerecordings that match the request.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of returned prerecordings.
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of skipped prerecordings.
    """

    prerecordings: typing.List[Prerecording] = pydantic.Field()
    """
    List of prerecordings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
