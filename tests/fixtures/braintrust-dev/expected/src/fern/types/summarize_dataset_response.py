

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_summary import DataSummary


class SummarizeDatasetResponse(UniversalBaseModel):
    """
    Summary of a dataset
    """

    project_name: str = pydantic.Field()
    """
    Name of the project that the dataset belongs to
    """

    dataset_name: str = pydantic.Field()
    """
    Name of the dataset
    """

    project_url: str = pydantic.Field()
    """
    URL to the project's page in the Braintrust app
    """

    dataset_url: str = pydantic.Field()
    """
    URL to the dataset's page in the Braintrust app
    """

    data_summary: typing.Optional[DataSummary] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
