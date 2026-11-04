

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TrackJourneyEventRequestIdentificationAccount(UniversalBaseModel):
    """
    Account identification requires an accountId, domain or both
    """

    account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountId"),
        pydantic.Field(alias="accountId", description="Unique identifier for the account in your database"),
    ] = None
    """
    Unique identifier for the account in your database
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain associated with the account (e.g. acme-inc.com)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
