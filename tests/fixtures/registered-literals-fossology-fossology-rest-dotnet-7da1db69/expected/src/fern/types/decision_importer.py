

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DecisionImporter(UniversalBaseModel):
    """
    Information required by Decision Importer agent
    """

    importer_user: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="importerUser"),
        pydantic.Field(
            alias="importerUser", description="User ID on which to tag imported decisions. Use '0' for self."
        ),
    ]
    """
    User ID on which to tag imported decisions. Use '0' for self.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
