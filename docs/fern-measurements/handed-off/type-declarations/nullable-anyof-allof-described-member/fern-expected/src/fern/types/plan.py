

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .diet import Diet
from .herb import Herb
from .plan_course import PlanCourse
from .plan_extras import PlanExtras
from .plan_sides import PlanSides


class Plan(UniversalBaseModel):
    plan_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="planId"), pydantic.Field(alias="planId")
    ] = None
    course: typing.Optional[PlanCourse] = pydantic.Field(default=None)
    """
    The planned course.
    """

    garnish: typing.Optional[Herb] = None
    pairing: typing.Optional[Diet] = None
    sides: typing.Optional[PlanSides] = pydantic.Field(default=None)
    """
    The side dish, whichever kind.
    """

    extras: typing.Optional[PlanExtras] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
