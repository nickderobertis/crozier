

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .profiles import Profiles


class PersonRetrieve(UniversalBaseModel):
    status: int = pydantic.Field()
    """
    The return status code for individual Person ID request
    """

    data: Profiles
    billed: bool = pydantic.Field()
    """
    Defines if the user was billed for this request.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User supplied metadata that is returned with the request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
