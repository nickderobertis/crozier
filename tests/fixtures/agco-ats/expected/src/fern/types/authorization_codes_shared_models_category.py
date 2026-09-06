

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorizationCodesSharedModelsCategory(UniversalBaseModel):
    """
    A category for Authorization Code Definitions
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="A description of the Category."),
    ] = None
    """
    A description of the Category.
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The ID of the Category."),
    ] = None
    """
    The ID of the Category.
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The Name of the Category."),
    ] = None
    """
    The Name of the Category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
