

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Site(UniversalBaseModel):
    """
    Represents a Square Online site, which is an online store for a Square seller.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the site was created, in RFC 3339 format.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain of the site (without the protocol). For example, `mysite1.square.site`.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the site.
    """

    is_published: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the site is published.
    """

    site_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the site.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the site was last updated, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
