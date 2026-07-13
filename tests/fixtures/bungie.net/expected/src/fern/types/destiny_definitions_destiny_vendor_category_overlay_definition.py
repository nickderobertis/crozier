

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorCategoryOverlayDefinition(UniversalBaseModel):
    """
    The details of an overlay prompt to show to a user. They are all fairly self-explanatory localized strings that can be shown.
    """

    choice_description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="choiceDescription")] = (
        None
    )
    currency_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="currencyItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this overlay has a currency item that it features, this is said featured item.
    """

    description: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
