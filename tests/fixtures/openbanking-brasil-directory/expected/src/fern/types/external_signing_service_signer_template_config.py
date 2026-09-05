

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExternalSigningServiceSignerTemplateConfig(UniversalBaseModel):
    signer1template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Signer1TemplateId"),
        pydantic.Field(alias="Signer1TemplateId", description="Template ID for 1 signer"),
    ] = None
    """
    Template ID for 1 signer
    """

    signer1version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Signer1Version"),
        pydantic.Field(alias="Signer1Version", description="Version of the TnC document"),
    ] = None
    """
    Version of the TnC document
    """

    signer2template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Signer2TemplateId"),
        pydantic.Field(alias="Signer2TemplateId", description="Template ID for 2 signers"),
    ] = None
    """
    Template ID for 2 signers
    """

    signer2version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Signer2Version"),
        pydantic.Field(alias="Signer2Version", description="Version of the TnC document"),
    ] = None
    """
    Version of the TnC document
    """

    signer3template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Signer3TemplateId"),
        pydantic.Field(alias="Signer3TemplateId", description="Template ID for 3 signers"),
    ] = None
    """
    Template ID for 3 signers
    """

    signer3version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Signer3Version"),
        pydantic.Field(alias="Signer3Version", description="Version of the TnC document"),
    ] = None
    """
    Version of the TnC document
    """

    signer4template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Signer4TemplateId"),
        pydantic.Field(alias="Signer4TemplateId", description="Template ID for 4 signers"),
    ] = None
    """
    Template ID for 4 signers
    """

    signer4version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Signer4Version"),
        pydantic.Field(alias="Signer4Version", description="Version of the TnC document"),
    ] = None
    """
    Version of the TnC document
    """

    signer5template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Signer5TemplateId"),
        pydantic.Field(alias="Signer5TemplateId", description="Template ID for 5 signers"),
    ] = None
    """
    Template ID for 5 signers
    """

    signer5version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Signer5Version"),
        pydantic.Field(alias="Signer5Version", description="Version of the TnC document"),
    ] = None
    """
    Version of the TnC document
    """

    signer6template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Signer6TemplateId"),
        pydantic.Field(alias="Signer6TemplateId", description="Template ID for 6 signers"),
    ] = None
    """
    Template ID for 6 signers
    """

    signer6version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Signer6Version"),
        pydantic.Field(alias="Signer6Version", description="Version of the TnC document"),
    ] = None
    """
    Version of the TnC document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
