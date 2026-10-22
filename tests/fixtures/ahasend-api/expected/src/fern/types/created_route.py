

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .route import Route


class CreatedRoute(Route):
    secret: str = pydantic.Field()
    """
    Route signing secret. Returned only when the route is created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
