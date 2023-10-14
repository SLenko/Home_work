import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []
MY_OTHER = []
ARCHIVES_ZIP = []
ARCHIVES_GZ = []
ARCHIVES_TAR = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES_ZIP,
    'GZ': ARCHIVES_GZ,
    'TAR': ARCHIVES_TAR,
    
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] з .jpg робимо jpg

def scan(folder: Path):
    for item in folder.iterdir():

        # Робота з папкою
        if item.is_dir():  # перевірка чи об'єкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                extension_reg = REGISTER_EXTENSION[extension]
                extension_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # додаємо невідомі розширення в set
                MY_OTHER.append(full_name) 

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))

    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print (f'Images svg: {SVG_IMAGES}')

    print (f'Video avi: {AVI_VIDEO}')
    print (f'Video mp4: {MP4_VIDEO}')
    print (f'Video mov: {MOV_VIDEO}')
    print (f'Video mkv: {MKV_VIDEO}')

    print (f'Document doc: {DOC_DOCUMENT}')
    print (f'Document docx: {DOCX_DOCUMENT}')
    print (f'Document txt: {TXT_DOCUMENT}')
    print (f'Document pdf: {PDF_DOCUMENT}')
    print (f'Document xlsx: {XLSX_DOCUMENT}')
    print (f'Document pptx: {PPTX_DOCUMENT}')

    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio ogg: {OGG_AUDIO}')
    print(f'Audio wav: {WAV_AUDIO}')
    print(f'Audio amr: {AMR_AUDIO}')

    print(f'Archives zip: {ARCHIVES_ZIP}')
    print(f'Archives gz: {ARCHIVES_GZ}')
    print(f'Archives tar: {ARCHIVES_TAR}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
