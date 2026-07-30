

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Links(UniversalBaseModel):
    """
    Links to navigate to previous or next pages through the API
    """

    current: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to navigate to the current page through the API
    """

    next: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to navigate to the previous page through the API
    """

    previous: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to navigate to the previous page through the API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
