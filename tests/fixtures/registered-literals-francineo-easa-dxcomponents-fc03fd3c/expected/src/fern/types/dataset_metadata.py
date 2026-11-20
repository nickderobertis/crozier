

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dataset_metadata_description import DatasetMetadataDescription
from .dataset_metadata_provider import DatasetMetadataProvider
from .dataset_metadata_technical_limitation import DatasetMetadataTechnicalLimitation


class DatasetMetadata(UniversalBaseModel):
    """
    Global information that qualifies and constrains the usage of the data contained in the associated data set.
    """

    valid_from: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="validFrom"),
        pydantic.Field(alias="validFrom", description="RFC3339 Datetime"),
    ] = None
    """
    RFC3339 Datetime
    """

    valid_to: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="validTo"),
        pydantic.Field(alias="validTo", description="RFC3339 Datetime"),
    ] = None
    """
    RFC3339 Datetime
    """

    provider: typing.Optional[DatasetMetadataProvider] = pydantic.Field(default=None)
    """
    A free text with a maximum length of 200 characters, optionally accompanied
    by an indication of the language in which the text is written.
    """

    issued: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    RFC3339 Datetime
    """

    description: typing.Optional[DatasetMetadataDescription] = pydantic.Field(default=None)
    """
    A free text with a maximum length of 200 characters, optionally accompanied
    by an indication of the language in which the text is written.
    """

    technical_limitation: typing_extensions.Annotated[
        typing.Optional[DatasetMetadataTechnicalLimitation],
        FieldMetadata(alias="technicalLimitation"),
        pydantic.Field(
            alias="technicalLimitation",
            description="A free text with a maximum length of 200 characters, optionally accompanied\nby an indication of the language in which the text is written.",
        ),
    ] = None
    """
    A free text with a maximum length of 200 characters, optionally accompanied
    by an indication of the language in which the text is written.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
