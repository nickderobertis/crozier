

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_signing_service_name import ExternalSigningServiceName
from .external_signing_service_signer_template_config import ExternalSigningServiceSignerTemplateConfig


class ExternalSigningService(UniversalBaseModel):
    external_signing_service_email_subject: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExternalSigningServiceEmailSubject"),
        pydantic.Field(
            alias="ExternalSigningServiceEmailSubject",
            description="The Subject of the Email for External Signing Service",
        ),
    ] = None
    """
    The Subject of the Email for External Signing Service
    """

    external_signing_service_name: typing_extensions.Annotated[
        typing.Optional[ExternalSigningServiceName],
        FieldMetadata(alias="ExternalSigningServiceName"),
        pydantic.Field(alias="ExternalSigningServiceName"),
    ] = None
    external_signing_service_signer_template_config: typing_extensions.Annotated[
        typing.Optional[ExternalSigningServiceSignerTemplateConfig],
        FieldMetadata(alias="ExternalSigningServiceSignerTemplateConfig"),
        pydantic.Field(alias="ExternalSigningServiceSignerTemplateConfig"),
    ] = None
    external_signing_service_subject: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExternalSigningServiceSubject"),
        pydantic.Field(
            alias="ExternalSigningServiceSubject", description="The Subject of the External Signing Service"
        ),
    ] = None
    """
    The Subject of the External Signing Service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
