

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GlobalResourcesSharedModelsGlobalImageCategory(UniversalBaseModel):
    """
    An image category from the Global Image library.
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The Id of the GlobalImage Categories."),
    ] = None
    """
    The Id of the GlobalImage Categories.
    """

    name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the globalImage Catetory."),
    ]
    """
    The name of the globalImage Catetory.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
