

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_tokens_address_response_reading_robinhood_app_match import GetTokensAddressResponseReadingRobinhoodAppMatch
from .get_tokens_address_response_reading_robinhood_app_pairs_item import (
    GetTokensAddressResponseReadingRobinhoodAppPairsItem,
)
from .get_tokens_address_response_reading_robinhood_app_status import GetTokensAddressResponseReadingRobinhoodAppStatus


class GetTokensAddressResponseReadingRobinhoodApp(UniversalBaseModel):
    source: str
    observed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="observedAt"), pydantic.Field(alias="observedAt")
    ] = None
    age_seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ageSeconds"), pydantic.Field(alias="ageSeconds")
    ] = None
    stale: bool
    error: typing.Optional[str] = None
    status: GetTokensAddressResponseReadingRobinhoodAppStatus
    pairs: typing.List[GetTokensAddressResponseReadingRobinhoodAppPairsItem]
    match: GetTokensAddressResponseReadingRobinhoodAppMatch

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
