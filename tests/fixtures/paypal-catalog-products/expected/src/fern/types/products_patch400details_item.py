

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_patch400details_item_invalid_parameter_syntax_description import (
    ProductsPatch400DetailsItemInvalidParameterSyntaxDescription,
)
from .products_patch400details_item_invalid_parameter_value_description import (
    ProductsPatch400DetailsItemInvalidParameterValueDescription,
)
from .products_patch400details_item_invalid_patch_path_description import (
    ProductsPatch400DetailsItemInvalidPatchPathDescription,
)
from .products_patch400details_item_missing_required_parameter_description import (
    ProductsPatch400DetailsItemMissingRequiredParameterDescription,
)
from .products_patch400details_item_unsupported_patch_operation_description import (
    ProductsPatch400DetailsItemUnsupportedPatchOperationDescription,
)


class ProductsPatch400DetailsItem_MissingRequiredParameter(UniversalBaseModel):
    issue: typing.Literal["MISSING_REQUIRED_PARAMETER"] = "MISSING_REQUIRED_PARAMETER"
    description: typing.Optional[ProductsPatch400DetailsItemMissingRequiredParameterDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsPatch400DetailsItem_UnsupportedPatchOperation(UniversalBaseModel):
    issue: typing.Literal["UNSUPPORTED_PATCH_OPERATION"] = "UNSUPPORTED_PATCH_OPERATION"
    description: typing.Optional[ProductsPatch400DetailsItemUnsupportedPatchOperationDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsPatch400DetailsItem_InvalidPatchPath(UniversalBaseModel):
    issue: typing.Literal["INVALID_PATCH_PATH"] = "INVALID_PATCH_PATH"
    description: typing.Optional[ProductsPatch400DetailsItemInvalidPatchPathDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsPatch400DetailsItem_InvalidParameterSyntax(UniversalBaseModel):
    issue: typing.Literal["INVALID_PARAMETER_SYNTAX"] = "INVALID_PARAMETER_SYNTAX"
    description: typing.Optional[ProductsPatch400DetailsItemInvalidParameterSyntaxDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProductsPatch400DetailsItem_InvalidParameterValue(UniversalBaseModel):
    issue: typing.Literal["INVALID_PARAMETER_VALUE"] = "INVALID_PARAMETER_VALUE"
    description: typing.Optional[ProductsPatch400DetailsItemInvalidParameterValueDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProductsPatch400DetailsItem = typing_extensions.Annotated[
    typing.Union[
        ProductsPatch400DetailsItem_MissingRequiredParameter,
        ProductsPatch400DetailsItem_UnsupportedPatchOperation,
        ProductsPatch400DetailsItem_InvalidPatchPath,
        ProductsPatch400DetailsItem_InvalidParameterSyntax,
        ProductsPatch400DetailsItem_InvalidParameterValue,
    ],
    pydantic.Field(discriminator="issue"),
]
