

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoginFlow(UniversalBaseModel):
    """
    An individual login flow which can be used to sign into the remote network.
    """

    name: str = pydantic.Field()
    """
    A human-readable name for the login flow.
    """

    description: str = pydantic.Field()
    """
    A human-readable description of the login flow.
    """

    id: str = pydantic.Field()
    """
    An internal ID that is passed to the /login/start call to start a login with this flow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
