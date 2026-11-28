

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .barcode_scan_form_instance_provider_identifier_type import BarcodeScanFormInstanceProviderIdentifierType
from .barcode_scan_form_instance_provider_mode import BarcodeScanFormInstanceProviderMode
from .barcode_scan_form_instance_provider_query_value_from_item import BarcodeScanFormInstanceProviderQueryValueFromItem
from .barcode_scan_form_instance_provider_type import BarcodeScanFormInstanceProviderType


class BarcodeScanFormInstanceProvider(UniversalBaseModel):
    identifier_type: typing_extensions.Annotated[
        typing.Optional[BarcodeScanFormInstanceProviderIdentifierType],
        FieldMetadata(alias="identifierType"),
        pydantic.Field(
            alias="identifierType",
            description="How we identify the entity that we should query for. Because Benchling entities have several different ways of declaring identity, we also must allow for different ways they can be distinguished by their barcodes.",
        ),
    ] = None
    """
    How we identify the entity that we should query for. Because Benchling entities have several different ways of declaring identity, we also must allow for different ways they can be distinguished by their barcodes.
    """

    mode: typing.Optional[BarcodeScanFormInstanceProviderMode] = pydantic.Field(default=None)
    """
    How we differentiate between single scan mode and multiple scan mode. This will allow a user to either choose to scan and load one barcode at a time or multiple barcodes.
    """

    query_value_from: typing_extensions.Annotated[
        typing.Optional[typing.List[BarcodeScanFormInstanceProviderQueryValueFromItem]],
        FieldMetadata(alias="queryValueFrom"),
        pydantic.Field(
            alias="queryValueFrom",
            description="Because in some contexts barcodes are not necessarily unique, we must also allow for ways to construct the actual value that we should use to match a Benchling entity with. An example here would be entities whose names are constructed like: <barcode>-<crop>",
        ),
    ] = None
    """
    Because in some contexts barcodes are not necessarily unique, we must also allow for ways to construct the actual value that we should use to match a Benchling entity with. An example here would be entities whose names are constructed like: <barcode>-<crop>
    """

    type: typing.Optional[BarcodeScanFormInstanceProviderType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
