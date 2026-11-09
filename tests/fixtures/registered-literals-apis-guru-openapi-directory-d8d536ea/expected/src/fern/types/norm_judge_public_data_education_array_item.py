

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NormJudgePublicDataEducationArrayItem(UniversalBaseModel):
    degree: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Degree Awarded to the Judge
    """

    school: typing.Optional[str] = pydantic.Field(default=None)
    """
    The University which awarded the degree to the Judge.
    """

    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    The year when the degree was awarded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
