

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Limits(UniversalBaseModel):
    """
    List of limitations on used resources, that are applied on the current instance of Registry.
    Keys represent the resource type and are suffixed by the corresponding unit.
    Values are integers. Only non-negative values are allowed, with the exception of -1, which means that the limit is not applied.
    """

    max_artifact_description_length_chars: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxArtifactDescriptionLengthChars")
    ] = None
    max_artifact_labels_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxArtifactLabelsCount")
    ] = None
    max_artifact_name_length_chars: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxArtifactNameLengthChars")
    ] = None
    max_artifact_properties_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxArtifactPropertiesCount")
    ] = None
    max_artifacts_count: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxArtifactsCount")] = (
        None
    )
    max_label_size_bytes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxLabelSizeBytes")
    ] = None
    max_property_key_size_bytes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxPropertyKeySizeBytes")
    ] = None
    max_property_value_size_bytes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxPropertyValueSizeBytes")
    ] = None
    max_requests_per_second_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxRequestsPerSecondCount")
    ] = None
    max_schema_size_bytes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxSchemaSizeBytes")
    ] = None
    max_total_schemas_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxTotalSchemasCount")
    ] = None
    max_versions_per_artifact_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxVersionsPerArtifactCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
