

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dbv0037diag_statistics_rollups import Dbv0037DiagStatisticsRollups
from .dbv0037diag_statistics_rp_cs import Dbv0037DiagStatisticsRpCs
from .dbv0037diag_statistics_users import Dbv0037DiagStatisticsUsers


class Dbv0037DiagStatistics(UniversalBaseModel):
    time_start: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp of start time
    """

    rollups: typing.Optional[typing.List[Dbv0037DiagStatisticsRollups]] = None
    rp_cs: typing_extensions.Annotated[
        typing.Optional[typing.List[Dbv0037DiagStatisticsRpCs]],
        FieldMetadata(alias="RPCs"),
        pydantic.Field(alias="RPCs"),
    ] = None
    users: typing.Optional[typing.List[Dbv0037DiagStatisticsUsers]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
