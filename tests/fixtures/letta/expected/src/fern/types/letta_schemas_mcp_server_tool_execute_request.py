

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LettaSchemasMcpServerToolExecuteRequest(UniversalBaseModel):
    """
    Request to execute a tool.
    """

    args: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Arguments to pass to the tool
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
