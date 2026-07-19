

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClientToolSchema(UniversalBaseModel):
    """
    Schema for a client-side tool passed in the request.

    Client-side tools are executed by the client, not the server. When the agent
    calls a client-side tool, execution pauses and returns control to the client
    to execute the tool and provide the result.
    """

    name: str = pydantic.Field()
    """
    The name of the tool function
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of what the tool does
    """

    parameters: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON Schema for the function parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
