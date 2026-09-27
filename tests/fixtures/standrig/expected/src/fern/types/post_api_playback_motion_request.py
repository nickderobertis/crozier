

import typing

from .post_api_playback_motion_request_clip import PostApiPlaybackMotionRequestClip
from .post_api_playback_motion_request_loop import PostApiPlaybackMotionRequestLoop
from .post_api_playback_motion_request_one import PostApiPlaybackMotionRequestOne
from .post_api_playback_motion_request_time import PostApiPlaybackMotionRequestTime

PostApiPlaybackMotionRequest = typing.Union[
    PostApiPlaybackMotionRequestClip,
    PostApiPlaybackMotionRequestOne,
    PostApiPlaybackMotionRequestTime,
    PostApiPlaybackMotionRequestLoop,
]
