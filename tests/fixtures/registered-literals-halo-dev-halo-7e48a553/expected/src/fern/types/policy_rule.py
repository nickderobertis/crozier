

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PolicyRule(UniversalBaseModel):
    """
    PolicyRule holds information that describes a policy rule, but does not contain information about whom the rule
     applies to or which namespace the rule applies to.
    """

    api_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="apiGroups"),
        pydantic.Field(
            alias="apiGroups",
            description="APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any\n action requested against one of the enumerated resources in any API group will be allowed.",
        ),
    ] = None
    """
    APIGroups is the name of the APIGroup that contains the resources. If multiple API groups are specified, any
     action requested against one of the enumerated resources in any API group will be allowed.
    """

    non_resource_ur_ls: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="nonResourceURLs"),
        pydantic.Field(
            alias="nonResourceURLs",
            description='NonResourceURLs is a set of partial urls that a user should have access to. *s are allowed, but only as the\n full, final step in the path If an action is not a resource API request, then the URL is split on \'/\' and is\n checked against the NonResourceURLs to look for a match. Since non-resource URLs are not namespaced, this\n field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API\n resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both.',
        ),
    ] = None
    """
    NonResourceURLs is a set of partial urls that a user should have access to. *s are allowed, but only as the
     full, final step in the path If an action is not a resource API request, then the URL is split on '/' and is
     checked against the NonResourceURLs to look for a match. Since non-resource URLs are not namespaced, this
     field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API
     resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"), but not both.
    """

    resource_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="resourceNames"),
        pydantic.Field(
            alias="resourceNames",
            description="ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything\n is allowed.",
        ),
    ] = None
    """
    ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything
     is allowed.
    """

    resources: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Resources is a list of resources this rule applies to. '*' represents all resources in the specified
     apiGroups. '*&#47;foo' represents the subresource 'foo' for all resources in the specified apiGroups.
    """

    verbs: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Verbs allowed by this rule, such as get, list, create, update, patch, or delete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
