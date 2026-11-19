

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataset_ref import DatasetRef


class Neighbors(UniversalBaseModel):
    """
    Datasets related to ``dataset`` (upstream provenance or downstream impact).
    """

    dataset: str
    related: typing.List[DatasetRef]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
