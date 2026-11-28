

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .knot import Knot
from .weave_plan_finish import WeavePlanFinish
from .weave_plan_pattern import WeavePlanPattern
from .weave_plan_threads_item import WeavePlanThreadsItem


class WeavePlan(UniversalBaseModel):
    """
    What a weave is made of.
    """

    pattern: WeavePlanPattern = pydantic.Field()
    """
    The weave's pattern.
    """

    threads: typing.List[WeavePlanThreadsItem] = pydantic.Field()
    """
    The threads, in order.
    """

    knots: typing.List[Knot] = pydantic.Field()
    """
    The knots tied along the selvedge.
    """

    finish: WeavePlanFinish = pydantic.Field()
    """
    How the cloth is finished.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
