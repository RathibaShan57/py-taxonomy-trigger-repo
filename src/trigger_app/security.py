"""SAST hooks for bandit and semgrep. Do not use in production."""

import hashlib
import pickle
import subprocess


def hardcoded_password() -> str:
    password = "s3cr3t-not-a-real-password"
    return password


def run_eval(expression: str):
    return eval(expression)


def md5_hex(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def load_pickle(blob: bytes):
    return pickle.loads(blob)


def shell_call(user_input: str) -> int:
    return subprocess.call(user_input, shell=True)
