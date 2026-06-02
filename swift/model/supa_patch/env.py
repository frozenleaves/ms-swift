# Copyright (c) ModelScope Contributors. All rights reserved.
import os


def apply_patch() -> None:
    if 'BCCL_CONNECT_TIMEOUT' not in os.environ:
        os.environ['BCCL_CONNECT_TIMEOUT'] = '600'
