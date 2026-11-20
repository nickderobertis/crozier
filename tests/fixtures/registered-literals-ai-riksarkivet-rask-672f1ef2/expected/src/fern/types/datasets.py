

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataset_summary import DatasetSummary


class Datasets(UniversalBaseModel):
    """
    A governed, paginated page of datasets the caller may see (the lineage catalog landing list).

    ``total`` is the count of *visible* datasets before the page slice — so a UI can show "X–Y of total".
    """

    datasets: typing.List[DatasetSummary]
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
