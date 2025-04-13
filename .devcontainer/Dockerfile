FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# explicitly copy files over in order to run pip install commands
COPY . .

# resolve libGL.so.1 issue
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 swig xvfb -y

RUN pip install --upgrade pip

RUN pip install torch torchvision torchaudio
ADD setup.py .
RUN pip install . tqdm rich debugpy swig
RUN pip install opencv-python

# Install headless opencv-python is encountering errors with
# opencv-python library
# RUN pip uninstall opencv-python
# RUN pip install opencv-python-headless

# Install gymnasium-based dependencies
# To run lunarlander env
RUN pip install gymnasium[box2d]
# To run humanoid env
RUN pip install gymnasium[mujoco]
