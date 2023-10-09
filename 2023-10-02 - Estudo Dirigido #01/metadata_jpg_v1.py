import os, sys

# ------------------------------------------------------------------------------------------
DIR_APP = os.path.dirname(os.path.abspath(__file__))
DIR_IMG = DIR_APP + '\\images'

# ------------------------------------------------------------------------------------------

strNomeArq = DIR_IMG + '\\LMC_20221219_202142_v7.jpg'

try:
    fileContent = open(strNomeArq, 'rb')
except FileNotFoundError:
    print('\nERRO: Arquivo Não Existe...\n')
    sys.exit()
except:
    print(f'\nERRO: {sys.exc_info()[1]}...\n')
    sys.exit()
else:
    # Verificando se o arquivo informado é JPG 
    if fileContent.read(2) != b'\xFF\xD8':
        print('\nERRO: Arquivo informado não é JPG...\n')
        sys.exit()

    # Verifica se o arquivo possui metadados
    if fileContent.read(2) != b'\xFF\xE1':
        fileContent.close()
        print('\nAVISO: Este arquivo não possui metadados...\n')
        sys.exit()

    # Obtendo EXIF
    exifSize      = fileContent.read(2)
    exifHeader    = fileContent.read(4) # EXIF Header (marcador EXIF)
    temp1         = fileContent.read(2) # EXIF Header (fixo)
    tiffHeader    = fileContent.read(2) # (49 49: Little Endian - Intel / 4D 4D: Big Endian - Motorola)
    temp2         = fileContent.read(2) # TIFF Header (fixo)
    temp3         = fileContent.read(4) # TIFF Header (fixo)
    countMetadata = fileContent.read(2) # Metadata Count

    if tiffHeader == b'\x49\x49':
        exifSize      = int.from_bytes(exifSize, byteorder='little')
        countMetadata = int.from_bytes(countMetadata, byteorder='little')
    else:
        exifSize      = int.from_bytes(exifSize, byteorder='big')
        countMetadata = int.from_bytes(countMetadata, byteorder='big')

    dicEXIF = { 'exifSize' : exifSize, 'exifMarker': exifHeader, 
                'temp1'    : temp1   , 'tiffHeader': tiffHeader, 
                'temp2'    : temp2   , 'temp3'     : temp3,
                'metaCoumt': countMetadata}

    # Obtendo os Metadados
    lstMetadata   = list()
    lstMetaHeader = ['TAGNumber', 'DataFormat', 'NumberComponentes', 'DataValue']
    for _ in range(countMetadata):
        lstTemp = [fileContent.read(2), fileContent.read(2),
                   fileContent.read(4), fileContent.read(4)]
        lstMetadata.append(dict(zip(lstMetaHeader, lstTemp)))

    # Imprimindo os resultados
    print('\n\n', dicEXIF, '\n\n')
    
    # Imprimindo os metadatas lidos
    for metaData in lstMetadata: print(metaData)
    print('\n\n')

