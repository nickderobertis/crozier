

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookConfigOptionItem(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A key for the configuration option.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable label of the configuration option.
    """

    validator: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the validator function for the configuration
    option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
