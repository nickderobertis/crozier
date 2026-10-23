

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_register_body_segy_v1data_dataset_properties import DatasetRegisterBodySegyV1DataDatasetProperties
from .dataset_register_body_segy_v1data_endian import DatasetRegisterBodySegyV1DataEndian
from .dataset_register_body_segy_v1data_vector_header_mapping_item import (
    DatasetRegisterBodySegyV1DataVectorHeaderMappingItem,
)


class DatasetRegisterBodySegyV1Data(UniversalBaseModel):
    resource_home_region_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ResourceHomeRegionID"),
        pydantic.Field(
            alias="ResourceHomeRegionID",
            description="The name of the home [cloud environment] region for this OSDU resource object.",
        ),
    ] = None
    """
    The name of the home [cloud environment] region for this OSDU resource object.
    """

    resource_host_region_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="ResourceHostRegionIDs"),
        pydantic.Field(
            alias="ResourceHostRegionIDs",
            description="The name of the host [cloud environment] region(s) for this OSDU resource object.",
        ),
    ] = None
    """
    The name of the host [cloud environment] region(s) for this OSDU resource object.
    """

    resource_curation_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ResourceCurationStatus"),
        pydantic.Field(alias="ResourceCurationStatus", description="Describes the current Curation status."),
    ] = None
    """
    Describes the current Curation status.
    """

    resource_lifecycle_status: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ResourceLifecycleStatus"),
        pydantic.Field(alias="ResourceLifecycleStatus", description="Describes the current Resource Lifecycle status."),
    ] = None
    """
    Describes the current Resource Lifecycle status.
    """

    resource_security_classification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ResourceSecurityClassification"),
        pydantic.Field(
            alias="ResourceSecurityClassification", description="Classifies the security level of the resource."
        ),
    ] = None
    """
    Classifies the security level of the resource.
    """

    source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Source"),
        pydantic.Field(
            alias="Source",
            description="The entity that produced the record, or from which it is received; could be an organization, agency, system, internal team, or individual. For informational purposes only, the list of sources is not governed.",
        ),
    ] = None
    """
    The entity that produced the record, or from which it is received; could be an organization, agency, system, internal team, or individual. For informational purposes only, the list of sources is not governed.
    """

    existence_kind: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExistenceKind"),
        pydantic.Field(
            alias="ExistenceKind",
            description="Where does this data resource sit in the cradle-to-grave span of its existence?",
        ),
    ] = None
    """
    Where does this data resource sit in the cradle-to-grave span of its existence?
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(
            alias="Name",
            description="An optional name of the dataset, e.g. a user friendly file or file collection name.",
        ),
    ] = None
    """
    An optional name of the dataset, e.g. a user friendly file or file collection name.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="An optional, textual description of the dataset."),
    ] = None
    """
    An optional, textual description of the dataset.
    """

    total_size: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TotalSize"),
        pydantic.Field(
            alias="TotalSize",
            description="Total size of the dataset in bytes; for files it is the same as declared in FileSourceInfo.FileSize or the sum of all individual files. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
        ),
    ] = None
    """
    Total size of the dataset in bytes; for files it is the same as declared in FileSourceInfo.FileSize or the sum of all individual files. Implemented as string. The value must be convertible to a long integer (sizes can become very large).
    """

    encoding_format_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EncodingFormatTypeID"),
        pydantic.Field(
            alias="EncodingFormatTypeID",
            description="EncodingFormatType ID reference value relationship. It can be a mime-type or media-type.",
        ),
    ] = None
    """
    EncodingFormatType ID reference value relationship. It can be a mime-type or media-type.
    """

    schema_format_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SchemaFormatTypeID"),
        pydantic.Field(alias="SchemaFormatTypeID", description="Relationship to the SchemaFormatType reference value."),
    ] = None
    """
    Relationship to the SchemaFormatType reference value.
    """

    endian: typing_extensions.Annotated[
        typing.Optional[DatasetRegisterBodySegyV1DataEndian],
        FieldMetadata(alias="Endian"),
        pydantic.Field(
            alias="Endian",
            description='Endianness of binary value.  Enumeration: "BIG", "LITTLE".  If absent, applications will need to interpret from context indicators.',
        ),
    ] = None
    """
    Endianness of binary value.  Enumeration: "BIG", "LITTLE".  If absent, applications will need to interpret from context indicators.
    """

    dataset_properties: typing_extensions.Annotated[
        DatasetRegisterBodySegyV1DataDatasetProperties,
        FieldMetadata(alias="DatasetProperties"),
        pydantic.Field(alias="DatasetProperties", description="The dataset properties for a file collection."),
    ]
    """
    The dataset properties for a file collection.
    """

    vector_header_mapping: typing_extensions.Annotated[
        typing.Optional[typing.List[DatasetRegisterBodySegyV1DataVectorHeaderMappingItem]],
        FieldMetadata(alias="VectorHeaderMapping"),
        pydantic.Field(
            alias="VectorHeaderMapping",
            description="Array of objects which define the meaning and format of a tabular structure used in a binary file as a header.  The initial use case is the trace headers of a SEG-Y file.  Note that some of this information may be repeated in the SEG-Y EBCDIC header.",
        ),
    ] = None
    """
    Array of objects which define the meaning and format of a tabular structure used in a binary file as a header.  The initial use case is the trace headers of a SEG-Y file.  Note that some of this information may be repeated in the SEG-Y EBCDIC header.
    """

    segy_revision: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SEGYRevision"),
        pydantic.Field(
            alias="SEGYRevision", description="The SEG-Y standard revision the SEG-Y file set is conforming to."
        ),
    ] = None
    """
    The SEG-Y standard revision the SEG-Y file set is conforming to.
    """

    extension_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="ExtensionProperties"),
        pydantic.Field(alias="ExtensionProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
