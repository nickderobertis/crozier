

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Filter(UniversalBaseModel):
    """
    Filter applied to route data. Controls which notefiles are sent through the route.
    """

    files: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of notefile names or patterns to filter on.
    """

    system_notefiles: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether system notefiles should be included.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of filter to apply (corresponds to `hublib.NotefileFilterType`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
