

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .checksum import Checksum
from .identifier import Identifier
from .uuid_ import Uuid


class ReleaseDistribution(UniversalBaseModel):
    distribution_id: typing_extensions.Annotated[
        Uuid,
        FieldMetadata(alias="distributionId"),
        pydantic.Field(alias="distributionId", description="A unique identifier for the TEA Distribution object"),
    ]
    """
    A unique identifier for the TEA Distribution object
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free-text description of the distribution.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    List of identifiers specific to this distribution.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Direct download URL for the distribution.
    """

    signature_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signatureUrl"),
        pydantic.Field(
            alias="signatureUrl", description="Direct download URL for the distribution's external signature."
        ),
    ] = None
    """
    Direct download URL for the distribution's external signature.
    """

    checksums: typing.Optional[typing.List[Checksum]] = pydantic.Field(default=None)
    """
    List of checksums for the distribution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
