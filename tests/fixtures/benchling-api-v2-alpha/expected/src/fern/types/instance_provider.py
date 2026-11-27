

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .barcode_scan_form_instance_provider_identifier_type import BarcodeScanFormInstanceProviderIdentifierType
from .barcode_scan_form_instance_provider_mode import BarcodeScanFormInstanceProviderMode
from .barcode_scan_form_instance_provider_query_value_from_item import BarcodeScanFormInstanceProviderQueryValueFromItem


class InstanceProvider_BarcodeScan(UniversalBaseModel):
    type: typing.Literal["BARCODE_SCAN"] = "BARCODE_SCAN"
    identifier_type: typing_extensions.Annotated[
        typing.Optional[BarcodeScanFormInstanceProviderIdentifierType],
        FieldMetadata(alias="identifierType"),
        pydantic.Field(alias="identifierType"),
    ] = None
    mode: typing.Optional[BarcodeScanFormInstanceProviderMode] = None
    query_value_from: typing_extensions.Annotated[
        typing.Optional[typing.List[BarcodeScanFormInstanceProviderQueryValueFromItem]],
        FieldMetadata(alias="queryValueFrom"),
        pydantic.Field(alias="queryValueFrom"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InstanceProvider_BlankForm(UniversalBaseModel):
    type: typing.Literal["BLANK_FORM"] = "BLANK_FORM"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InstanceProvider_EntitySearch(UniversalBaseModel):
    value: typing.Any
    type: typing.Literal["ENTITY_SEARCH"] = "ENTITY_SEARCH"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


InstanceProvider = typing_extensions.Annotated[
    typing.Union[InstanceProvider_BarcodeScan, InstanceProvider_BlankForm, InstanceProvider_EntitySearch],
    pydantic.Field(discriminator="type"),
]
