

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .dataset_run import DatasetRun
from .dataset_run_item import DatasetRunItem


class DatasetRunWithItems(DatasetRun):
    dataset_run_items: typing_extensions.Annotated[
        typing.List[DatasetRunItem], FieldMetadata(alias="datasetRunItems"), pydantic.Field(alias="datasetRunItems")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
