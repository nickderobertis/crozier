

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreprintProviderListResponseAttributes(UniversalBaseModel):
    """
    The properties of the preprint provider entity.
    """

    advisory_board: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTML representation of the preprint provider's advisory board.
    """

    banner_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    A static path to the preprint provider's banner image. This field is deprecated as of verson 2.4.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the preprint provider.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preprint provider's domain, if the provider is using a domain to for their preprint service.
    """

    domain_redirect_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not redirects are enabled for the provider's domain.
    """

    email_contact: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preprint provider's contact email address. This field is deprecated as of verson 2.4.
    """

    email_support: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preprint providers's support email address.
    """

    example: typing.Optional[str] = pydantic.Field(default=None)
    """
    The GUID for an example preprint from this preprint provider.
    """

    logo_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    A static path to the preprint provider's logo image. This field is deprecated as of verson 2.4.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the preprint provider.
    """

    social_facebook: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preprint provider's Facebook account ID. This field is deprecated as of verson 2.4.
    """

    social_instagram: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preprint provider's Instagram account ID. This field is deprecated as of verson 2.4.
    """

    subjects_acceptable: typing.Optional[str] = pydantic.Field(default=None)
    """
    A nested array structure defining allowed subjects for this preprint provider, in the BePress taxonomy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
