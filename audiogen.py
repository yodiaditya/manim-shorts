"""
MIT License

Copyright (c) 2025 Yodi aditya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import torch
import torchaudio
import ChatTTS
import io
import argparse

class TTS:
    def __init__(self, voice='male'):
        voice_seeds = {
            'female': 28,
            'male': 34,
            'male_alt_1': 43
        }
        print(f"Using voice {voice} with seed {voice_seeds[voice]}")
        self.voice_seed = voice_seeds[voice]
        torch.manual_seed(voice_seeds[voice])

    def load_model(self):
        self.chat = ChatTTS.Chat()
        self.chat.load(compile=False)

        torch.manual_seed(self.voice_seed)
        # self.rand_spk = self.chat.sample_random_speaker()
        self.rand_spk = torch.load('embedding/speaker_bad_late/std_spk_emb_df-seed68-bad.pt')
    
    def speak(self, text, temperature=0.18, top_p=0.9, top_k=20):
       
        if text:
            text = text.strip()
        
        params_infer_code = ChatTTS.Chat.InferCodeParams(
            spk_emb = self.rand_spk,
            temperature = temperature,
            top_P = top_p,
            top_K = top_k
        )

        params_refine_text = ChatTTS.Chat.RefineTextParams(
            prompt='[oral_2][laugh_0][break_4]',
        )

        text = """Lets go to first solution, which is Brute Force. 
                  Iterate to each element in array and match sum with target. 
                  This is not efficient with time complexity is n power by two. [uv_break][uv_break]
                  The best solution is using hashmap. I will walk you through the steps on how we do it.[uv_break][uv_break]
                  Step one is Create an Hashmap [uv_break][uv_break][uv_break]
                  Step two Iterate Array [uv_break][uv_break][uv_break][uv_break]
                  Step three Calculate the remaining [uv_break][uv_break][uv_break]
                  Step four Check if in Hashmap exists [uv_break][uv_break][uv_break]
                  Step five If not found, add into Hashmap [uv_break][uv_break][uv_break]
                  I hope this help you. Thanks for watching.   
                  """.replace('\n', '') # English is still experimental.

        params_refine_text = ChatTTS.Chat.RefineTextParams(
            prompt='[oral_2][laugh_0][break_4]',
        )

        wavs = self.chat.infer(text, skip_refine_text=True, 
                               params_infer_code=params_infer_code,
                               params_refine_text=params_refine_text)
    
        wav_file = io.BytesIO()
        torchaudio.save(wav_file, torch.from_numpy(wavs[0]).unsqueeze(0), 
                        24000, format='wav', backend='ffmpeg')

        return wav_file
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text to Speech using ChatTTS')
    parser.add_argument('--text', type=str, required=False, help='Text to convert to speech')
    args = parser.parse_args()

    tts = TTS()
    tts.load_model()
    wav = tts.speak(args.text)

    with open(f"output.wav", "wb") as f:
        f.write(wav.getvalue())
