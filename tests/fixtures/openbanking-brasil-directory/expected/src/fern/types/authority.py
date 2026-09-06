

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authority_id import AuthorityId
from .status_enum import StatusEnum


class Authority(UniversalBaseModel):
    authority_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityCode"),
        pydantic.Field(alias="AuthorityCode", description="Code of the Authority i.e. FCA, etc"),
    ] = None
    """
    Code of the Authority i.e. FCA, etc
    """

    authority_country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityCountry"),
        pydantic.Field(alias="AuthorityCountry", description="country of the Authority"),
    ] = None
    """
    country of the Authority
    """

    authority_id: typing_extensions.Annotated[
        typing.Optional[AuthorityId], FieldMetadata(alias="AuthorityId"), pydantic.Field(alias="AuthorityId")
    ] = None
    authority_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityName"),
        pydantic.Field(alias="AuthorityName", description="Name of the Authority i.e. FCA, etc"),
    ] = None
    """
    Name of the Authority i.e. FCA, etc
    """

    authority_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AuthorityUri"),
        pydantic.Field(alias="AuthorityUri", description="URI of the authority"),
    ] = None
    """
    URI of the authority
    """

    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
