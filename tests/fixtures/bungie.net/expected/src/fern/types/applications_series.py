

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .applications_datapoint import ApplicationsDatapoint


class ApplicationsSeries(UniversalBaseModel):
    datapoints: typing.Optional[typing.List[ApplicationsDatapoint]] = pydantic.Field(default=None)
    """
    Collection of samples with time and value.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target to which to datapoints apply.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
