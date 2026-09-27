

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FamilyBalanceAggregateGroup(UniversalBaseModel):
    school_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    family_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
