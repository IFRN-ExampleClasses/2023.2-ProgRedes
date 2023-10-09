import os, sys

# ------------------------------------------------------------------------------------------
DIR_APP = os.path.dirname(os.path.abspath(__file__))
DIR_IMG = DIR_APP + '\\images'

CODE_PAGE = 'utf-8'

METADATA_HEADER = ['TAGNumber', 'DataFormat', 'NumberComponentes', 'DataValue']

# (b'\x49\x49': Little Endian - Intel / b'\x4D\xD9': Big Endian - Motorola)
BYTE_ORDER = {b'\x49\x49': 'little', b'\x4D\x4D': 'big'}

TAG_NUMBER  = { b'\x01\x0e': 'ImageDescription'        , b'\x01\x0f': 'Make',
                b'\x01\x10': 'Model'                   , b'\x01\x12': 'Orientation',
                b'\x01\x1a': 'XResolution'             , b'\x01\x1b': 'YResolution',
                b'\x01\x28': 'ResolutionUnit'          , b'\x01\x31': 'Software',
                b'\x01\x32': 'DateTime'                , b'\x01\x3e': 'WhitePoint',
                b'\x01\x3f': 'PrimaryChromaticitie'    , b'\x02\x11': 'YCbCrCoefficients',
                b'\x02\x13': 'YCbCrPositioning'        , b'\x02\x14': 'ReferenceBlackWhite',
                b'\x82\x98': 'Copyright'               , b'\x87\x69': 'ExifOffset',
                b'\x01\x00': 'ImageWidth'              , b'\x01\x01': 'ImageLength',
                b'\x01\x02': 'BitsPerSample'           , b'\x01\x03': 'Compression',
                b'\x01\x06': 'PhotometricInterpretatio', b'\x01\x11': 'StripOffsets',
                b'\x01\x15': 'SamplesPerPixel'         , b'\x01\x16': 'RowsPerStrip',
                b'\x01\x17': 'StripByteConunts'        , b'\x01\x1a': 'XResolution',
                b'\x01\x1b': 'YResolution'             , b'\x01\x1c': 'PlanarConfiguration',
                b'\x01\x28': 'ResolutionUnit'          , b'\x02\x01': 'JpegIFOffset',
                b'\x02\x02': 'JpegIFByteCount'         , b'\x02\x11': 'YCbCrCoefficients',
                b'\x02\x12': 'YCbCrSubSampling'        , b'\x02\x13': 'YCbCrPositioning',
                b'\x02\x14': 'ReferenceBlackWhite'     , b'\x00\xfe': 'NewSubfileType',          
                b'\x00\xff': 'SubfileType'             , b'\x01\x2d': 'TransferFunction',
                b'\x01\x3b': 'Artist'                  , b'\x01\x3d': 'Predictor',
                b'\x01\x42': 'TileWidth'               , b'\x01\x43': 'TileLength',
                b'\x01\x44': 'TileOffsets'             , b'\x01\x45': 'TileByteCounts',
                b'\x01\x4a': 'SubIFDs'                 , b'\x01\x5b': 'JPEGTables',
                b'\x82\x8d': 'CFARepeatPatternDim'     , b'\x82\x8e': 'CFAPattern',
                b'\x82\x8f': 'BatteryLevel'            , b'\x83\xbb': 'IPTC/NAA',
                b'\x87\x73': 'InterColorProfile'       , b'\x88\x24': 'SpectralSensitivity',
                b'\x88\x25': 'GPSInfo'                 , b'\x88\x28': 'OECF',
                b'\x88\x29': 'Interlace'               , b'\x88\x2a': 'TimeZoneOffset',
                b'\x88\x2b': 'SelfTimerMode'           , b'\x92\x0b': 'FlashEnergy',
                b'\x92\x0c': 'SpatialFrequencyResponse', b'\x92\x0d': 'Noise',
                b'\x92\x11': 'ImageNumber'             , b'\x92\x12': 'SecurityClassification',
                b'\x92\x13': 'ImageHistory'            , b'\x92\x14': 'SubjectLocation',
                b'\x92\x15': 'ExposureIndex'           , b'\x92\x16': 'TIFF/EPStandardID',
                b'\x92\x90': 'SubSecTime'              , b'\x92\x91': 'SubSecTimeOriginal',
                b'\x92\x92': 'SubSecTimeDigitized'     , b'\xa2\x0b': 'FlashEnergy',
                b'\xa2\x0c': 'SpatialFrequencyResponse', b'\xa2\x14': 'SubjectLocation',
                b'\xa2\x15': 'ExposureIndex'           , b'\xa3\x02': 'CFAPattern'
                }

DATA_FORMAT = {b'\x01\x00': 'Unsigned Byte'    , b'\x02\x00': 'ASCII String', 
               b'\x03\x00': 'Unsigned Short'   , b'\x04\x00': 'Unsigned Long', 
               b'\x05\x00': 'Unsigned Rational', b'\x06\x00': 'Signed Byte', 
               b'\x07\x00': 'Undefinied'       , b'\x08\x00': 'Signed Short', 
               b'\x09\x00': 'Signed Long'      , b'\x10\x00': 'Signed Rational', 
               b'\x11\x00': 'Single Float'     , b'\x12\x00': 'Double Float'}
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
        fileContent.close()
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

    exifSize      = int.from_bytes(exifSize, byteorder=BYTE_ORDER[tiffHeader])
    countMetadata = int.from_bytes(countMetadata, byteorder=BYTE_ORDER[tiffHeader])

    dicEXIF = { 'exifSize' : exifSize, 'exifMarker': exifHeader, 
                'temp1'    : temp1   , 'tiffHeader': tiffHeader, 
                'temp2'    : temp2   , 'temp3'     : temp3,
                'metaCoumt': countMetadata}

    # Obtendo os Metadados
    lstMetadata   = list()
    for _ in range(countMetadata):
        lstTemp = [fileContent.read(2), fileContent.read(2),
                   fileContent.read(4), fileContent.read(4)]
        lstMetadata.append(dict(zip(METADATA_HEADER, lstTemp)))

    # Imprimindo os resultados
    print('\n\n', dicEXIF, '\n\n')
    
    # Imprimindo os metadatas lidos
    for metaData in lstMetadata: print(metaData)
    print('\n\n')

    # Invertendo os bytes das chaves do dicionário TAG_NUMBER (padrão II)
    if tiffHeader == b'\x49\x49':
        TAG_NUMBER = {key[::-1]: value for key, value in TAG_NUMBER.items()}

    # Tratando os dados obtidos
    for data in lstMetadata:
        data['TAGNumber']         = TAG_NUMBER[data['TAGNumber']]
        data['DataFormat']        = DATA_FORMAT[data['DataFormat']]
        data['NumberComponentes'] = int.from_bytes(data['NumberComponentes'], byteorder=BYTE_ORDER[tiffHeader])
        data['DataValue']         = int.from_bytes(data['DataValue'], byteorder=BYTE_ORDER[tiffHeader])
        if data['DataFormat'] == 'ASCII String':
            fileContent.seek(data['DataValue']+12,0)
            data['DataValue'] = fileContent.read(data['NumberComponentes']).decode(CODE_PAGE).rstrip('\x00')

    # Imprimindo os metadatas tratados
    for metaData in lstMetadata: print(metaData)
    print('\n\n')

    # Fechando o arquivo
    fileContent.close()

