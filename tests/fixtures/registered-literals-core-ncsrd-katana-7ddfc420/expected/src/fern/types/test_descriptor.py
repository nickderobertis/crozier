

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_descriptor_performance_monitoring import TestDescriptorPerformanceMonitoring
from .test_descriptor_performance_prediction import TestDescriptorPerformancePrediction


class TestDescriptor(UniversalBaseModel):
    """
    This is the schema for the Test Descriptor part of slice IM
    """

    probe_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of probe ids to be included in the slice
    """

    performance_monitoring: typing.Optional[TestDescriptorPerformanceMonitoring] = pydantic.Field(default=None)
    """
    This attribute provides the capability to monitor KQIs and KPIs.
    """

    performance_prediction: typing.Optional[TestDescriptorPerformancePrediction] = pydantic.Field(default=None)
    """
    This attribute provides the capability to predict KQIs and KPIs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
