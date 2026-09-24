

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemoteLights(UniversalBaseModel):
    """
    Remote to swith on / off lights.
    """

    true: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Swith, if ```true```, the vehicle lights ON  or OFF (otherwise).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
