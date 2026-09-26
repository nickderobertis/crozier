

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attribute_set import AttributeSet
from .url import Url


class Webhook(UniversalBaseModel):
    """
    Defines the webhook for htp notification .
    """

    target: Url
    name: str = pydantic.Field()
    """
    Webhook name.
    """

    attributes: typing.Optional[AttributeSet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
