import pytest
from media import Media

def test_add_nota():
    media = Media()
    assert len(media.notas()) == 0
    media.add(3)
    assert len(media.notas()) == 1

def test_add_Nota_Error_20():
    media = Media()
    media.notas().clear()
    assert len(media.notas()) == 0
    with pytest.raises(ValueError):
        media.add(20)

def test_add_Nota_Error_low():
    media = Media()
    assert len(media.notas()) == 0
    with pytest.raises(ValueError):
        media.add(-1)

def test_media():
    media = Media()
    assert len(media.notas()) == 0
    media.add(5)
    media.add(5)
    media.add(5)
    assert len(media.notas()) == 3
    assert media.media() == 5.0