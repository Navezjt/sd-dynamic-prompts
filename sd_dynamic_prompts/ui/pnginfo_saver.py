from __future__ import annotations

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ImagePrompts:
    prompt: str
    negative_prompt: str


class PngInfoSaver:
    def update_pnginfo(self, parameters: str, image_prompts: ImagePrompts):
        if image_prompts.prompt != "":
            parameters += "\nTemplate:" + image_prompts.prompt

        if image_prompts.negative_prompt != "":
            parameters += "\nNegative Template:" + image_prompts.negative_prompt

        return parameters