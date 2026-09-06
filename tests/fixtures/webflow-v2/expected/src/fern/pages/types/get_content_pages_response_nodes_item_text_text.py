

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetContentPagesResponseNodesItemTextText(UniversalBaseModel):
    """
    The text content of the node
    """

    html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTML content of the text node.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The raw text content of the text node.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
