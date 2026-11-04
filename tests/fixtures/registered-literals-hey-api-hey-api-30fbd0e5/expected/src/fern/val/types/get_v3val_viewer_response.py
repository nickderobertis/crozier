

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_v3val_viewer_response_links import GetV3ValViewerResponseLinks
from .get_v3val_viewer_response_type import GetV3ValViewerResponseType


class GetV3ValViewerResponse(UniversalBaseModel):
    """
    Public identity of the viewer derived from a verified X-Val-Town-User header. Only safe, public profile fields are returned — no email or tier.
    """

    id: str = pydantic.Field()
    """
    The viewer's user id
    """

    type: typing.Optional[GetV3ValViewerResponseType] = pydantic.Field(default=None)
    """
    Whether the viewer is a user or an organization
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The viewer's handle, without the @ symbol
    """

    bio: typing.Optional[str] = pydantic.Field(default=None)
    """
    The viewer's bio, if any
    """

    profile_image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="profileImageUrl"),
        pydantic.Field(alias="profileImageUrl", description="URL to the viewer's profile image, if any"),
    ] = None
    """
    URL to the viewer's profile image, if any
    """

    url: str = pydantic.Field()
    """
    The viewer's profile URL on val.town
    """

    links: GetV3ValViewerResponseLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
