

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.alert import Alert


class GetAlertsResponse(UniversalBaseModel):
    alerts: typing.List[Alert] = pydantic.Field()
    """
    The list of alerts
    """

    has_more: bool = pydantic.Field()
    """
    True if there are more alerts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
