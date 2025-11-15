#!/bin/sh

curl -L -o kokoro.zip https://codeload.github.com/Hexgrad/Kokoro-TTS/zip/refs/heads/main
unzip kokoro.zip
mv Kokoro-TTS-main kokoro
pip install ./kokoro
