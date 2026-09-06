

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostLinksPermissionsDomainIdLinkIdUserIdResponse(UniversalBaseModel):
    id: str
    domain_id: typing_extensions.Annotated[int, FieldMetadata(alias="DomainId"), pydantic.Field(alias="DomainId")]
    user_id: typing_extensions.Annotated[int, FieldMetadata(alias="UserId"), pydantic.Field(alias="UserId")]
    link_id_string: typing_extensions.Annotated[
        str, FieldMetadata(alias="LinkIdString"), pydantic.Field(alias="LinkIdString", description="Link ID")
    ]
    """
    Link ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
