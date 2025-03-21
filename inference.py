from parallel_wavegan.utils import load_model
from espnet2.bin.tts_inference import Text2Speech
from scipy.io.wavfile import write
from utils import normalization
import torch
import sys

if len(sys.argv) > 1:
    fs = 22050
    vocoder_checkpoint="parallelwavegan_male2_checkpoint/checkpoint-400000steps.pkl" ### specify vocoder path
    vocoder = load_model(vocoder_checkpoint).to("cpu").eval() # use cuda if available
    vocoder.remove_weight_norm()

    ### specify path to the main model(transformer/tacotron2/fastspeech) and its config file
    config_file = "exp/tts_train_raw_char/config.yaml"
    model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"

    text2speech = Text2Speech(
        config_file,
        model_path,
        device="cpu", ## use cuda if available
        ### only for Tacotron 2
        threshold=0.5,
        minlenratio=0.0,
        maxlenratio=10.0,
        use_att_constraint=True,
        backward_window=1,
        forward_window=3,
        ### only for FastSpeech & FastSpeech2
        speed_control_alpha=1.0,
    )
    text2speech.spc2wav = None  ### disable griffin-lim

    text_to_audio = sys.argv[1]
    text = (text_to_audio)
    ### available options are azerbaijani, bashkir, kazakh, kyrgyz, sakha, tatar, turkish, turkmen, uyghur, uzbek
    lang = "karakalpak"

    text = normalization(text, lang)
    with torch.no_grad():
        c_mel = text2speech(text)['feat_gen']
        wav = vocoder.inference(c_mel)
    write("result.wav", fs, wav.view(-1).cpu().numpy())
else:
    print("Usage: python inference.py 'Karakalpak text you want to turn to audio, in Cyrillic alphabet'")