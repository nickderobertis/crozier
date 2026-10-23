

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetChainsChainIdAssetsSymbolHistoryResponseCoverage(UniversalBaseModel):
    days_on_record: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="daysOnRecord"), pydantic.Field(alias="daysOnRecord")
    ] = None
    first_day: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstDay"), pydantic.Field(alias="firstDay")
    ] = None
    latest_day: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="latestDay"), pydantic.Field(alias="latestDay")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
