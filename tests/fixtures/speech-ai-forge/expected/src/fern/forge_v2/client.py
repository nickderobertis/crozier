

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.adjust_config import AdjustConfig
from ..types.encoder_config import EncoderConfig
from ..types.enhancer_config import EnhancerConfig
from ..types.infer_config import InferConfig
from ..types.input_audio import InputAudio
from ..types.speaker_config import SpeakerConfig
from ..types.stt_output_format import SttOutputFormat
from ..types.tn_config import TnConfig
from ..types.transcriptions_response import TranscriptionsResponse
from ..types.tts_config import TtsConfig
from ..types.vc_config import VcConfig
from .raw_client import AsyncRawForgeV2Client, RawForgeV2Client


OMIT = typing.cast(typing.Any, ...)


class ForgeV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawForgeV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawForgeV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawForgeV2Client
        """
        return self._raw_client

    def forge_text_synthesize(
        self,
        *,
        adjust: typing.Optional[AdjustConfig] = OMIT,
        encoder: typing.Optional[EncoderConfig] = OMIT,
        enhance: typing.Optional[EnhancerConfig] = OMIT,
        infer: typing.Optional[InferConfig] = OMIT,
        vc: typing.Optional[VcConfig] = OMIT,
        tn: typing.Optional[TnConfig] = OMIT,
        tts: typing.Optional[TtsConfig] = OMIT,
        spk: typing.Optional[SpeakerConfig] = OMIT,
        text: typing.Optional[str] = OMIT,
        texts: typing.Optional[typing.Sequence[str]] = OMIT,
        ssml: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        **Text-to-Speech Synthesis API (v2)**

        This endpoint converts text into speech, offering a wide range of customization options.
        It accepts JSON formatted data in the request body.

        **Core Functionality**:
        *   Synthesizes speech from various text inputs.
        *   Supports voice cloning by directly uploading a reference audio.

        **Input Flexibility**:
        *   Provide text via one of these mutually exclusive fields:
            *   `text`: A single string of text.
            *   `texts`: A list of strings for batch processing.
            *   `ssml`: Text formatted using Speech Synthesis Markup Language (SSML).

        **Speaker Customization (`spk`)**:
        *   Use pre-defined speakers via `spk.from_spk_id` or `spk.from_spk_name`.
        *   **Voice Cloning**: Provide reference audio for voice cloning:
            *   `spk.from_ref.wav_b64`: Base64 encoded WAV audio data.
            *   `spk.from_ref.text`: The transcript corresponding to the reference audio.

        **Audio Processing & Control**:
        *   **Adjustments (`adjust`)**:
            *   `pitch`: Modify audio pitch.
            *   `speed_rate`: Adjust speaking rate.
            *   `volume_gain_db`: Change audio volume.
            *   `normalize`: Apply volume normalization.
            *   `remove_silence`: Trim silence from audio ends.
        *   **Encoding (`encoder`)**:
            *   `format`: Output audio format (e.g., "mp3", "wav").
            *   `bitrate`: Audio bitrate (e.g., "64k").
            *   `acodec`: Audio codec (e.g., "libmp3lame").
        *   **Enhancement (`enhance`)**:
            *   `enabled`: Toggle audio enhancement.
            *   `model`: Select enhancement model.
            *   Additional parameters like `nfe`, `solver`, `lambd`, `tau` for fine-tuning.
        *   **Inference (`infer`)**:
            *   `batch_size`, `spliter_threshold`, `eos` for text processing.
            *   `seed`: For reproducible outputs.
            *   `stream`, `stream_chunk_size`: Enable and configure streaming output.
            *   `no_cache`, `sync_gen`: Control caching and generation mode.
        *   **Text Normalization (`tn`)**:
            *   `enabled`/`disabled`: Specify text normalization rules.
        *   **TTS Model Parameters (`tts`)**:
            *   `mid`: TTS model ID (e.g., "cosy-voice").
            *   `style`, `emotion`: Control speaking style and emotion.
            *   `temperature`, `top_p`, `top_k`: Adjust sampling parameters for generation.
            *   Deprecated: `prompt`, `prompt1`, `prompt2`, `prefix`.
        *   **Voice Cloning (`vc`)** (Note: Potentially deprecated, mainly for OpenVoice):
            *   `enabled`, `mid`, `emotion`, `tau`.

        **Response**:
        *   **Success**: An audio file stream (`FileResponse`).
        *   **Failure**: A JSON object detailing the error.

        **Key Considerations**:
        1.  Ensure only one of `text`, `texts`, or `ssml` is provided.
        2.  For voice cloning, use high-quality reference audio (3-5 seconds recommended).
        3.  Enabling audio enhancement may increase generation latency.

        Parameters
        ----------
        adjust : typing.Optional[AdjustConfig]

        encoder : typing.Optional[EncoderConfig]

        enhance : typing.Optional[EnhancerConfig]

        infer : typing.Optional[InferConfig]

        vc : typing.Optional[VcConfig]

        tn : typing.Optional[TnConfig]

        tts : typing.Optional[TtsConfig]

        spk : typing.Optional[SpeakerConfig]

        text : typing.Optional[str]

        texts : typing.Optional[typing.Sequence[str]]

        ssml : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.forge_v2.forge_text_synthesize()
        """
        _response = self._raw_client.forge_text_synthesize(
            adjust=adjust,
            encoder=encoder,
            enhance=enhance,
            infer=infer,
            vc=vc,
            tn=tn,
            tts=tts,
            spk=spk,
            text=text,
            texts=texts,
            ssml=ssml,
            request_options=request_options,
        )
        return _response.data

    def transcribe_v2(
        self,
        *,
        input_audio: InputAudio,
        model: typing.Optional[str] = OMIT,
        refrence_transcript: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[float] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptionsResponse:
        """
        Transcribes audio using base64 or URL input. Stateless interface.

        Parameters
        ----------
        input_audio : InputAudio

        model : typing.Optional[str]
            ASR 模型名称，如 whisper.base、whisper.large

        refrence_transcript : typing.Optional[str]
            参考文案

        prompt : typing.Optional[str]
            提示词，用于引导模型

        prefix : typing.Optional[str]
            对话历史或固定开头

        language : typing.Optional[str]
            语言代码，如 'en', 'zh' 等

        temperature : typing.Optional[float]
            采样温度，控制多样性，范围 0~1

        sample_len : typing.Optional[int]
            采样长度，必须 >= 1

        best_of : typing.Optional[int]
            在 temperature > 0 时采样 n 次取最佳结果

        beam_size : typing.Optional[int]
            beam search 的宽度，推荐 5~10

        patience : typing.Optional[float]
            beam search 的 patience 参数，越大越宽松

        length_penalty : typing.Optional[float]
            对生成文本长度的惩罚，负值鼓励短输出

        format : typing.Optional[SttOutputFormat]
            输出格式，如 txt, json, srt, vtt

        highlight_words : typing.Optional[bool]
            是否高亮每个识别的单词（如 JSON 格式）

        max_line_count : typing.Optional[int]
            最大行数限制（用于格式化输出）

        max_line_width : typing.Optional[int]
            最大每行字符数（用于 txt 格式）

        max_words_per_line : typing.Optional[int]
            每行最多几个词（用于格式化输出）

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, InputAudio

        client = FernApi()
        client.forge_v2.transcribe_v2(
            input_audio=InputAudio(),
        )
        """
        _response = self._raw_client.transcribe_v2(
            input_audio=input_audio,
            model=model,
            refrence_transcript=refrence_transcript,
            prompt=prompt,
            prefix=prefix,
            language=language,
            temperature=temperature,
            sample_len=sample_len,
            best_of=best_of,
            beam_size=beam_size,
            patience=patience,
            length_penalty=length_penalty,
            format=format,
            highlight_words=highlight_words,
            max_line_count=max_line_count,
            max_line_width=max_line_width,
            max_words_per_line=max_words_per_line,
            request_options=request_options,
        )
        return _response.data


class AsyncForgeV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawForgeV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawForgeV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawForgeV2Client
        """
        return self._raw_client

    async def forge_text_synthesize(
        self,
        *,
        adjust: typing.Optional[AdjustConfig] = OMIT,
        encoder: typing.Optional[EncoderConfig] = OMIT,
        enhance: typing.Optional[EnhancerConfig] = OMIT,
        infer: typing.Optional[InferConfig] = OMIT,
        vc: typing.Optional[VcConfig] = OMIT,
        tn: typing.Optional[TnConfig] = OMIT,
        tts: typing.Optional[TtsConfig] = OMIT,
        spk: typing.Optional[SpeakerConfig] = OMIT,
        text: typing.Optional[str] = OMIT,
        texts: typing.Optional[typing.Sequence[str]] = OMIT,
        ssml: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        **Text-to-Speech Synthesis API (v2)**

        This endpoint converts text into speech, offering a wide range of customization options.
        It accepts JSON formatted data in the request body.

        **Core Functionality**:
        *   Synthesizes speech from various text inputs.
        *   Supports voice cloning by directly uploading a reference audio.

        **Input Flexibility**:
        *   Provide text via one of these mutually exclusive fields:
            *   `text`: A single string of text.
            *   `texts`: A list of strings for batch processing.
            *   `ssml`: Text formatted using Speech Synthesis Markup Language (SSML).

        **Speaker Customization (`spk`)**:
        *   Use pre-defined speakers via `spk.from_spk_id` or `spk.from_spk_name`.
        *   **Voice Cloning**: Provide reference audio for voice cloning:
            *   `spk.from_ref.wav_b64`: Base64 encoded WAV audio data.
            *   `spk.from_ref.text`: The transcript corresponding to the reference audio.

        **Audio Processing & Control**:
        *   **Adjustments (`adjust`)**:
            *   `pitch`: Modify audio pitch.
            *   `speed_rate`: Adjust speaking rate.
            *   `volume_gain_db`: Change audio volume.
            *   `normalize`: Apply volume normalization.
            *   `remove_silence`: Trim silence from audio ends.
        *   **Encoding (`encoder`)**:
            *   `format`: Output audio format (e.g., "mp3", "wav").
            *   `bitrate`: Audio bitrate (e.g., "64k").
            *   `acodec`: Audio codec (e.g., "libmp3lame").
        *   **Enhancement (`enhance`)**:
            *   `enabled`: Toggle audio enhancement.
            *   `model`: Select enhancement model.
            *   Additional parameters like `nfe`, `solver`, `lambd`, `tau` for fine-tuning.
        *   **Inference (`infer`)**:
            *   `batch_size`, `spliter_threshold`, `eos` for text processing.
            *   `seed`: For reproducible outputs.
            *   `stream`, `stream_chunk_size`: Enable and configure streaming output.
            *   `no_cache`, `sync_gen`: Control caching and generation mode.
        *   **Text Normalization (`tn`)**:
            *   `enabled`/`disabled`: Specify text normalization rules.
        *   **TTS Model Parameters (`tts`)**:
            *   `mid`: TTS model ID (e.g., "cosy-voice").
            *   `style`, `emotion`: Control speaking style and emotion.
            *   `temperature`, `top_p`, `top_k`: Adjust sampling parameters for generation.
            *   Deprecated: `prompt`, `prompt1`, `prompt2`, `prefix`.
        *   **Voice Cloning (`vc`)** (Note: Potentially deprecated, mainly for OpenVoice):
            *   `enabled`, `mid`, `emotion`, `tau`.

        **Response**:
        *   **Success**: An audio file stream (`FileResponse`).
        *   **Failure**: A JSON object detailing the error.

        **Key Considerations**:
        1.  Ensure only one of `text`, `texts`, or `ssml` is provided.
        2.  For voice cloning, use high-quality reference audio (3-5 seconds recommended).
        3.  Enabling audio enhancement may increase generation latency.

        Parameters
        ----------
        adjust : typing.Optional[AdjustConfig]

        encoder : typing.Optional[EncoderConfig]

        enhance : typing.Optional[EnhancerConfig]

        infer : typing.Optional[InferConfig]

        vc : typing.Optional[VcConfig]

        tn : typing.Optional[TnConfig]

        tts : typing.Optional[TtsConfig]

        spk : typing.Optional[SpeakerConfig]

        text : typing.Optional[str]

        texts : typing.Optional[typing.Sequence[str]]

        ssml : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.forge_v2.forge_text_synthesize()


        asyncio.run(main())
        """
        _response = await self._raw_client.forge_text_synthesize(
            adjust=adjust,
            encoder=encoder,
            enhance=enhance,
            infer=infer,
            vc=vc,
            tn=tn,
            tts=tts,
            spk=spk,
            text=text,
            texts=texts,
            ssml=ssml,
            request_options=request_options,
        )
        return _response.data

    async def transcribe_v2(
        self,
        *,
        input_audio: InputAudio,
        model: typing.Optional[str] = OMIT,
        refrence_transcript: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        sample_len: typing.Optional[int] = OMIT,
        best_of: typing.Optional[int] = OMIT,
        beam_size: typing.Optional[int] = OMIT,
        patience: typing.Optional[float] = OMIT,
        length_penalty: typing.Optional[float] = OMIT,
        format: typing.Optional[SttOutputFormat] = OMIT,
        highlight_words: typing.Optional[bool] = OMIT,
        max_line_count: typing.Optional[int] = OMIT,
        max_line_width: typing.Optional[int] = OMIT,
        max_words_per_line: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptionsResponse:
        """
        Transcribes audio using base64 or URL input. Stateless interface.

        Parameters
        ----------
        input_audio : InputAudio

        model : typing.Optional[str]
            ASR 模型名称，如 whisper.base、whisper.large

        refrence_transcript : typing.Optional[str]
            参考文案

        prompt : typing.Optional[str]
            提示词，用于引导模型

        prefix : typing.Optional[str]
            对话历史或固定开头

        language : typing.Optional[str]
            语言代码，如 'en', 'zh' 等

        temperature : typing.Optional[float]
            采样温度，控制多样性，范围 0~1

        sample_len : typing.Optional[int]
            采样长度，必须 >= 1

        best_of : typing.Optional[int]
            在 temperature > 0 时采样 n 次取最佳结果

        beam_size : typing.Optional[int]
            beam search 的宽度，推荐 5~10

        patience : typing.Optional[float]
            beam search 的 patience 参数，越大越宽松

        length_penalty : typing.Optional[float]
            对生成文本长度的惩罚，负值鼓励短输出

        format : typing.Optional[SttOutputFormat]
            输出格式，如 txt, json, srt, vtt

        highlight_words : typing.Optional[bool]
            是否高亮每个识别的单词（如 JSON 格式）

        max_line_count : typing.Optional[int]
            最大行数限制（用于格式化输出）

        max_line_width : typing.Optional[int]
            最大每行字符数（用于 txt 格式）

        max_words_per_line : typing.Optional[int]
            每行最多几个词（用于格式化输出）

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InputAudio

        client = AsyncFernApi()


        async def main() -> None:
            await client.forge_v2.transcribe_v2(
                input_audio=InputAudio(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transcribe_v2(
            input_audio=input_audio,
            model=model,
            refrence_transcript=refrence_transcript,
            prompt=prompt,
            prefix=prefix,
            language=language,
            temperature=temperature,
            sample_len=sample_len,
            best_of=best_of,
            beam_size=beam_size,
            patience=patience,
            length_penalty=length_penalty,
            format=format,
            highlight_words=highlight_words,
            max_line_count=max_line_count,
            max_line_width=max_line_width,
            max_words_per_line=max_words_per_line,
            request_options=request_options,
        )
        return _response.data
