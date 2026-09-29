

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .country import Country
from .organization_pid import OrganizationPid


class ApiOrganization(UniversalBaseModel):
    legal_short_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="legalShortName"), pydantic.Field(alias="legalShortName")
    ] = None
    legal_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="legalName"), pydantic.Field(alias="legalName")
    ] = None
    website_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteUrl"), pydantic.Field(alias="websiteUrl")
    ] = None
    alternative_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="alternativeNames"),
        pydantic.Field(alias="alternativeNames"),
    ] = None
    country: typing.Optional[Country] = None
    id: typing.Optional[str] = None
    pids: typing.Optional[typing.List[OrganizationPid]] = None
    original_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="originalIds"), pydantic.Field(alias="originalIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
