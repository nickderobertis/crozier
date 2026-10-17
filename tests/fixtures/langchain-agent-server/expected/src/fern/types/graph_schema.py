

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GraphSchema(UniversalBaseModel):
    """
    Defines the structure and properties of a graph.
    """

    graph_id: str = pydantic.Field()
    """
    The ID of the graph.
    """

    input_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The schema for the graph input. Missing if unable to generate JSON schema from graph.
    """

    output_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The schema for the graph output. Missing if unable to generate JSON schema from graph.
    """

    state_schema: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The schema for the graph state. Missing if unable to generate JSON schema from graph.
    """

    config_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The schema for the graph config. Missing if unable to generate JSON schema from graph.
    """

    context_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The schema for the graph context. Missing if unable to generate JSON schema from graph.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
