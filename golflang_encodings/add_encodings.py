#!/usr/bin/env python3

import importlib
import pkgutil
import golflang_encodings
import codecs

# adapted from https://stackoverflow.com/a/25562415/2508324


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages
    :param package: package (name or actual module)
    :param recursive: recursively import submodules?
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


submods = import_submodules(golflang_encodings)
codepages = {}
for mod in submods.values():
    try:
        codepages[mod.NAME] = {k: ord(v) for k,v in mod.CODEPAGE.items()}
    except:
        pass

# PyOEM is a special case
codepages["pyoem"] = golflang_encodings.PyOEM.pyoem.decoding_map


def make_classes(name):
    decoding_map = codepages[name]
    encoding_map = codecs.make_encoding_map(decoding_map)

    class _Codec(codecs.Codec):
        def encode(self, input, errors='strict'):
            return codecs.charmap_encode(input, errors, encoding_map)

        def decode(self, input, errors='strict'):
            return codecs.charmap_decode(input, errors, decoding_map)

    class _IncrementalEncoder(codecs.IncrementalEncoder):
        def encode(self, input, final=False):
            data, nbytes = codecs.charmap_encode(input, self.errors, encoding_map)
            return data

    class _IncrementalDecoder(codecs.IncrementalDecoder):
        def decode(self, input, final=False):
            data, nbytes = codecs.charmap_decode(input, self.errors, decoding_map)
            return data

    class _StreamReader(_Codec, codecs.StreamReader):
        pass

    class _StreamWriter(_Codec, codecs.StreamWriter):
        pass

    return _Codec, _IncrementalEncoder, _IncrementalDecoder, _StreamReader, _StreamWriter


def make_finder(name, classes):
    codec, incremental_encoder, incremental_decoder, stream_reader, stream_writer = classes

    def _find_codec(encoding):
        if '-'.join(encoding.lower().split()) == '-'.join(name.lower().split()):
            return codecs.CodecInfo(
                name=name,
                encode=codec().encode,
                decode=codec().decode,
                incrementalencoder=incremental_encoder,
                incrementaldecoder=incremental_decoder,
                streamreader=stream_reader,
                streamwriter=stream_writer,
            )
        return None

    return _find_codec


def register_codec(name):
    classes = make_classes(name)
    finder = make_finder(name, classes)
    codecs.register(finder)


def register_codecs():
    for codec_name in codepages:
        register_codec(codec_name)


if __name__ == "__main__":
    register_codecs()
