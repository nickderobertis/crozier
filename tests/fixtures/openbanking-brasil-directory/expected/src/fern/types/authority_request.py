

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorityRequest(UniversalBaseModel):
    authority_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorityCode"),
        pydantic.Field(alias="AuthorityCode", description="Code of the Authority i.e. GBFCA, etc"),
    ]
    """
    Code of the Authority i.e. GBFCA, etc
    """

    authority_country: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorityCountry"),
        pydantic.Field(alias="AuthorityCountry", description="Country of the authority"),
    ]
    """
    Country of the authority
    """

    authority_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorityName"),
        pydantic.Field(alias="AuthorityName", description="The ID of the Authority i.e GBFCA, etc"),
    ]
    """
    The ID of the Authority i.e GBFCA, etc
    """

    authority_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorityUri"),
        pydantic.Field(alias="AuthorityUri", description="URI of the authority"),
    ]
    """
    URI of the authority
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
