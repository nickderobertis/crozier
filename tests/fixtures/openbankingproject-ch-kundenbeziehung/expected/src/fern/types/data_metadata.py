

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_metadata_data_classification import DataMetadataDataClassification
from .data_metadata_verification_status import DataMetadataVerificationStatus


class DataMetadata(UniversalBaseModel):
    originator: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ursprungsystem/Institution
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Datenversion
    """

    data_classification: typing_extensions.Annotated[
        typing.Optional[DataMetadataDataClassification],
        FieldMetadata(alias="dataClassification"),
        pydantic.Field(alias="dataClassification"),
    ] = None
    retention_policy: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="retentionPolicy"),
        pydantic.Field(alias="retentionPolicy", description="Aufbewahrungsrichtlinie"),
    ] = None
    """
    Aufbewahrungsrichtlinie
    """

    legal_basis: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="legalBasis"),
        pydantic.Field(alias="legalBasis", description="Rechtsgrundlage der Verarbeitung"),
    ] = None
    """
    Rechtsgrundlage der Verarbeitung
    """

    quality_score: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="qualityScore"),
        pydantic.Field(alias="qualityScore", description="Datenqualitätsbewertung (0-1)"),
    ] = None
    """
    Datenqualitätsbewertung (0-1)
    """

    verification_status: typing_extensions.Annotated[
        typing.Optional[DataMetadataVerificationStatus],
        FieldMetadata(alias="verificationStatus"),
        pydantic.Field(alias="verificationStatus"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
