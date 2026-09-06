

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetPropertiesComponentsResponsePropertiesItemText(UniversalBaseModel):
    """
    Represents text content within the DOM. It contains both the raw text and its HTML representation.
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
