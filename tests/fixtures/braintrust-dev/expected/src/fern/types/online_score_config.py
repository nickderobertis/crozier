

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .online_score_config_scope import OnlineScoreConfigScope
from .online_score_config_scorers_item import OnlineScoreConfigScorersItem


class OnlineScoreConfig(UniversalBaseModel):
    sampling_rate: float = pydantic.Field()
    """
    The sampling rate for online scoring
    """

    scorers: typing.List[OnlineScoreConfigScorersItem] = pydantic.Field()
    """
    The list of functions to run for online scoring. Can include scorers, facets, or other function types.
    """

    btql_filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter logs using BTQL
    """

    apply_to_root_span: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to trigger online scoring on the root span of each trace. Only applies when scope is 'span' or unset.
    """

    apply_to_span_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Trigger online scoring on any spans with a name in this list. Only applies when scope is 'span' or unset.
    """

    skip_logging: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to skip adding scorer spans when computing scores
    """

    scope: typing.Optional[OnlineScoreConfigScope] = pydantic.Field(default=None)
    """
    The scope at which to run the functions. Defaults to span-level execution. Trace/group scope requires all functions to be facets.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
