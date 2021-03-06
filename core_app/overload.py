def string_to_html(our_str):
    our_str = our_str.replace('Á', '&Aacute;')
    our_str = our_str.replace('á', '&aacute;')
    our_str = our_str.replace('Â', '&Acirc;')
    our_str = our_str.replace('â', '&acirc;')
    our_str = our_str.replace('À', '&Agrave;')
    our_str = our_str.replace('à', '&agrave;')
    our_str = our_str.replace('Å', '&Aring;')
    our_str = our_str.replace('å', '&aring;')
    our_str = our_str.replace('Ã', '&Atilde;')
    our_str = our_str.replace('ã', '&atilde;')
    our_str = our_str.replace('Ä', '&Auml;')
    our_str = our_str.replace('ä', '&auml;')
    our_str = our_str.replace('Æ', '&AElig;')
    our_str = our_str.replace('æ', '&aelig;')
    our_str = our_str.replace('É', '&Eacute;')
    our_str = our_str.replace('é', '&eacute;')
    our_str = our_str.replace('Ê', '&Ecirc;')
    our_str = our_str.replace('ê', '&ecirc;')
    our_str = our_str.replace('È', '&Egrave;')
    our_str = our_str.replace('è', '&egrave;')
    our_str = our_str.replace('Ë', '&Euml;')
    our_str = our_str.replace('ë', '&euml;')
    our_str = our_str.replace('Ð', '&ETH;')
    our_str = our_str.replace('ð', '&eth;')
    our_str = our_str.replace('Í', '&Iacute;')
    our_str = our_str.replace('í', '&iacute;')
    our_str = our_str.replace('Î', '&Icirc;')
    our_str = our_str.replace('î', '&icirc;')
    our_str = our_str.replace('Ì', '&Igrave;')
    our_str = our_str.replace('ì', '&igrave;')
    our_str = our_str.replace('Ï', '&Iuml;')
    our_str = our_str.replace('ï', '&iuml;')
    our_str = our_str.replace('Ó', '&Oacute;')
    our_str = our_str.replace('ó', '&oacute;')
    our_str = our_str.replace('Ô', '&Ocirc;')
    our_str = our_str.replace('ô', '&ocirc;')
    our_str = our_str.replace('Ò', '&Ograve;')
    our_str = our_str.replace('ò', '&ograve;')
    our_str = our_str.replace('Ø', '&Oslash;')
    our_str = our_str.replace('ø', '&oslash;')
    our_str = our_str.replace('Õ', '&Otilde;')
    our_str = our_str.replace('õ', '&otilde;')
    our_str = our_str.replace('Ö', '&Ouml;')
    our_str = our_str.replace('ö', '&ouml;')
    our_str = our_str.replace('Ú', '&Uacute;')
    our_str = our_str.replace('ú', '&uacute;')
    our_str = our_str.replace('Û', '&Ucirc;')
    our_str = our_str.replace('û', '&ucirc;')
    our_str = our_str.replace('Ù', '&Ugrave;')
    our_str = our_str.replace('ù', '&ugrave;')
    our_str = our_str.replace('Ü', '&Uuml;')
    our_str = our_str.replace('ü', '&uuml;')
    our_str = our_str.replace('Ç', '&Ccedil;')
    our_str = our_str.replace('ç', '&ccedil;')
    our_str = our_str.replace('Ñ', '&Ntilde;')
    our_str = our_str.replace('ñ', '&ntilde;')
    our_str = our_str.replace('<', '&lt;')
    our_str = our_str.replace('>', '&gt;')
    our_str = our_str.replace('"', '&quot;')
    our_str = our_str.replace('®', '&reg;')
    our_str = our_str.replace('©', '&copy;')
    our_str = our_str.replace('Ý', '&Yacute;')
    our_str = our_str.replace('ý', '&yacute;')
    our_str = our_str.replace('Þ', '&THORN;')
    our_str = our_str.replace('þ', '&thorn;')
    our_str = our_str.replace('ß', '&szlig;')
    return our_str
