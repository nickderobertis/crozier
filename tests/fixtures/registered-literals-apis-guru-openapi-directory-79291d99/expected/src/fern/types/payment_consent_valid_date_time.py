

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PaymentConsentValidDateTime(UniversalBaseModel):
    """
    Life span for the payment consent. After the `to` date the payment consent expires and can no longer be used for payment initiation.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="from"),
        pydantic.Field(
            alias="from",
            description="The date and time from which the consent should be active, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.",
        ),
    ] = None
    """
    The date and time from which the consent should be active, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    to: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time at which the consent expires, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
