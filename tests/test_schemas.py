from app.schemas import Applicant
import pytest
from pydantic import ValidationError

def test_valid_applicant():
    applicant = Applicant(
        laufkont=2, laufzeit=12, moral=1, verw=0, hoehe=5000,
        sparkont=2, beszeit=1, rate=2, famges=2, buerge=1,
        wohnzeit=2, verm=2, alter=30, weitkred=2, wohn=1,
        bishkred=2, beruf=3, pers=1, telef=1, gastarb=1
    )
    assert applicant.laufkont == 2
    assert applicant.hoehe == 5000

def test_invalid_applicant():
    with pytest.raises(ValidationError):
        Applicant(
            laufkont=5,  # invalid: should be 1-4
            laufzeit=12, moral=1, verw=0, hoehe=5000,
            sparkont=2, beszeit=1, rate=2, famges=2, buerge=1,
            wohnzeit=2, verm=2, alter=30, weitkred=2, wohn=1,
            bishkred=2, beruf=3, pers=1, telef=1, gastarb=1
        )
