

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiKeyPresentation(UniversalBaseModel):
    active: bool = pydantic.Field()
    """
    Whether this API key is active
    """

    created_at: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The UTC unix timestamp of when this api key has been created"),
    ]
    """
    The UTC unix timestamp of when this api key has been created
    """

    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    key: str = pydantic.Field()
    """
    The api key identifier
    """

    label: str = pydantic.Field()
    """
    The label / name of the api key
    """

    organization_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The organization namespace this api key belongs to"),
    ]
    """
    The organization namespace this api key belongs to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
