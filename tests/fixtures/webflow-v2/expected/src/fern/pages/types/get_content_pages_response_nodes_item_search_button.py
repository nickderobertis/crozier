

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetContentPagesResponseNodesItemSearchButton(UniversalBaseModel):
    """
    Represents search button elements within the DOM. It contains the text of the button. Additional attributes can be associated with the text for styling or other purposes.
    """

    id: str = pydantic.Field()
    """
    Node UUID
    """

    value: str = pydantic.Field()
    """
    The text content of the search button.
    """

    attributes: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The custom attributes of the node
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
