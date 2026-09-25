

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomProfileField(UniversalBaseModel):
    """
    Dictionary containing the details of a custom profile field configured
    for this organization.
    """

    id: int = pydantic.Field()
    """
    The ID of the custom profile field. This will be referenced in the custom
    profile fields section of user objects.
    """

    type: int = pydantic.Field()
    """
    An integer indicating the type of the custom profile field, which determines
    how it is configured and displayed to users.
    
    See the [Custom profile fields](/help/custom-profile-fields#profile-field-types)
    article for details on what each type means.
    
    - **1**: Short text
    - **2**: Paragraph
    - **3**: Dropdown
    - **4**: Date
    - **5**: Link
    - **6**: Users
    - **7**: External account
    - **8**: Pronouns
    
    **Changes**: Field type `8` added in Zulip 6.0 (feature level 151).
    """

    order: int = pydantic.Field()
    """
    Custom profile fields are displayed in both settings UI and
    UI showing users' profiles in increasing `order`.
    """

    name: str = pydantic.Field()
    """
    The name of the custom profile field.
    """

    hint: str = pydantic.Field()
    """
    The help text to be displayed for the custom profile field in user-facing
    settings UI for configuring custom profile fields.
    """

    field_data: typing.Optional[str] = pydantic.Field(default=None)
    """
    Field types 3 (Dropdown) and 7 (External account) support storing
    additional configuration for the field type in the `field_data` attribute.
    
    For field type 3 (Dropdown), this attribute is a JSON object
    defining the choices and the order they will be displayed in the
    dropdown UI for individual users to select an option.
    
    The interface for field type 7 is not yet stabilized.
    """

    display_in_profile_summary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the custom profile field, display or not on the user card.
    
    Must be false for `Users`
    [profile field types](/help/custom-profile-fields#profile-field-types).
    
    This field is only included when its value is `true`.
    
    **Changes**: Before Zulip 12.0 (feature level 476), the
    "Paragraph" field type was not supported.
    
    New in Zulip 6.0 (feature level 146).
    """

    required: bool = pydantic.Field()
    """
    Whether an organization administrator has configured this profile field as
    required.
    
    Because the required property is mutable, clients cannot assume that a required
    custom profile field has a value. The Zulip web application displays a prominent
    banner to any user who has not set a value for a required field.
    
    **Changes**: New in Zulip 9.0 (feature level 244).
    """

    editable_by_user: bool = pydantic.Field()
    """
    Whether regular users can edit this profile field on their own account.
    
    Note that organization administrators can edit custom profile fields for any user
    regardless of this setting.
    
    **Changes**: New in Zulip 10.0 (feature level 296).
    """

    use_for_user_matching: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this custom profile field should be used to match users in typeahead
    suggestions. Only allowed for Short Text and External Account
    [profile field types](/help/custom-profile-fields#profile-field-types).
    
    This field is only included when its value is `true`.
    
    **Changes**: New in Zulip 12.0 (feature level 455).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
