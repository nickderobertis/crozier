

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListWebhooksResponseWebhooksItemFilter(UniversalBaseModel):
    """
    Only supported for the `form_submission` trigger type. Filter for the form you want Webhooks to be sent for.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the form you'd like to recieve notifications for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
