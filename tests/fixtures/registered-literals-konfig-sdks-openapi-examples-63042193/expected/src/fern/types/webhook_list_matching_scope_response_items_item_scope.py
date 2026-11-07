

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookListMatchingScopeResponseItemsItemScope(UniversalBaseModel):
    """
    The scope in which the relevant events that will trigger webhooks
    """

    id: str = pydantic.Field()
    """
    ID of the scope being used (at the moment, only project ID is supported)
    """

    type: str = pydantic.Field()
    """
    Type of the scope being used
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
