

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ComputationStarted(UniversalBaseModel):
    pipeline_id: str = pydantic.Field()
    """
    ID for created pipeline (=project identifier)
    """

    ref_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Checkpoints IDs for created pipeline
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
