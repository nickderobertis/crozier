

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .glitchtip_project_alert_recipient import GlitchtipProjectAlertRecipient


class GlitchtipProjectAlert(UniversalBaseModel):
    """
    Desired state for a single project alert.
    """

    name: str = pydantic.Field()
    """
    Alert name (unique identifier within a project)
    """

    quantity: int = pydantic.Field()
    """
    Number of events to trigger the alert
    """

    recipients: typing.Optional[typing.List[GlitchtipProjectAlertRecipient]] = pydantic.Field(default=None)
    """
    List of alert recipients
    """

    timespan_minutes: int = pydantic.Field()
    """
    Time window in minutes for alert evaluation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
