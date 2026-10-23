

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebhookDeliveryWatcher(UniversalBaseModel):
    """
    null for a ping, which belongs to the endpoint rather than to any watcher.
    """

    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    kind: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
