

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ActivityTotals(UniversalBaseModel):
    """
    Activity Totals.
    """

    nap_activity: int
    bathroom_activity: int
    bottle_activity: int
    meal_activity: int
    photo_activity: int
    sign_in_activity: int
    sign_out_activity: int
    learning_activity: int
    name_to_face_activity: int
    absent_activity: int
    observation_activity: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
