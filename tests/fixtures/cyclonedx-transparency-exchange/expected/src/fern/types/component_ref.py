

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .uuid_ import Uuid


class ComponentRef(UniversalBaseModel):
    """
    A reference to a TEA component or specific component release
    """

    uuid_: typing_extensions.Annotated[
        Uuid,
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="A unique identifier for the TEA component"),
    ]
    """
    A unique identifier for the TEA component
    """

    release: typing.Optional[Uuid] = pydantic.Field(default=None)
    """
    Optional UUID of a specific release included in the product in the case where the product
    always include a specific release of a component. The product name should include a version
    identifier in this case.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
