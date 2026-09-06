

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorisation_domain_role_name import AuthorisationDomainRoleName
from .metadata_id import MetadataId


class MetadataResponse(UniversalBaseModel):
    domain_role_name: typing_extensions.Annotated[
        typing.Optional[AuthorisationDomainRoleName],
        FieldMetadata(alias="DomainRoleName"),
        pydantic.Field(alias="DomainRoleName"),
    ] = None
    metadata_id: typing_extensions.Annotated[
        typing.Optional[MetadataId], FieldMetadata(alias="MetadataId"), pydantic.Field(alias="MetadataId")
    ] = None
    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the metadata object"),
    ] = None
    """
    The name of the metadata object
    """

    type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The type of metadata i.e. scope, grant_type..."),
    ] = None
    """
    The type of metadata i.e. scope, grant_type...
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
