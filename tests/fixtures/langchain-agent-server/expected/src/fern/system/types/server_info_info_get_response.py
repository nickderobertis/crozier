

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServerInfoInfoGetResponse(UniversalBaseModel):
    version: str = pydantic.Field()
    """
    LangGraph API version
    """

    langgraph_py_version: str = pydantic.Field()
    """
    LangGraph Python library version
    """

    flags: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Enabled features and capabilities
    """

    metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Server deployment metadata
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
