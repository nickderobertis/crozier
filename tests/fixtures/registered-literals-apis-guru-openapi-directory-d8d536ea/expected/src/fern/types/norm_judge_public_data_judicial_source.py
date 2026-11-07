

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .norm_judge_public_data_judicial_source_type import NormJudgePublicDataJudicialSourceType


class NormJudgePublicDataJudicialSource(UniversalBaseModel):
    """
    The judicial source of the Judge
    """

    name: str = pydantic.Field()
    """
    Name of the Judicial Data Source
    """

    type: NormJudgePublicDataJudicialSourceType = pydantic.Field()
    """
    Type of acquisition of the data source
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the data source, if type is Website
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
