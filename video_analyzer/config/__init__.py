# -*- coding: utf-8 -*-
"""
配置模块
"""

from .settings import (
    # API
    API_KEY,
    API_BASE_URL,
    get_api_key,
    get_api_base_url,
    
    # 模型
    VISION_MODEL,
    VISION_FALLBACK_MODELS,
    NARRATION_MODEL,
    NARRATION_FALLBACK_MODELS,
    GOD_MODE_MODEL,
    GOD_MODE_FALLBACK_MODELS,
    
    # 路径
    JIANYING_DRAFT_DIR,
    OUTPUT_BASE_DIR,
    
    # 处理参数
    SCENE_THRESHOLD,
    MIN_SCENE_DURATION,
    MAX_SCENE_DURATION,
    
    # 智能分块配置
    LONG_VIDEO_THRESHOLD,
    TARGET_CHUNK_DURATION,
    MIN_CHUNK_DURATION,
    MAX_CHUNK_DURATION,
    MAX_PARALLEL_GEMINI,
    
    # 并发控制
    MAX_CONCURRENT_REQUESTS,
    MAX_CONCURRENT_EXTRACT,
    REQUEST_DELAY,
    IMAGE_MAX_SIZE,
    BATCH_SIZE,
    
    # TTS
    TTS_ENGINE,
    TTS_VOICE,
    TTS_RATE,
    TTS_CONCURRENT,
    
    # 字幕
    SUBTITLE_STYLE,
    FONT_SIZE,
    
    # Chinese-CLIP 配置
    CLIP_MODEL_NAME,
    CLIP_FEATURE_DIM,
    CLIP_CACHE_DIR,
    
    # 文案匹配配置
    MATCH_MIN_SIMILARITY,
    MATCH_AVOID_ADJACENT_REPEAT,
    
    # 函数
    get_vision_model,
    get_narration_model,
    get_god_mode_model,
    get_clip_model_name,
    get_match_min_similarity,
)

# 解说风格配置
from .narration_styles import (
    NarrationStyle,
    NARRATION_STYLES,
    STYLE_LIST,
    get_style,
    get_all_styles,
)

# Prompt 管理
from .prompt_manager import (
    get_prompt_manager,
    get_prompt,
    PromptManager,
    PromptInfo,
    PROMPT_CATEGORIES,
    PROMPT_REGISTRY,
)
