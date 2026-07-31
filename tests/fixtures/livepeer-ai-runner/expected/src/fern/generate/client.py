

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.audio_response import AudioResponse
from ..types.image_response import ImageResponse
from ..types.image_to_text_response import ImageToTextResponse
from ..types.live_video_to_video_response import LiveVideoToVideoResponse
from ..types.llm_message import LlmMessage
from ..types.llm_response import LlmResponse
from ..types.masks_response import MasksResponse
from ..types.text_response import TextResponse
from ..types.video_response import VideoResponse
from .raw_client import AsyncRawGenerateClient, RawGenerateClient


OMIT = typing.cast(typing.Any, ...)


class GenerateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGenerateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGenerateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGenerateClient
        """
        return self._raw_client

    def gen_text_to_image(
        self,
        *,
        prompt: str,
        model_id: typing.Optional[str] = OMIT,
        loras: typing.Optional[str] = OMIT,
        height: typing.Optional[int] = OMIT,
        width: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        num_images_per_prompt: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageResponse:
        """
        Generate images from text prompts.

        Parameters
        ----------
        prompt : str
            Text prompt(s) to guide image generation. Separate multiple prompts with '|' if supported by the model.

        model_id : typing.Optional[str]
            Hugging Face model ID used for image generation.

        loras : typing.Optional[str]
            A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}.

        height : typing.Optional[int]
            The height in pixels of the generated image.

        width : typing.Optional[int]
            The width in pixels of the generated image.

        guidance_scale : typing.Optional[float]
            Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).

        negative_prompt : typing.Optional[str]
            Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        num_images_per_prompt : typing.Optional[int]
            Number of images to generate per prompt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_text_to_image(
            prompt="prompt",
        )
        """
        _response = self._raw_client.gen_text_to_image(
            prompt=prompt,
            model_id=model_id,
            loras=loras,
            height=height,
            width=width,
            guidance_scale=guidance_scale,
            negative_prompt=negative_prompt,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=num_images_per_prompt,
            request_options=request_options,
        )
        return _response.data

    def gen_image_to_image(
        self,
        *,
        prompt: str,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        loras: typing.Optional[str] = OMIT,
        strength: typing.Optional[float] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        image_guidance_scale: typing.Optional[float] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        num_images_per_prompt: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageResponse:
        """
        Apply image transformations to a provided image.

        Parameters
        ----------
        prompt : str
            Text prompt(s) to guide image generation.

        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for image generation.

        loras : typing.Optional[str]
            A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}.

        strength : typing.Optional[float]
            Degree of transformation applied to the reference image (0 to 1).

        guidance_scale : typing.Optional[float]
            Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).

        image_guidance_scale : typing.Optional[float]
            Degree to which the generated image is pushed towards the initial image.

        negative_prompt : typing.Optional[str]
            Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        num_images_per_prompt : typing.Optional[int]
            Number of images to generate per prompt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_image_to_image(
            prompt="prompt",
        )
        """
        _response = self._raw_client.gen_image_to_image(
            prompt=prompt,
            image=image,
            model_id=model_id,
            loras=loras,
            strength=strength,
            guidance_scale=guidance_scale,
            image_guidance_scale=image_guidance_scale,
            negative_prompt=negative_prompt,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=num_images_per_prompt,
            request_options=request_options,
        )
        return _response.data

    def gen_image_to_video(
        self,
        *,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        height: typing.Optional[int] = OMIT,
        width: typing.Optional[int] = OMIT,
        fps: typing.Optional[int] = OMIT,
        motion_bucket_id: typing.Optional[int] = OMIT,
        noise_aug_strength: typing.Optional[float] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VideoResponse:
        """
        Generate a video from a provided image.

        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for video generation.

        height : typing.Optional[int]
            The height in pixels of the generated video.

        width : typing.Optional[int]
            The width in pixels of the generated video.

        fps : typing.Optional[int]
            The frames per second of the generated video.

        motion_bucket_id : typing.Optional[int]
            Used for conditioning the amount of motion for the generation. The higher the number the more motion will be in the video.

        noise_aug_strength : typing.Optional[float]
            Amount of noise added to the conditioning image. Higher values reduce resemblance to the conditioning image and increase motion.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VideoResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_image_to_video()
        """
        _response = self._raw_client.gen_image_to_video(
            image=image,
            model_id=model_id,
            height=height,
            width=width,
            fps=fps,
            motion_bucket_id=motion_bucket_id,
            noise_aug_strength=noise_aug_strength,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            request_options=request_options,
        )
        return _response.data

    def gen_upscale(
        self,
        *,
        prompt: str,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageResponse:
        """
        Upscale an image by increasing its resolution.

        Parameters
        ----------
        prompt : str
            Text prompt(s) to guide upscaled image generation.

        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for upscaled image generation.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_upscale(
            prompt="prompt",
        )
        """
        _response = self._raw_client.gen_upscale(
            prompt=prompt,
            image=image,
            model_id=model_id,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            request_options=request_options,
        )
        return _response.data

    def gen_audio_to_text(
        self,
        *,
        audio: core.File,
        model_id: typing.Optional[str] = OMIT,
        return_timestamps: typing.Optional[str] = OMIT,
        metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TextResponse:
        """
        Transcribe audio files to text.

        Parameters
        ----------
        audio : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for transcription.

        return_timestamps : typing.Optional[str]
            Return timestamps for the transcribed text. Supported values: 'sentence', 'word', or a string boolean ('true' or 'false'). Default is 'true' ('sentence'). 'false' means no timestamps. 'word' means word-based timestamps.

        metadata : typing.Optional[str]
            Additional job information to be passed to the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_audio_to_text()
        """
        _response = self._raw_client.gen_audio_to_text(
            audio=audio,
            model_id=model_id,
            return_timestamps=return_timestamps,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def gen_segment_anything2(
        self,
        *,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        point_coords: typing.Optional[str] = OMIT,
        point_labels: typing.Optional[str] = OMIT,
        box: typing.Optional[str] = OMIT,
        mask_input: typing.Optional[str] = OMIT,
        multimask_output: typing.Optional[bool] = OMIT,
        return_logits: typing.Optional[bool] = OMIT,
        normalize_coords: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MasksResponse:
        """
        Segment objects in an image.

        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for image generation.

        point_coords : typing.Optional[str]
            Nx2 array of point prompts to the model, where each point is in (X,Y) in pixels.

        point_labels : typing.Optional[str]
            Labels for the point prompts, where 1 indicates a foreground point and 0 indicates a background point.

        box : typing.Optional[str]
            A length 4 array given as a box prompt to the model, in XYXY format.

        mask_input : typing.Optional[str]
            A low-resolution mask input to the model, typically from a previous prediction iteration, with the form 1xHxW (H=W=256 for SAM).

        multimask_output : typing.Optional[bool]
            If true, the model will return three masks for ambiguous input prompts, often producing better masks than a single prediction.

        return_logits : typing.Optional[bool]
            If true, returns un-thresholded mask logits instead of a binary mask.

        normalize_coords : typing.Optional[bool]
            If true, the point coordinates will be normalized to the range [0,1], with point_coords expected to be with respect to image dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MasksResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_segment_anything2()
        """
        _response = self._raw_client.gen_segment_anything2(
            image=image,
            model_id=model_id,
            point_coords=point_coords,
            point_labels=point_labels,
            box=box,
            mask_input=mask_input,
            multimask_output=multimask_output,
            return_logits=return_logits,
            normalize_coords=normalize_coords,
            request_options=request_options,
        )
        return _response.data

    def gen_llm(
        self,
        *,
        messages: typing.Sequence[LlmMessage],
        model: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LlmResponse:
        """
        Generate text using a language model.

        Parameters
        ----------
        messages : typing.Sequence[LlmMessage]

        model : typing.Optional[str]

        temperature : typing.Optional[float]

        max_tokens : typing.Optional[int]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LlmResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, LlmMessage

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_llm(
            messages=[
                LlmMessage(
                    role="role",
                    content="content",
                )
            ],
        )
        """
        _response = self._raw_client.gen_llm(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            top_k=top_k,
            stream=stream,
            request_options=request_options,
        )
        return _response.data

    def gen_image_to_text(
        self,
        *,
        image: core.File,
        prompt: typing.Optional[str] = OMIT,
        model_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageToTextResponse:
        """
        Transform image files to text.

        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        prompt : typing.Optional[str]
            Text prompt(s) to guide transformation.

        model_id : typing.Optional[str]
            Hugging Face model ID used for transformation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageToTextResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_image_to_text()
        """
        _response = self._raw_client.gen_image_to_text(
            image=image, prompt=prompt, model_id=model_id, request_options=request_options
        )
        return _response.data

    def gen_live_video_to_video(
        self,
        *,
        subscribe_url: str,
        publish_url: str,
        control_url: typing.Optional[str] = OMIT,
        events_url: typing.Optional[str] = OMIT,
        model_id: typing.Optional[str] = OMIT,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LiveVideoToVideoResponse:
        """
        Apply transformations to a live video streamed to the returned endpoints.

        Parameters
        ----------
        subscribe_url : str
            Source URL of the incoming stream to subscribe to.

        publish_url : str
            Destination URL of the outgoing stream to publish.

        control_url : typing.Optional[str]
            URL for subscribing via Trickle protocol for updates in the live video-to-video generation params.

        events_url : typing.Optional[str]
            URL for publishing events via Trickle protocol for pipeline status and logs.

        model_id : typing.Optional[str]
            Name of the pipeline to run in the live video to video job. Notice that this is named model_id for consistency with other routes, but it does not refer to a Hugging Face model ID. The exact model(s) depends on the pipeline implementation and might be configurable via the `params` argument.

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Initial parameters for the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveVideoToVideoResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_live_video_to_video(
            subscribe_url="subscribe_url",
            publish_url="publish_url",
        )
        """
        _response = self._raw_client.gen_live_video_to_video(
            subscribe_url=subscribe_url,
            publish_url=publish_url,
            control_url=control_url,
            events_url=events_url,
            model_id=model_id,
            params=params,
            request_options=request_options,
        )
        return _response.data

    def gen_text_to_speech(
        self,
        *,
        model_id: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudioResponse:
        """
        Generate a text-to-speech audio file based on the provided text input and speaker description.

        Parameters
        ----------
        model_id : typing.Optional[str]
            Hugging Face model ID used for text to speech generation.

        text : typing.Optional[str]
            Text input for speech generation.

        description : typing.Optional[str]
            Description of speaker to steer text to speech generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.generate.gen_text_to_speech()
        """
        _response = self._raw_client.gen_text_to_speech(
            model_id=model_id, text=text, description=description, request_options=request_options
        )
        return _response.data


class AsyncGenerateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGenerateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGenerateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGenerateClient
        """
        return self._raw_client

    async def gen_text_to_image(
        self,
        *,
        prompt: str,
        model_id: typing.Optional[str] = OMIT,
        loras: typing.Optional[str] = OMIT,
        height: typing.Optional[int] = OMIT,
        width: typing.Optional[int] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        num_images_per_prompt: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageResponse:
        """
        Generate images from text prompts.

        Parameters
        ----------
        prompt : str
            Text prompt(s) to guide image generation. Separate multiple prompts with '|' if supported by the model.

        model_id : typing.Optional[str]
            Hugging Face model ID used for image generation.

        loras : typing.Optional[str]
            A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}.

        height : typing.Optional[int]
            The height in pixels of the generated image.

        width : typing.Optional[int]
            The width in pixels of the generated image.

        guidance_scale : typing.Optional[float]
            Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).

        negative_prompt : typing.Optional[str]
            Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        num_images_per_prompt : typing.Optional[int]
            Number of images to generate per prompt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_text_to_image(
                prompt="prompt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_text_to_image(
            prompt=prompt,
            model_id=model_id,
            loras=loras,
            height=height,
            width=width,
            guidance_scale=guidance_scale,
            negative_prompt=negative_prompt,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=num_images_per_prompt,
            request_options=request_options,
        )
        return _response.data

    async def gen_image_to_image(
        self,
        *,
        prompt: str,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        loras: typing.Optional[str] = OMIT,
        strength: typing.Optional[float] = OMIT,
        guidance_scale: typing.Optional[float] = OMIT,
        image_guidance_scale: typing.Optional[float] = OMIT,
        negative_prompt: typing.Optional[str] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        num_images_per_prompt: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageResponse:
        """
        Apply image transformations to a provided image.

        Parameters
        ----------
        prompt : str
            Text prompt(s) to guide image generation.

        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for image generation.

        loras : typing.Optional[str]
            A LoRA (Low-Rank Adaptation) model and its corresponding weight for image generation. Example: { "latent-consistency/lcm-lora-sdxl": 1.0, "nerijs/pixel-art-xl": 1.2}.

        strength : typing.Optional[float]
            Degree of transformation applied to the reference image (0 to 1).

        guidance_scale : typing.Optional[float]
            Encourages model to generate images closely linked to the text prompt (higher values may reduce image quality).

        image_guidance_scale : typing.Optional[float]
            Degree to which the generated image is pushed towards the initial image.

        negative_prompt : typing.Optional[str]
            Text prompt(s) to guide what to exclude from image generation. Ignored if guidance_scale < 1.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        num_images_per_prompt : typing.Optional[int]
            Number of images to generate per prompt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_image_to_image(
                prompt="prompt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_image_to_image(
            prompt=prompt,
            image=image,
            model_id=model_id,
            loras=loras,
            strength=strength,
            guidance_scale=guidance_scale,
            image_guidance_scale=image_guidance_scale,
            negative_prompt=negative_prompt,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=num_images_per_prompt,
            request_options=request_options,
        )
        return _response.data

    async def gen_image_to_video(
        self,
        *,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        height: typing.Optional[int] = OMIT,
        width: typing.Optional[int] = OMIT,
        fps: typing.Optional[int] = OMIT,
        motion_bucket_id: typing.Optional[int] = OMIT,
        noise_aug_strength: typing.Optional[float] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VideoResponse:
        """
        Generate a video from a provided image.

        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for video generation.

        height : typing.Optional[int]
            The height in pixels of the generated video.

        width : typing.Optional[int]
            The width in pixels of the generated video.

        fps : typing.Optional[int]
            The frames per second of the generated video.

        motion_bucket_id : typing.Optional[int]
            Used for conditioning the amount of motion for the generation. The higher the number the more motion will be in the video.

        noise_aug_strength : typing.Optional[float]
            Amount of noise added to the conditioning image. Higher values reduce resemblance to the conditioning image and increase motion.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VideoResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_image_to_video()


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_image_to_video(
            image=image,
            model_id=model_id,
            height=height,
            width=width,
            fps=fps,
            motion_bucket_id=motion_bucket_id,
            noise_aug_strength=noise_aug_strength,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            request_options=request_options,
        )
        return _response.data

    async def gen_upscale(
        self,
        *,
        prompt: str,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        safety_check: typing.Optional[bool] = OMIT,
        seed: typing.Optional[int] = OMIT,
        num_inference_steps: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageResponse:
        """
        Upscale an image by increasing its resolution.

        Parameters
        ----------
        prompt : str
            Text prompt(s) to guide upscaled image generation.

        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for upscaled image generation.

        safety_check : typing.Optional[bool]
            Perform a safety check to estimate if generated images could be offensive or harmful.

        seed : typing.Optional[int]
            Seed for random number generation.

        num_inference_steps : typing.Optional[int]
            Number of denoising steps. More steps usually lead to higher quality images but slower inference. Modulated by strength.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_upscale(
                prompt="prompt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_upscale(
            prompt=prompt,
            image=image,
            model_id=model_id,
            safety_check=safety_check,
            seed=seed,
            num_inference_steps=num_inference_steps,
            request_options=request_options,
        )
        return _response.data

    async def gen_audio_to_text(
        self,
        *,
        audio: core.File,
        model_id: typing.Optional[str] = OMIT,
        return_timestamps: typing.Optional[str] = OMIT,
        metadata: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TextResponse:
        """
        Transcribe audio files to text.

        Parameters
        ----------
        audio : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for transcription.

        return_timestamps : typing.Optional[str]
            Return timestamps for the transcribed text. Supported values: 'sentence', 'word', or a string boolean ('true' or 'false'). Default is 'true' ('sentence'). 'false' means no timestamps. 'word' means word-based timestamps.

        metadata : typing.Optional[str]
            Additional job information to be passed to the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TextResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_audio_to_text()


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_audio_to_text(
            audio=audio,
            model_id=model_id,
            return_timestamps=return_timestamps,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def gen_segment_anything2(
        self,
        *,
        image: core.File,
        model_id: typing.Optional[str] = OMIT,
        point_coords: typing.Optional[str] = OMIT,
        point_labels: typing.Optional[str] = OMIT,
        box: typing.Optional[str] = OMIT,
        mask_input: typing.Optional[str] = OMIT,
        multimask_output: typing.Optional[bool] = OMIT,
        return_logits: typing.Optional[bool] = OMIT,
        normalize_coords: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MasksResponse:
        """
        Segment objects in an image.

        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        model_id : typing.Optional[str]
            Hugging Face model ID used for image generation.

        point_coords : typing.Optional[str]
            Nx2 array of point prompts to the model, where each point is in (X,Y) in pixels.

        point_labels : typing.Optional[str]
            Labels for the point prompts, where 1 indicates a foreground point and 0 indicates a background point.

        box : typing.Optional[str]
            A length 4 array given as a box prompt to the model, in XYXY format.

        mask_input : typing.Optional[str]
            A low-resolution mask input to the model, typically from a previous prediction iteration, with the form 1xHxW (H=W=256 for SAM).

        multimask_output : typing.Optional[bool]
            If true, the model will return three masks for ambiguous input prompts, often producing better masks than a single prediction.

        return_logits : typing.Optional[bool]
            If true, returns un-thresholded mask logits instead of a binary mask.

        normalize_coords : typing.Optional[bool]
            If true, the point coordinates will be normalized to the range [0,1], with point_coords expected to be with respect to image dimensions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MasksResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_segment_anything2()


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_segment_anything2(
            image=image,
            model_id=model_id,
            point_coords=point_coords,
            point_labels=point_labels,
            box=box,
            mask_input=mask_input,
            multimask_output=multimask_output,
            return_logits=return_logits,
            normalize_coords=normalize_coords,
            request_options=request_options,
        )
        return _response.data

    async def gen_llm(
        self,
        *,
        messages: typing.Sequence[LlmMessage],
        model: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        max_tokens: typing.Optional[int] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LlmResponse:
        """
        Generate text using a language model.

        Parameters
        ----------
        messages : typing.Sequence[LlmMessage]

        model : typing.Optional[str]

        temperature : typing.Optional[float]

        max_tokens : typing.Optional[int]

        top_p : typing.Optional[float]

        top_k : typing.Optional[int]

        stream : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LlmResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LlmMessage

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_llm(
                messages=[
                    LlmMessage(
                        role="role",
                        content="content",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_llm(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            top_k=top_k,
            stream=stream,
            request_options=request_options,
        )
        return _response.data

    async def gen_image_to_text(
        self,
        *,
        image: core.File,
        prompt: typing.Optional[str] = OMIT,
        model_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageToTextResponse:
        """
        Transform image files to text.

        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        prompt : typing.Optional[str]
            Text prompt(s) to guide transformation.

        model_id : typing.Optional[str]
            Hugging Face model ID used for transformation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageToTextResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_image_to_text()


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_image_to_text(
            image=image, prompt=prompt, model_id=model_id, request_options=request_options
        )
        return _response.data

    async def gen_live_video_to_video(
        self,
        *,
        subscribe_url: str,
        publish_url: str,
        control_url: typing.Optional[str] = OMIT,
        events_url: typing.Optional[str] = OMIT,
        model_id: typing.Optional[str] = OMIT,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LiveVideoToVideoResponse:
        """
        Apply transformations to a live video streamed to the returned endpoints.

        Parameters
        ----------
        subscribe_url : str
            Source URL of the incoming stream to subscribe to.

        publish_url : str
            Destination URL of the outgoing stream to publish.

        control_url : typing.Optional[str]
            URL for subscribing via Trickle protocol for updates in the live video-to-video generation params.

        events_url : typing.Optional[str]
            URL for publishing events via Trickle protocol for pipeline status and logs.

        model_id : typing.Optional[str]
            Name of the pipeline to run in the live video to video job. Notice that this is named model_id for consistency with other routes, but it does not refer to a Hugging Face model ID. The exact model(s) depends on the pipeline implementation and might be configurable via the `params` argument.

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Initial parameters for the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveVideoToVideoResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_live_video_to_video(
                subscribe_url="subscribe_url",
                publish_url="publish_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_live_video_to_video(
            subscribe_url=subscribe_url,
            publish_url=publish_url,
            control_url=control_url,
            events_url=events_url,
            model_id=model_id,
            params=params,
            request_options=request_options,
        )
        return _response.data

    async def gen_text_to_speech(
        self,
        *,
        model_id: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudioResponse:
        """
        Generate a text-to-speech audio file based on the provided text input and speaker description.

        Parameters
        ----------
        model_id : typing.Optional[str]
            Hugging Face model ID used for text to speech generation.

        text : typing.Optional[str]
            Text input for speech generation.

        description : typing.Optional[str]
            Description of speaker to steer text to speech generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.generate.gen_text_to_speech()


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_text_to_speech(
            model_id=model_id, text=text, description=description, request_options=request_options
        )
        return _response.data
