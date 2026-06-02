# Copyright (c) ModelScope Contributors. All rights reserved.
from __future__ import annotations

import sys
from transformers.utils import strtobool

_APPLIED = False
_ENABLE_SUPA_MODEL_PATCH_ARGS = ('--enable_supa_model_patch', '--enable-supa-model-patch')


def _parse_model_patch_enabled(value: str) -> bool:
    try:
        return bool(strtobool(value))
    except ValueError as exc:
        raise ValueError('--enable_supa_model_patch must be true or false.') from exc


def _is_model_patch_enabled_from_argv() -> bool:
    for i, arg in enumerate(sys.argv):
        if arg in _ENABLE_SUPA_MODEL_PATCH_ARGS:
            if i + 1 >= len(sys.argv) or sys.argv[i + 1].startswith('--'):
                raise ValueError('--enable_supa_model_patch requires a value: true or false.')
            return _parse_model_patch_enabled(sys.argv[i + 1])
        if any(arg.startswith(f'{name}=') for name in _ENABLE_SUPA_MODEL_PATCH_ARGS):
            value = arg.split('=', 1)[1]
            return _parse_model_patch_enabled(value)
    return True


def apply_all_patches() -> None:
    global _APPLIED
    if _APPLIED:
        return

    from . import env

    env.apply_patch()
    _APPLIED = True


__all__ = ['apply_all_patches']
