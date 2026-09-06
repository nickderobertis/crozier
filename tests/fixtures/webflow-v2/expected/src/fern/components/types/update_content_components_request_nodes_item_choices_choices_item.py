

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateContentComponentsRequestNodesItemChoicesChoicesItem(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    The value of the choice when selected.
    """

    text: str = pydantic.Field()
    """
    The text to display for the choice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
