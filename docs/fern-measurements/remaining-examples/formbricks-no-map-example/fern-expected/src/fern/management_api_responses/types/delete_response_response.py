

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .delete_response_response_data_value import DeleteResponseResponseDataValue
from .delete_response_response_meta import DeleteResponseResponseMeta
from .delete_response_response_variables_value import DeleteResponseResponseVariablesValue


class DeleteResponseResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the response
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the response was created"),
    ] = None
    """
    The date and time the response was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the response was last updated"),
    ] = None
    """
    The date and time the response was last updated
    """

    finished: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the response is finished
    """

    survey_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="surveyId"),
        pydantic.Field(alias="surveyId", description="The ID of the survey"),
    ] = None
    """
    The ID of the survey
    """

    contact_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactId"),
        pydantic.Field(alias="contactId", description="The ID of the contact"),
    ] = None
    """
    The ID of the contact
    """

    ending_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endingId"),
        pydantic.Field(alias="endingId", description="The ID of the ending"),
    ] = None
    """
    The ID of the ending
    """

    data: typing.Optional[typing.Dict[str, DeleteResponseResponseDataValue]] = pydantic.Field(default=None)
    """
    The data of the response
    """

    variables: typing.Optional[typing.Dict[str, DeleteResponseResponseVariablesValue]] = pydantic.Field(default=None)
    """
    The variables of the response
    """

    ttc: typing.Optional[typing.Dict[str, float]] = pydantic.Field(default=None)
    """
    The TTC of the response
    """

    meta: typing.Optional[DeleteResponseResponseMeta] = pydantic.Field(default=None)
    """
    The meta data of the response
    """

    contact_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[str]]],
        FieldMetadata(alias="contactAttributes"),
        pydantic.Field(alias="contactAttributes", description="The attributes of the contact"),
    ] = None
    """
    The attributes of the contact
    """

    single_use_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="singleUseId"),
        pydantic.Field(alias="singleUseId", description="The single use ID of the response"),
    ] = None
    """
    The single use ID of the response
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language of the response
    """

    display_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayId"),
        pydantic.Field(alias="displayId", description="The display ID of the response"),
    ] = None
    """
    The display ID of the response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
