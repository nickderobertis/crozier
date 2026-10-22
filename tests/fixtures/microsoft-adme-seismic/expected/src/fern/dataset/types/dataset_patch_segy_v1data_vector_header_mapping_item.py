

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_patch_segy_v1data_vector_header_mapping_item_scalar_indicator import (
    DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator,
)


class DatasetPatchSegyV1DataVectorHeaderMappingItem(UniversalBaseModel):
    """
    Array of objects which define the meaning and format of a tabular structure used in a binary file as a header.  The initial use case is the trace headers of a SEG-Y file.  Note that some of this information may be repeated in the SEG-Y EBCDIC header.
    """

    key_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="KeyName"),
        pydantic.Field(
            alias="KeyName",
            description="Relationship to a reference value for a name of a property header such as INLINE, CDPX.",
        ),
    ] = None
    """
    Relationship to a reference value for a name of a property header such as INLINE, CDPX.
    """

    word_format: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="WordFormat"),
        pydantic.Field(
            alias="WordFormat",
            description="Relationship to a reference value for binary data types, such as INT, UINT, FLOAT, IBM_FLOAT, ASCII, EBCDIC.",
        ),
    ] = None
    """
    Relationship to a reference value for binary data types, such as INT, UINT, FLOAT, IBM_FLOAT, ASCII, EBCDIC.
    """

    word_width: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="WordWidth"),
        pydantic.Field(alias="WordWidth", description="Size of the word in bytes."),
    ] = None
    """
    Size of the word in bytes.
    """

    position: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Position"),
        pydantic.Field(alias="Position", description="Beginning byte position of header value, 1 indexed."),
    ] = None
    """
    Beginning byte position of header value, 1 indexed.
    """

    uo_m: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UoM"),
        pydantic.Field(
            alias="UoM", description="Relationship to units of measure reference if header standard is not followed."
        ),
    ] = None
    """
    Relationship to units of measure reference if header standard is not followed.
    """

    scalar_indicator: typing_extensions.Annotated[
        typing.Optional[DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator],
        FieldMetadata(alias="ScalarIndicator"),
        pydantic.Field(
            alias="ScalarIndicator",
            description="Enumerated string indicating whether to use the normal scalar field for scaling this field (STANDARD), no scaling (NOSCALE), or override scalar (OVERRIDE).  Default is current STANDARD (such as SEG-Y rev2).",
        ),
    ] = None
    """
    Enumerated string indicating whether to use the normal scalar field for scaling this field (STANDARD), no scaling (NOSCALE), or override scalar (OVERRIDE).  Default is current STANDARD (such as SEG-Y rev2).
    """

    scalar_override: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="ScalarOverride"),
        pydantic.Field(
            alias="ScalarOverride",
            description="Scalar value (as defined by standard) when a value present in the header needs to be overwritten for this value.",
        ),
    ] = None
    """
    Scalar value (as defined by standard) when a value present in the header needs to be overwritten for this value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
