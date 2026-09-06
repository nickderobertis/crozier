

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorityAuthorisationDomainRequest(UniversalBaseModel):
    authorisation_domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AuthorisationDomainName"),
        pydantic.Field(alias="AuthorisationDomainName", description="The authorisation domain name"),
    ]
    """
    The authorisation domain name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
