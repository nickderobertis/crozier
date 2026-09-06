

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OasSupportSharedModelsTranslationKey(UniversalBaseModel):
    """
    A translation key to map the relationship of keyNames, usually for ODX, and string Ids
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The identifier for the translationKey. Read Only."),
    ] = None
    """
    The identifier for the translationKey. Read Only.
    """

    key_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="KeyName"),
        pydantic.Field(alias="KeyName", description="The key name of the item. One example is tkODX_HWIKM14R01"),
    ]
    """
    The key name of the item. One example is tkODX_HWIKM14R01
    """

    string_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StringID"),
        pydantic.Field(alias="StringID", description="Foreign key to StringDefinitionID"),
    ]
    """
    Foreign key to StringDefinitionID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
