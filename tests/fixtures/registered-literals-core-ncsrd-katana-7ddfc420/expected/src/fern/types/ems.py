

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ems(UniversalBaseModel):
    """
    A new EMS
    """

    id: str = pydantic.Field()
    """
    Unique id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the new EMS
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description for the EMS
    """

    url: str = pydantic.Field()
    """
    EMS' authentication URL - example: http://10.200.64.2:5000/
    """

    type: str = pydantic.Field()
    """
    EMS' type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
