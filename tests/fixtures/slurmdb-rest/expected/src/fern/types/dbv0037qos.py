

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits import Dbv0037QosLimits
from .dbv0037qos_preempt import Dbv0037QosPreempt


class Dbv0037Qos(UniversalBaseModel):
    """
    QOS description
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    QOS description
    """

    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of properties of QOS
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Database id
    """

    limits: typing.Optional[Dbv0037QosLimits] = None
    preempt: typing.Optional[Dbv0037QosPreempt] = None
    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    QOS priority
    """

    usage_factor: typing.Optional[float] = pydantic.Field(default=None)
    """
    Usage factor
    """

    usage_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Usage threshold
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
