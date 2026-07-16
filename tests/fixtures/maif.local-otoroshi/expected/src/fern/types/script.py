

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Script(UniversalBaseModel):
    """
    A script to transformer otoroshi requests
    """

    code: typing.Dict[str, str] = pydantic.Field()
    """
    The code of the script
    """

    desc: typing.Dict[str, str] = pydantic.Field()
    """
    The description of the script
    """

    id: str = pydantic.Field()
    """
    The id of the script
    """

    name: str = pydantic.Field()
    """
    The name of the script
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
