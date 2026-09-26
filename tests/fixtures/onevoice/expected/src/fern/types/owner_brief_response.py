

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OwnerBriefResponse(UniversalBaseModel):
    enabled: bool = pydantic.Field()
    """
    Whether the proactive weekly owner-brief DM is enabled. Default-on:
    true when the business never set a preference.
    """

    weekday: int = pydantic.Field()
    """
    Weekday the brief fires on (0=Sunday .. 6=Saturday).
    """

    hour: int = pydantic.Field()
    """
    Hour-of-day (0-23) the brief fires at.
    """

    last_sent: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastSent"),
        pydantic.Field(
            alias="lastSent",
            description='ISO year-week ("<year>-W<week>") of the last successful send; absent\nwhen a brief has never been sent.',
        ),
    ] = None
    """
    ISO year-week ("<year>-W<week>") of the last successful send; absent
    when a brief has never been sent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
