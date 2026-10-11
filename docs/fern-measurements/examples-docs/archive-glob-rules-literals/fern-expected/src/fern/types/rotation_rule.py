

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cadence import Cadence


class RotationRule(UniversalBaseModel):
    """
    Keeps snapshots under vault/** /weekly for a month.
    """

    include: str = pydantic.Field()
    """
    Paths such as archive/** /snapshots or /* /tmp.
    """

    keep_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Days to keep; * / marks the end of a cron field.
    """

    cadence: typing.Optional[Cadence] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
