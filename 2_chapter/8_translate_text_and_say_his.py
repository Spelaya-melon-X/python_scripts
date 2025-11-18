import asyncio
from googletrans import Translator  # type: ignore
from gtts import gTTS # type: ignore
import os


async def translate_text(text):
    translator = Translator()
    translated = await translator.translate(text, src="en", dest="ru")
    return translated.text


def text_to_speech(text, lang="ru"):
    tts = gTTS(text=text, lang=lang)
    filename = "output_file_translated.mp3"
    tts.save(filename)
    os.system("afplay " + filename)
    os.remove(filename)


async def main(english_text):
    # english_text = 'When are we going to fuck?'

    print(f"Оригинальный текст: {english_text}")

    russian_text = await translate_text(english_text)
    print(f"Переведённый текст: {russian_text}")

    text_to_speech(russian_text)


if __name__ == "__main__":
    asyncio.run(main(input("введите пж текст который вы бы хотели перевести на русский с английского ? ")))
