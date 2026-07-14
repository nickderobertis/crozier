

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LogOperation(UniversalBaseModel):
    """
    The request as defined in OpenApi Spec.
    """

    id: str = pydantic.Field()
    """
    The OpenApi Operation Id associated with the request
    """

    name: str = pydantic.Field()
    """
    The OpenApi Operation name associated with the request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
