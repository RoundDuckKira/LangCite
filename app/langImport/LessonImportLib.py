try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract as tess
import PyPDF2
import io
import json
import unicodedata
from youtube_transcript_api import YouTubeTranscriptApi
from pdf2image import convert_from_path
import os
try:
    # python 3
    from urllib.parse import urlparse, parse_qs
except ImportError:
    # python 2
    from urlparse import urlparse, parse_qs


# pass image and language reference to create lesson
def image_to_string(image_file, imageLang):
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_string = tess.image_to_string(Image.open(image_file), lang=imageLang)
   
    os.remove(image_file)
    return image_string


# pass a string and create a json file
def string_to_json(lesson_string, target_lang, native_lang):
    lesson_string = lesson_string.replace("\n", " ")
    lesson_string = lesson_string.replace("- ", '')
    lesson_string = lesson_string.replace("\\", '')
    lesson_string = lesson_string.split(". ")

    new_json = ''

    for x in lesson_string:
        k = x.split(" ")
        for y in k:

            nj = "{'" + target_lang + "':" + "'" + y + "','" + native_lang + "':" + "'" + "' },"
            print(nj)
            new_json = new_json + nj

    new_json = new_json.rstrip(new_json[-1])
    new_json = "{'lesson_words': [" + new_json + "]}"
    new_json = new_json.replace("'", '"')  # replaces single quotes with double quotes
    new_json = remove_control_characters(new_json)
    print(new_json)
    new_json = json.loads(new_json)
    return json.dumps(new_json, ensure_ascii=False)


# pass video code, target language and native language to create a json file
def youtube_to_json(urlString, targetLang, nativeLang):
    video_id = urlString
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[targetLang, nativeLang])

    transcript = str(transcript)

    new = transcript.replace('"', '')  # removes double quotes
    new = new.replace("'", '"')  # replaces single quotes with double quotes
    print(type(new))

    new_string = new.replace('\\xa0', '')  # removes \\XaO
    new_string = new_string.replace('\\n', ' ')  # replaces \n with a space
    new_string = json.loads(new_string)
    return json.dumps(new_string, ensure_ascii=False)

    

# converts a pdf to image then image to string
# depends on image_to_string method to work!!!
def pdf_to_string(pdf_file, target_lang):
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)
    newstring = ''
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('temp_images/_page' + str(i) + '.jpg', 'JPEG')

    for i in range(len(images)):
        newstring = newstring + image_to_string('temp_images/_page' + str(i) + '.jpg', target_lang)
        
    os.remove(pdf_file)

    return newstring

def text_to_string(text_file, target_lang, native_lang):
    # new_file_name = os.path.splitext(text_file)[0] + ''
    text = io.open(text_file, 'r', encoding="utf-8")
    text_json_obj = string_to_json(text.read(), target_lang, native_lang)
    text.close()
    # os.remove(text_file)
    return text_json_obj

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


def extract_id(url):
    """Returns Video_ID extracting from the given url of Youtube

    Examples of URLs:
      Valid:
        'http://youtu.be/_lOT2p_FCvA',
        'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
        'http://www.youtube.com/embed/_lOT2p_FCvA',
        'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
        'youtube.com/watch?v=_lOT2p_FCvA',

      Invalid:
        'youtu.be/watch?v=_lOT2p_FCvA',
    """

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url

    query = urlparse(url)

    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError

# pass a string, the native language and target language to get the translated text
def translate_string(target_string, native_lang, target_lang):
    translated_text = translator(target_lang, native_lang, target_string)
    print(translated_text[0][0][0])
    return translated_text

#finds all the language codes that need to be translated to
def find_all_to_translate(native_lang):
    language_codes = ['en', 'ru', 'fr', 'es']
    codes_to_translate = []
    for x in language_codes:
        if x == native_lang:
            pass
        else:
            codes_to_translate.append(x)
    return codes_to_translate

#translates a word in all available lanuages
def translate_to_all(target_string, native_lang, lang_codes):
    for x in lang_codes:
        translate_string(target_string, native_lang, x)
