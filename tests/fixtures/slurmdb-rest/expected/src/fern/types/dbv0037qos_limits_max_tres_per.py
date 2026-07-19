

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037qos_limits_max_tres_per_account_item import Dbv0037QosLimitsMaxTresPerAccountItem
from .dbv0037qos_limits_max_tres_per_job_item import Dbv0037QosLimitsMaxTresPerJobItem
from .dbv0037qos_limits_max_tres_per_node_item import Dbv0037QosLimitsMaxTresPerNodeItem
from .dbv0037qos_limits_max_tres_per_user_item import Dbv0037QosLimitsMaxTresPerUserItem


class Dbv0037QosLimitsMaxTresPer(UniversalBaseModel):
    """
    Max TRES per settings
    """

    account: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresPerAccountItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    job: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresPerJobItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    node: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresPerNodeItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    user: typing.Optional[typing.List[Dbv0037QosLimitsMaxTresPerUserItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
