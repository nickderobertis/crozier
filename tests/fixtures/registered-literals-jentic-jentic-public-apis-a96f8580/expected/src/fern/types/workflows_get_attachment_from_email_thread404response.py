

import typing

from .attachment_not_found import AttachmentNotFound
from .email_not_found import EmailNotFound
from .workflow_not_found import WorkflowNotFound

WorkflowsGetAttachmentFromEmailThread404Response = typing.Union[WorkflowNotFound, EmailNotFound, AttachmentNotFound]
