

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LdapAuthModuleConfig(UniversalBaseModel):
    """
    Settings to authenticate users using a generic OAuth2 provider
    """

    admin_password: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="adminPassword"),
        pydantic.Field(alias="adminPassword", description="The admin password"),
    ]
    """
    The admin password
    """

    admin_username: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="adminUsername"),
        pydantic.Field(alias="adminUsername", description="The admin username"),
    ]
    """
    The admin username
    """

    desc: str = pydantic.Field()
    """
    Description of the config
    """

    email_field: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="emailField"),
        pydantic.Field(alias="emailField", description="Field name to get email from user profile"),
    ]
    """
    Field name to get email from user profile
    """

    group_filter: typing_extensions.Annotated[
        str, FieldMetadata(alias="groupFilter"), pydantic.Field(alias="groupFilter", description="Filter for groups")
    ]
    """
    Filter for groups
    """

    id: str = pydantic.Field()
    """
    Unique id of the config
    """

    name: str = pydantic.Field()
    """
    Name of the config
    """

    name_field: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nameField"),
        pydantic.Field(alias="nameField", description="Field name to get name from user profile"),
    ]
    """
    Field name to get name from user profile
    """

    otoroshi_data_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="otoroshiDataField"),
        pydantic.Field(
            alias="otoroshiDataField",
            description="Field name to get otoroshi metadata from. You can specify sub fields using | as separator",
        ),
    ] = None
    """
    Field name to get otoroshi metadata from. You can specify sub fields using | as separator
    """

    search_base: typing_extensions.Annotated[
        str, FieldMetadata(alias="searchBase"), pydantic.Field(alias="searchBase", description="LDAP search base")
    ]
    """
    LDAP search base
    """

    search_filter: typing_extensions.Annotated[
        str, FieldMetadata(alias="searchFilter"), pydantic.Field(alias="searchFilter", description="Filter for users")
    ]
    """
    Filter for users
    """

    server_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="serverUrl"), pydantic.Field(alias="serverUrl", description="URL of the ldap server")
    ]
    """
    URL of the ldap server
    """

    session_max_age: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="sessionMaxAge"),
        pydantic.Field(alias="sessionMaxAge", description="Max age of the session"),
    ]
    """
    Max age of the session
    """

    type: str = pydantic.Field()
    """
    Type of settings. value is ldap
    """

    user_base: typing_extensions.Annotated[
        str, FieldMetadata(alias="userBase"), pydantic.Field(alias="userBase", description="LDAP user base DN")
    ]
    """
    LDAP user base DN
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
