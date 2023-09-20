import pytest  # noqa: F401

import karentify
from karentify.__main__ import main


def test_casing(capfd):
    karentify.tiktok = None
    main(['I', 'want', 'to', 'buy', 'a', 'damburger'])
    out, _ = capfd.readouterr()
    assert out == 'I WaNt tO BuY A DaMbUrGeR!!!\n'

    karentify.tiktok = None
    main(['i', 'want', 'to', 'buy', 'a', 'damburger'])
    out, _ = capfd.readouterr()
    assert out == 'i wAnT To bUy a dAmBuRgEr!!!\n'


def test_manager(capfd):
    karentify.tiktok = None
    main(['--dEmAnD-MaNaGeR', 'drivel', 'drivel'])
    out, _ = capfd.readouterr()
    assert out.lower().endswith('and i would like to talk to your manager!!!\n')

    karentify.tiktok = None
    main(['-D', 'drivel', 'drivel'])
    out, _ = capfd.readouterr()
    assert out.lower().endswith('and i would like to talk to your manager!!!\n')


def test_acting_out(capfd):
    karentify.tiktok = None
    main(['--AcT-ApPrOpRiAtElY', ''])
    out, err = capfd.readouterr()
    assert out.startswith('[')
    assert out.endswith(']!!!\n')

    karentify.tiktok = None
    main(['-A', ''])
    out, _ = capfd.readouterr()
    assert out.startswith('[')
    assert out.endswith(']!!!\n')


def test_punctuation(capfd):
    karentify.tiktok = None
    main(['test.'])
    out, _ = capfd.readouterr()
    assert out.lower().endswith('t!!!\n')

    karentify.tiktok = None
    main(['multiple exclamation marks, a sure sign of a diseased mind!!!'])
    out, _ = capfd.readouterr()
    assert out.lower().endswith('d!!!\n')
