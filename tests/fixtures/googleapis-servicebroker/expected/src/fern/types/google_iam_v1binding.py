

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .google_type_expr import GoogleTypeExpr


class GoogleIamV1Binding(UniversalBaseModel):
    """
    Associates `members` with a `role`.
    """

    condition: typing.Optional[GoogleTypeExpr] = pydantic.Field(default=None)
    """
    The condition that is associated with this binding.
    NOTE: An unsatisfied condition will not allow user access via current
    binding. Different bindings, including their conditions, are examined
    independently.
    """

    members: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Specifies the identities requesting access for a Cloud Platform resource.
    `members` can have the following values:
    
    * `allUsers`: A special identifier that represents anyone who is
       on the internet; with or without a Google account.
    
    * `allAuthenticatedUsers`: A special identifier that represents anyone
       who is authenticated with a Google account or a service account.
    
    * `user:{emailid}`: An email address that represents a specific Google
       account. For example, `alice@example.com` .
    
    
    * `serviceAccount:{emailid}`: An email address that represents a service
       account. For example, `my-other-app@appspot.gserviceaccount.com`.
    
    * `group:{emailid}`: An email address that represents a Google group.
       For example, `admins@example.com`.
    
    * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
       identifier) representing a user that has been recently deleted. For
       example, `alice@example.com?uid=123456789012345678901`. If the user is
       recovered, this value reverts to `user:{emailid}` and the recovered user
       retains the role in the binding.
    
    * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus
       unique identifier) representing a service account that has been recently
       deleted. For example,
       `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`.
       If the service account is undeleted, this value reverts to
       `serviceAccount:{emailid}` and the undeleted service account retains the
       role in the binding.
    
    * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique
       identifier) representing a Google group that has been recently
       deleted. For example, `admins@example.com?uid=123456789012345678901`. If
       the group is recovered, this value reverts to `group:{emailid}` and the
       recovered group retains the role in the binding.
    
    
    * `domain:{domain}`: The G Suite domain (primary) that represents all the    users of that domain. For example, `google.com` or `example.com`.
    """

    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    Role that is assigned to `members`.
    For example, `roles/viewer`, `roles/editor`, or `roles/owner`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
