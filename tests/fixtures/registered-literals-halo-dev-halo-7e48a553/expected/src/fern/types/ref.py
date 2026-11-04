

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ref(UniversalBaseModel):
    """
    Extension reference object. The name is mandatory
    """

    group: str = pydantic.Field()
    """
    Extension group
    """

    kind: str = pydantic.Field()
    """
    Extension kind
    """

    name: str = pydantic.Field()
    """
    Extension name. This field is mandatory
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Extension version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
