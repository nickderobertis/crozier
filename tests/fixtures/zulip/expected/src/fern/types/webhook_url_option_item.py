

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookUrlOptionItem(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the URL parameter.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label used for the input field in the UI.
    """

    input_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of input field this URL parameter maps to in the UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
