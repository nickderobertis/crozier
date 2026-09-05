

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_node_prompt_template_position import GraphNodePromptTemplatePosition
from .prompt_block_data import PromptBlockData


class GraphNodePromptTemplate(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the node
    """

    position: typing.Optional[GraphNodePromptTemplatePosition] = pydantic.Field(default=None)
    """
    The position of the node
    """

    prompt: PromptBlockData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
