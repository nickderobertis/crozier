

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_quick_amount import CatalogQuickAmount


class CatalogQuickAmountsSettings(UniversalBaseModel):
    """
    A parent Catalog Object model represents a set of Quick Amounts and the settings control the amounts.
    """

    amounts: typing.Optional[typing.List[CatalogQuickAmount]] = pydantic.Field(default=None)
    """
    Represents a set of Quick Amounts at this location.
    """

    eligible_for_auto_amounts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Represents location's eligibility for auto amounts
    The boolean should be consistent with whether there are AUTO amounts in the `amounts`.
    """

    option: str = pydantic.Field()
    """
    Represents the option seller currently uses on Quick Amounts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
