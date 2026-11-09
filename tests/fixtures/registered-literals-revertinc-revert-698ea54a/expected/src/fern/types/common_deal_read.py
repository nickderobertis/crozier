

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonDealRead(UniversalBaseModel):
    amount: int = pydantic.Field()
    """
    The deal amount mentioned in the CRM for this deal.
    """

    priority: typing.Optional[str] = pydantic.Field(default=None)
    """
    The priority attached to this deal. (not supported by pipedrive)
    """

    stage: str = pydantic.Field()
    """
    Deal stage in the CRM.
    """

    name: str = pydantic.Field()
    """
    The name of the deal in a CRM.
    """

    expected_close_date: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="expectedCloseDate"), pydantic.Field(alias="expectedCloseDate")
    ]
    is_won: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isWon"),
        pydantic.Field(alias="isWon", description="Is `true` if the deal is closed (won)."),
    ]
    """
    Is `true` if the deal is closed (won).
    """

    probability: int = pydantic.Field()
    """
    Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
