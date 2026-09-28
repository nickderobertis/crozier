

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ivcs_installed_app_type import IvcsInstalledAppType


class IvcsInstalledApp(UniversalBaseModel):
    admin_permissions: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="adminPermissions"),
        pydantic.Field(
            alias="adminPermissions",
            description="VCS App installed with repository or organization level admin permissions",
        ),
    ]
    """
    VCS App installed with repository or organization level admin permissions
    """

    customer_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="customerName"), pydantic.Field(alias="customerName", description="Customer Prisma ID")
    ]
    """
    Customer Prisma ID
    """

    events: typing.List[str] = pydantic.Field()
    """
    VCS webhook events the App listens on
    """

    html_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="htmlUrl"), pydantic.Field(alias="htmlUrl", description="VCS App settings URL")
    ]
    """
    VCS App settings URL
    """

    id: str = pydantic.Field()
    """
    VCS App ID
    """

    name: str = pydantic.Field()
    """
    VCS App name
    """

    node_created_timestamp: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="nodeCreatedTimestamp"),
        pydantic.Field(alias="nodeCreatedTimestamp"),
    ] = None
    read_permissions: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="readPermissions"),
        pydantic.Field(alias="readPermissions", description="VCS App read permissions"),
    ]
    """
    VCS App read permissions
    """

    repository_selection: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="repositorySelection"),
        pydantic.Field(
            alias="repositorySelection",
            description="repositorySelection:\n  - `all`: VCS App installed on organization level\n  - `selected`: VCS App installed on selected repositories",
        ),
    ]
    """
    repositorySelection:
      - `all`: VCS App installed on organization level
      - `selected`: VCS App installed on selected repositories
    """

    timestamp: float
    type: IvcsInstalledAppType
    vendor_created_timestamp: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="vendorCreatedTimestamp"),
        pydantic.Field(alias="vendorCreatedTimestamp", description="Webhook creation date"),
    ] = None
    """
    Webhook creation date
    """

    write_permissions: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="writePermissions"),
        pydantic.Field(alias="writePermissions", description="VCS App write permissions"),
    ]
    """
    VCS App write permissions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
