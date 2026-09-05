

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .envelope_summary import EnvelopeSummary


class DocusignPostData(UniversalBaseModel):
    """
    Data associated with the docusign event
    """

    envelope_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="envelopeId"),
        pydantic.Field(alias="envelopeId", description="The envelope ID"),
    ] = None
    """
    The envelope ID
    """

    envelope_summary: typing_extensions.Annotated[
        typing.Optional[EnvelopeSummary],
        FieldMetadata(alias="envelopeSummary"),
        pydantic.Field(alias="envelopeSummary"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
