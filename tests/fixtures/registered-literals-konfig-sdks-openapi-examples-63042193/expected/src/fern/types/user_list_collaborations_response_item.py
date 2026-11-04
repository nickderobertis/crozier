

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserListCollaborationsResponseItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The UUID of the organization
    """

    vcs_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="vcs-type"), pydantic.Field(alias="vcs-type", description="The VCS provider")
    ]
    """
    The VCS provider
    """

    name: str = pydantic.Field()
    """
    The name of the organization
    """

    avatar_url: str = pydantic.Field()
    """
    URL to the user's avatar on the VCS
    """

    slug: str = pydantic.Field()
    """
    The slug of the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
