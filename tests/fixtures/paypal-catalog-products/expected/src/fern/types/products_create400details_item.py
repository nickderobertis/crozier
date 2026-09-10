

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_create400details_item_a_required_field_is_missing_issue import (
    ProductsCreate400DetailsItemARequiredFieldIsMissingIssue,
)
from .products_create400details_item_input_identifier_must_not_use_system_prefix_prod_issue import (
    ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue,
)
from .products_create400details_item_the_value_of_a_field_does_not_conform_to_the_expected_format_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue,
)
from .products_create400details_item_the_value_of_a_field_is_invalid_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue,
)
from .products_create400details_item_the_value_of_a_field_is_too_long_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue,
)
from .products_create400details_item_the_value_of_a_field_is_too_short_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue,
)


class ProductsCreate400DetailsItem_InputIdentifierMustNotUseSystemPrefixProd(UniversalBaseModel):
    description: typing.Literal["Input identifier must not use system prefix(PROD-)."] = (
        "Input identifier must not use system prefix(PROD-)."
    )
    issue: typing.Optional[ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsCreate400DetailsItem_TheValueOfAFieldDoesNotConformToTheExpectedFormat(UniversalBaseModel):
    description: typing.Literal["The value of a field does not conform to the expected format."] = (
        "The value of a field does not conform to the expected format."
    )
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsCreate400DetailsItem_TheValueOfAFieldIsInvalid(UniversalBaseModel):
    description: typing.Literal["The value of a field is invalid."] = "The value of a field is invalid."
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsCreate400DetailsItem_ARequiredFieldIsMissing(UniversalBaseModel):
    description: typing.Literal["A required field is missing."] = "A required field is missing."
    issue: typing.Optional[ProductsCreate400DetailsItemARequiredFieldIsMissingIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsCreate400DetailsItem_TheValueOfAFieldIsTooShort(UniversalBaseModel):
    description: typing.Literal["The value of a field is too short."] = "The value of a field is too short."
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsCreate400DetailsItem_TheValueOfAFieldIsTooLong(UniversalBaseModel):
    description: typing.Literal["The value of a field is too long."] = "The value of a field is too long."
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProductsCreate400DetailsItem = typing_extensions.Annotated[
    typing.Union[
        ProductsCreate400DetailsItem_InputIdentifierMustNotUseSystemPrefixProd,
        ProductsCreate400DetailsItem_TheValueOfAFieldDoesNotConformToTheExpectedFormat,
        ProductsCreate400DetailsItem_TheValueOfAFieldIsInvalid,
        ProductsCreate400DetailsItem_ARequiredFieldIsMissing,
        ProductsCreate400DetailsItem_TheValueOfAFieldIsTooShort,
        ProductsCreate400DetailsItem_TheValueOfAFieldIsTooLong,
    ],
    pydantic.Field(discriminator="description"),
]
