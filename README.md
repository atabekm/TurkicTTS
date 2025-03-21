<h1 align="center">TurkicTTS <br> ⌨️ 🗣 </h1>

<p align="center">
  <a href="https://github.com/IS2AI/TurkicTTS/stargazers">
    <img src="https://img.shields.io/github/stars/IS2AI/TurkicTTS.svg?colorA=orange&colorB=orange&logo=github"
         alt="GitHub stars">
  </a>
  <a href="https://github.com/IS2AI/TurkicTTS/issues">
    <img src="https://img.shields.io/github/issues/IS2AI/TurkicTTS.svg"
         alt="GitHub issues">
  </a>
  <a href="https://issai.nu.edu.kz">
    <img src="https://img.shields.io/static/v1?label=ISSAI&amp;message=official site&amp;color=blue&amp"
         alt="ISSAI Official Website">
  </a> 
</p>

<p align = "center">This repository provides a demo and a pre-trained model for the paper <br><a href = "https://arxiv.org/abs/2305.15749"><b>Multilingual Text-to-Speech Synthesis for Turkic Languages Using Transliteration</b></a></p>

Please refer to original [repository](https://github.com/IS2AI/TurkicTTS) in order to get more information about the project. Below will contain only what has been added on top of the original project.

## Aim

The goal of this fork is to add a support for [Karakalpak language](https://en.wikipedia.org/wiki/Karakalpak_language) to TurkicTTS project. The architecture of the project allows it to achieve this target easily just by modifying ipa_converter.py file.

## What has been done?

For the moment, the minimum work has been done to support Karakalpak language. To be specific, since Kazakh language is pretty close to Karakalpak, `kazakh_to_ipa` function is copied with some modifications to the letters.

## How to improve?

As the author of the fork is not a linguistics expert, the project only can be considered as an experimental work. If you know experts in the area, it'd be a great help to get some assistance to improve the project.

## How to play around with the project (inference)?

### Clone the repo

```
git clone https://github.com/atabekm/TurkicTTS.git
cd TurkicTTS
```

### Download and extract files

#### Download the following files, and unzip them inside the TurkicTTS folder:

- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_male2_checkpoint.zip
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_male2_tacotron2_train.loss.ave.zip

### Create python virtual environment

```
python -m venv venv
```

### Activate the environment

```
. ./venv/bin/activate
```

### Install required dependencies

```
pip install -r requirements.txt
```

### Inference

```
python inference.py "Мине, бул биздеги күндеги көринис, яғный, бизиң мектепхана."
```

### Outcome. If successful, `result.wav` file will be generated in the root folder.
