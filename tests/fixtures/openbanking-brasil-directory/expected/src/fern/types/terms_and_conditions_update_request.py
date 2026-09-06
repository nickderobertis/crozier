

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_signing_service import ExternalSigningService


class TermsAndConditionsUpdateRequest(UniversalBaseModel):
    content: typing_extensions.Annotated[
        str, FieldMetadata(alias="Content"), pydantic.Field(alias="Content", description="The MarkDown of the TnC")
    ]
    """
    The MarkDown of the TnC
    """

    external_signing_service: typing_extensions.Annotated[
        typing.Optional[ExternalSigningService],
        FieldMetadata(alias="ExternalSigningService"),
        pydantic.Field(alias="ExternalSigningService"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
