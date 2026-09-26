

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IndexConfig(UniversalBaseModel):
    index_type: str = pydantic.Field()
    """
    The type of the index to create
    """

    m: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="M"),
        pydantic.Field(
            alias="M", description="The maximum degree of the node and applies only when index_type is set to __HNSW__."
        ),
    ] = None
    """
    The maximum degree of the node and applies only when index_type is set to __HNSW__.
    """

    ef_construction: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="efConstruction"),
        pydantic.Field(
            alias="efConstruction",
            description="The search scope. This applies only when **index_type** is set to **HNSW**",
        ),
    ] = None
    """
    The search scope. This applies only when **index_type** is set to **HNSW**
    """

    nlist: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of cluster units. This applies to IVF-related index types.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
