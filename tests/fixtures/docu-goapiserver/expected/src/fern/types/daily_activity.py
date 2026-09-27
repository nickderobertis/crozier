

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DailyActivity(UniversalBaseModel):
    """
    Daily Activity.
    """

    activiable: typing.Any
    activity_date: str
    activity_time: str
    activity_type: str = pydantic.Field()
    """
    Activity kind supplied by Procare, for example bottle_activity, meal_activity, bathroom_activity, nap_activity, sign_in_activity, sign_out_activity, learning_activity or photo_activity.
    """

    batch_id: str = pydantic.Field()
    """
    Batch id.
    """

    comment: typing.Optional[str] = None
    data: typing.Any
    id: str
    indicators: typing.Optional[typing.List[typing.Any]] = None
    is_staff_only: bool
    kid_ids: typing.Optional[typing.List[str]] = None
    measures: typing.Optional[typing.List[typing.Any]] = None
    photo_url: typing.Optional[str] = None
    reminder_active: typing.Optional[bool] = None
    staff_present_id: str = pydantic.Field()
    """
    Staff present id.
    """

    staff_present_name: str
    teacher_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
