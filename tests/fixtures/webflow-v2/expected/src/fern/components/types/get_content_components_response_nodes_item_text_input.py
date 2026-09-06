

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetContentComponentsResponseNodesItemTextInput(UniversalBaseModel):
    """
    Represents text input and textarea elements within the DOM. It contains the placeholder text in the input. Additional attributes can be associated with the text for styling or other purposes.
    """

    id: str = pydantic.Field()
    """
    Node UUID
    """

    placeholder: str = pydantic.Field()
    """
    The placeholder text of the input node
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
