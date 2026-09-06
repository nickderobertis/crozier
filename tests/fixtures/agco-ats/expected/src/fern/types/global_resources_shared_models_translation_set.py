

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_resources_shared_models_translation_set_attribute import GlobalResourcesSharedModelsTranslationSetAttribute
from .global_resources_shared_models_translation_set_state import GlobalResourcesSharedModelsTranslationSetState


class GlobalResourcesSharedModelsTranslationSet(UniversalBaseModel):
    """
    A set of strings submitted for translation
    """

    attributes: typing_extensions.Annotated[
        typing.Optional[typing.List[GlobalResourcesSharedModelsTranslationSetAttribute]],
        FieldMetadata(alias="Attributes"),
        pydantic.Field(alias="Attributes", description="Attributes of the Translation Set"),
    ] = None
    """
    Attributes of the Translation Set
    """

    file_i_ds: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="FileIDs"),
        pydantic.Field(
            alias="FileIDs",
            description="IDs for files related to this translation set. For example, the original and processed files",
        ),
    ]
    """
    IDs for files related to this translation set. For example, the original and processed files
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The id of the TranslationSet."),
    ] = None
    """
    The id of the TranslationSet.
    """

    in_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="InDate"),
        pydantic.Field(alias="InDate", description="Read Only. The date the translation set was returned."),
    ] = None
    """
    Read Only. The date the translation set was returned.
    """

    notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Notes on the TranslationSet"),
    ] = None
    """
    Notes on the TranslationSet
    """

    out_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="OutDate"),
        pydantic.Field(alias="OutDate", description="Read Only. The date the translation set was sent out."),
    ] = None
    """
    Read Only. The date the translation set was sent out.
    """

    state: typing_extensions.Annotated[
        GlobalResourcesSharedModelsTranslationSetState,
        FieldMetadata(alias="State"),
        pydantic.Field(alias="State", description="An enum indicating the state of the translation set"),
    ]
    """
    An enum indicating the state of the translation set
    """

    translation_request_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TranslationRequestID"),
        pydantic.Field(
            alias="TranslationRequestID",
            description="Read Only. The Id of the TranslationRequest which generated this translation set.",
        ),
    ] = None
    """
    Read Only. The Id of the TranslationRequest which generated this translation set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
