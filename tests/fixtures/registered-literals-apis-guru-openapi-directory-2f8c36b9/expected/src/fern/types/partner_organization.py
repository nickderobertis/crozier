

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PartnerOrganization(UniversalBaseModel):
    """
    A partner organization
    """

    logo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoURL"),
        pydantic.Field(alias="logoURL", description="URL to a logo of the organization"),
    ] = None
    """
    URL to a logo of the organization
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the organization
    """

    namespace: typing.Optional[str] = pydantic.Field(default=None)
    """
    The namespace of the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
