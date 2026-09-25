

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_list_uuid import ColumnListUuid
from .column_ratio import ColumnRatio
from .column_uuid import ColumnUuid
from .default_answer_string import DefaultAnswerString
from .has_default_answer import HasDefaultAnswer
from .is_hidden import IsHidden
from .is_required import IsRequired
from .name import Name


class InputPhoneNumberPayload(UniversalBaseModel):
    """
    Payload for INPUT_PHONE_NUMBER block type. Used for phone number input fields.
    """

    is_hidden: typing_extensions.Annotated[
        typing.Optional[IsHidden], FieldMetadata(alias="isHidden"), pydantic.Field(alias="isHidden")
    ] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[IsRequired], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    has_default_answer: typing_extensions.Annotated[
        typing.Optional[HasDefaultAnswer],
        FieldMetadata(alias="hasDefaultAnswer"),
        pydantic.Field(alias="hasDefaultAnswer"),
    ] = None
    default_answer: typing_extensions.Annotated[
        typing.Optional[DefaultAnswerString],
        FieldMetadata(alias="defaultAnswer"),
        pydantic.Field(alias="defaultAnswer"),
    ] = None
    placeholder: typing.Optional[str] = None
    international_format: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="internationalFormat"),
        pydantic.Field(
            alias="internationalFormat",
            description="When true, allows international phone numbers from any country. When false, restricts input to the default country.",
        ),
    ] = None
    """
    When true, allows international phone numbers from any country. When false, restricts input to the default country.
    """

    default_country_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="defaultCountryCode"),
        pydantic.Field(
            alias="defaultCountryCode",
            description="ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB', 'DE') that sets the default country for the phone number input.",
        ),
    ] = None
    """
    ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB', 'DE') that sets the default country for the phone number input.
    """

    column_list_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnListUuid], FieldMetadata(alias="columnListUuid"), pydantic.Field(alias="columnListUuid")
    ] = None
    column_uuid: typing_extensions.Annotated[
        typing.Optional[ColumnUuid], FieldMetadata(alias="columnUuid"), pydantic.Field(alias="columnUuid")
    ] = None
    column_ratio: typing_extensions.Annotated[
        typing.Optional[ColumnRatio], FieldMetadata(alias="columnRatio"), pydantic.Field(alias="columnRatio")
    ] = None
    name: typing.Optional[Name] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
