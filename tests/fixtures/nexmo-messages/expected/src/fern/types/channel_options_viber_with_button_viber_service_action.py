

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChannelOptionsViberWithButtonViberServiceAction(UniversalBaseModel):
    """
    Node for Viber action buttons.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text which is rendered on the action button.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URL which is requested when the action button is clicked.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
