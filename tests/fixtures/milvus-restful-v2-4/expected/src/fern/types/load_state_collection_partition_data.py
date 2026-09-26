

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LoadStateCollectionPartitionData(UniversalBaseModel):
    load_state: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="loadState"),
        pydantic.Field(
            alias="loadState",
            description="An object that indicates the load status of the specified collection.\nThe possible states are as follows:\n- **Loaded**\n  -  Indicates that the specified collection is loaded.\n- **Loading**\n  -  Indicates that the specified collection is being loaded.\n- **NotExist**\n  -  Indicates that the specified collection does not exist. \n  -  Including a non-existing partition in **partition_names** results in a **MilvusException**.\n- **NotLoad**\n  -  Indicates that the specified collection is not loaded.",
        ),
    ]
    """
    An object that indicates the load status of the specified collection.
    The possible states are as follows:
    - **Loaded**
      -  Indicates that the specified collection is loaded.
    - **Loading**
      -  Indicates that the specified collection is being loaded.
    - **NotExist**
      -  Indicates that the specified collection does not exist. 
      -  Including a non-existing partition in **partition_names** results in a **MilvusException**.
    - **NotLoad**
      -  Indicates that the specified collection is not loaded.
    """

    load_progress: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="loadProgress"),
        pydantic.Field(
            alias="loadProgress",
            description="An integer that indicates the load progress in the percentage of the specified collection.",
        ),
    ]
    """
    An integer that indicates the load progress in the percentage of the specified collection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
