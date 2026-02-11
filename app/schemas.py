# app/schemas.py

from pydantic import BaseModel, conint, Field

class Applicant(BaseModel):
    laufkont: conint(ge=1, le=4) = Field(
        ..., description="Status of existing checking account (1=very good, 4=critical)", json_schema_extra={"example": 2}
    )
    laufzeit: conint(ge=4, le=72) = Field(
        ..., description="Duration of the loan in months", json_schema_extra={"example": 12}
    )
    moral: conint(ge=0, le=4) = Field(
        ..., description="Credit history / Creditworthiness (0=excellent, 4=critical)", json_schema_extra={"example": 1}
    )
    verw: conint(ge=0, le=10) = Field(
        ..., description="Purpose of the credit (0=car, 1=furniture, 2=radio/TV,...)", json_schema_extra={"example": 0}
    )
    hoehe: conint(ge=250, le=18424) = Field(
        ..., description="Loan amount in DM (Deutsche Mark)", json_schema_extra={"example": 5000}
    )
    sparkont: conint(ge=1, le=5) = Field(
        ..., description="Status of savings account/bonds (1=very good, 5=unknown/none)", json_schema_extra={"example": 2}
    )
    beszeit: conint(ge=1, le=5) = Field(
        ..., description="Length of current employment in years (1=<1, 5=unemployed)", json_schema_extra={"example": 1}
    )
    rate: conint(ge=1, le=4) = Field(
        ..., description="Installment rate as a percentage of disposable income", json_schema_extra={"example": 2}
    )
    famges: conint(ge=1, le=4) = Field(
        ..., description="Personal status and sex (1=male div/sep, 2=female div/sep, etc.)", json_schema_extra={"example": 2}
    )
    buerge: conint(ge=1, le=3) = Field(
        ..., description="Other debtors / guarantors (1=none, 2=co-applicant, 3=guarantor)", json_schema_extra={"example": 1}
    )
    wohnzeit: conint(ge=1, le=4) = Field(
        ..., description="Present residence since (1=<1yr, 4=>=7yrs)", json_schema_extra={"example": 2}
    )
    verm: conint(ge=1, le=4) = Field(
        ..., description="Property (1=real estate, 2=life insurance, 3=car, 4=unknown/none)", json_schema_extra={"example": 2}
    )
    alter: conint(ge=19, le=75) = Field(
        ..., description="Age in years", json_schema_extra={"example": 30}
    )
    weitkred: conint(ge=1, le=3) = Field(
        ..., description="Other installment plans (1=bank, 2=store, 3=none)", json_schema_extra={"example": 2}
    )
    wohn: conint(ge=1, le=3) = Field(
        ..., description="Housing situation (1=rent, 2=own, 3=for free)", json_schema_extra={"example": 1}
    )
    bishkred: conint(ge=1, le=4) = Field(
        ..., description="Number of existing credits at this bank", json_schema_extra={"example": 2}
    )
    beruf: conint(ge=1, le=4) = Field(
        ..., description="Job category (1=unemployed/unskilled, 4=highly skilled)", json_schema_extra={"example": 3}
    )
    pers: conint(ge=1, le=2) = Field(
        ..., description="People liable for maintenance (1=none, 2=1 or more)", json_schema_extra={"example": 1}
    )
    telef: conint(ge=1, le=2) = Field(
        ..., description="Telephone availability (1=yes, 2=no)", json_schema_extra={"example": 1}
    )
    gastarb: conint(ge=1, le=2) = Field(
        ..., description="Foreign worker (1=yes, 2=no)", json_schema_extra={"example": 1}
    )
