from main import db


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    gender_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)
    birth_datetime = db.Column(db.DateTime, nullable=False)
    race_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)
    ethnicity_concept_id = db.Column(db.Integer, nullable=False)

    year_of_birth = db.Column(db.Integer, nullable=False)
    month_of_birth = db.Column(db.Integer, nullable=False)
    day_of_birth = db.Column(db.Integer, nullable=False)
    location_id = db.Column(db.Integer, nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    care_site_id = db.Column(db.Integer, nullable=True)
    person_source_value = db.Column(db.String(64), nullable=False)
    gender_source_value = db.Column(db.String(4), nullable=False)
    gender_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                         nullable=True)
    race_source_value = db.Column(db.String(32), nullable=False)
    race_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                       nullable=True)
    ethnicity_source_value = db.Column(db.String(32), nullable=False)
    ethnicity_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                            nullable=True)


class VisitOccurrence(db.Model):
    __tablename__ = 'visit_occurrence'
    visit_occurrence_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'), nullable=False)
    visit_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)
    visit_start_datetime = db.Column(db.DateTime, nullable=False)
    visit_end_datetime = db.Column(db.DateTime, nullable=False)

    visit_start_date = db.Column(db.Date, nullable=False)
    visit_end_date = db.Column(db.Date, nullable=False)
    visit_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                      nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    care_site_id = db.Column(db.Integer, nullable=True)
    visit_source_value = db.Column(db.String(64), nullable=False)
    visit_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                        nullable=True)
    admitting_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                            nullable=True)
    admitting_source_value = db.Column(db.String(64), nullable=True)
    discharge_to_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                        nullable=True)
    discharge_to_source_value = db.Column(db.String(64), nullable=True)
    preceding_visit_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                           nullable=True)


class ConditionOccurrence(db.Model):
    __tablename__ = 'condition_occurrence'
    condition_occurrence_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'), nullable=False)
    visit_occurrence_id = db.Column(db.Integer, db.ForeignKey('visit_occurrence.visit_occurrence_id',
                                                              ondelete='CASCADE'), nullable=False)
    condition_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=True)
    condition_start_datetime = db.Column(db.DateTime, nullable=False)
    condition_end_datetime = db.Column(db.DateTime, nullable=True)

    condition_start_date = db.Column(db.Date, nullable=False)
    condition_end_date = db.Column(db.Date, nullable=True)
    condition_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                          nullable=False)
    stop_reason = db.Column(db.String(64), nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    visit_detail_id = db.Column(db.Integer, nullable=False)
    condition_source_value = db.Column(db.String(64), nullable=False)
    condition_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                            nullable=True)
    condition_status_source_value = db.Column(db.String(64), nullable=True)
    condition_status_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                            nullable=True)


class Death(db.Model):
    __tablename__ = 'death'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'), nullable=False,
                          unique=True)
    death_date = db.Column(db.Date, nullable=False)

    death_datetime = db.Column(db.DateTime, nullable=True)
    death_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                      nullable=False)
    cause_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=True)
    cause_source_value = db.Column(db.String(64), nullable=False)
    cause_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                        nullable=True)


class DrugExposure(db.Model):
    __tablename__ = 'drug_exposure'
    drug_exposure_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'), nullable=False)
    drug_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=True)
    drug_exposure_start_datetime = db.Column(db.DateTime, nullable=True)
    drug_exposure_end_datetime = db.Column(db.DateTime, nullable=True)
    visit_occurrence_id = db.Column(db.Integer, db.ForeignKey('visit_occurrence.visit_occurrence_id',
                                                              ondelete='CASCADE'), nullable=False)
    drug_exposure_start_date = db.Column(db.Date, nullable=False)
    drug_exposure_end_date = db.Column(db.Date, nullable=False)
    verbatim_end_date = db.Column(db.Date, nullable=True)
    drug_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=True)
    stop_reason = db.Column(db.String(64), nullable=True)
    refills = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    days_supply = db.Column(db.Integer, nullable=False)
    sig = db.Column(db.String(64), nullable=True)
    route_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=True)
    lot_number = db.Column(db.Integer, nullable=False)
    provider_id = db.Column(db.Integer, nullable=False)
    drug_source_value = db.Column(db.String(32), nullable=False)
    drug_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'),
                                       nullable=True)
    route_source_value = db.Column(db.String(64), nullable=True)
    does_unit_source_value = db.Column(db.String(64), nullable=True)
    visit_detail_id = db.Column(db.Integer, nullable=True)


class Concept(db.Model):
    __tablename__ = 'concept'
    concept_id = db.Column(db.Integer, primary_key=True)
    concept_name = db.Column(db.String(256), nullable=True)
    domain_id = db.Column(db.String(32), nullable=False)

    vocabulary_id = db.Column(db.String(32), nullable=False)
    concept_class_id = db.Column(db.String(32), nullable=False)
    standard_concept = db.Column(db.String(64), nullable=True)
    concept_code = db.Column(db.String(64), nullable=True)
    valid_start_date = db.Column(db.Date, nullable=False)
    valid_end_date = db.Column(db.Date, nullable=False)
    invalid_reason = db.Column(db.String(32), nullable=True)