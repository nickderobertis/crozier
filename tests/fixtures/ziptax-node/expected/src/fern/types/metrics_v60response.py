

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetricsV60Response(UniversalBaseModel):
    is_active: bool = pydantic.Field()
    """
    Whether the account is currently active.
    """

    message: str = pydantic.Field()
    """
    Informational message about the account.
    """

    request_count: int = pydantic.Field()
    """
    Number of requests consumed in the current period.
    """

    request_limit: int = pydantic.Field()
    """
    Maximum requests allowed for the account in the current period.
    """

    usage_percent: float = pydantic.Field()
    """
    Request usage as a percentage of the limit (0-100).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
