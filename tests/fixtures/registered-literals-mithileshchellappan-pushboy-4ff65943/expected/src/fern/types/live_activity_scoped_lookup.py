

import typing

from .live_activity_topic_scope import LiveActivityTopicScope
from .live_activity_user_scope import LiveActivityUserScope

LiveActivityScopedLookup = typing.Union[LiveActivityUserScope, LiveActivityTopicScope]
