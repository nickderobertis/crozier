

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BrowserReleaseFeatureMetric(UniversalBaseModel):
    timestamp: dt.datetime = pydantic.Field()
    """
    The timestamp that correlates to an event that may influence the count of features for a browser. This may be the release of the browser itself (when a browser may support a new set of features), or the release of another browser (when another browser supports a feature but our specified browser is now lagging behind with a new feature). Refer to the individual endpoint for more context on the use of this component.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total count of features.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
