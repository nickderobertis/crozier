

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .demo_dataset import DemoDataset


class DemoDatasets(UniversalBaseModel):
    """
    The medallion datasets as they currently exist on S3 (demo data peek).
    """

    datasets: typing.List[DemoDataset]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
