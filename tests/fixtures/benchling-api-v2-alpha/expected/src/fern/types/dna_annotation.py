

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .sequence_feature_base import SequenceFeatureBase


class DnaAnnotation(SequenceFeatureBase):
    end: typing.Optional[int] = pydantic.Field(default=None)
    """
    0-based exclusive end index. The end of the sequence is always represented as 0.
    """

    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    0-based inclusive start index.
    """

    strand: typing.Optional[int] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
