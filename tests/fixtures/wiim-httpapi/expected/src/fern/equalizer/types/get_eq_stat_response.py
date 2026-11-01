

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_eq_stat_response_eq_stat import GetEqStatResponseEqStat


class GetEqStatResponse(UniversalBaseModel):
    eq_stat: typing_extensions.Annotated[
        typing.Optional[GetEqStatResponseEqStat], FieldMetadata(alias="EQStat"), pydantic.Field(alias="EQStat")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
