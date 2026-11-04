

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Policy(UniversalBaseModel):
    """
    A new Policy Management System
    """

    id: str = pydantic.Field()
    """
    Unique id
    """

    url: str = pydantic.Field()
    """
    The URL of the Policy Management System
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description for the Policy Management System
    """

    type: str = pydantic.Field()
    """
    The type for new Policy Management System
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
