

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookEventLogService(UniversalBaseModel):
    """
    Apideck service provider associated with event.
    """

    id: str = pydantic.Field()
    """
    Apideck service provider id.
    """

    name: str = pydantic.Field()
    """
    Apideck service provider name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
