

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookUrlOptionItem(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parameter variable to encode the users input for this
    option in the integrations webhook URL.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable label of the url option.
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
