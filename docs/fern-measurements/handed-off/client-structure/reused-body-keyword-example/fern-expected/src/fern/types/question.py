

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Question(UniversalBaseModel):
    bench: str = pydantic.Field()
    """
    The bench the question is about.
    """

    asked_by: str = pydantic.Field()
    """
    The grower asking.
    """

    urgent: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a keeper should answer today.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
