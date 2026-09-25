

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Button(UniversalBaseModel):
    """
    Customizes the button text for form navigation.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text displayed on the button (e.g., "Start", "Next", "Submit").
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
