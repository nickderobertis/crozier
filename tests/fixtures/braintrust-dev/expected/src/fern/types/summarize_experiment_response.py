

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metric_summary import MetricSummary
from .score_summary import ScoreSummary


class SummarizeExperimentResponse(UniversalBaseModel):
    """
    Summary of an experiment
    """

    project_name: str = pydantic.Field()
    """
    Name of the project that the experiment belongs to
    """

    experiment_name: str = pydantic.Field()
    """
    Name of the experiment
    """

    project_url: str = pydantic.Field()
    """
    URL to the project's page in the Braintrust app
    """

    experiment_url: str = pydantic.Field()
    """
    URL to the experiment's page in the Braintrust app
    """

    comparison_experiment_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The experiment which scores are baselined against
    """

    scores: typing.Optional[typing.Dict[str, typing.Optional[ScoreSummary]]] = pydantic.Field(default=None)
    """
    Summary of the experiment's scores
    """

    metrics: typing.Optional[typing.Dict[str, typing.Optional[MetricSummary]]] = pydantic.Field(default=None)
    """
    Summary of the experiment's metrics
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
