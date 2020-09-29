# coding=utf-8
from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer
from .models import NpDbLocal, NPidinotherdatabase, NPenglishnamecas, NPderivativeassay, NPderivativeid, NPDtargetinfo, \
    NPassay, InfoDrug, InfoClinical, InfoClinical2, TargetDistribution, PhaseDistribution, ChemicalIndex, FDAPatent, \
    ClinicalDataBig, FDAdrugOrangeBook, FDAdrug, InactiveIngredientSearch, GenericDrugData, Clinicaldetail, \
    Clinicalbrowse


class NpDbLocalSerializer(DynamicModelSerializer):
    class Meta:
        model = NpDbLocal
        fields = ('database_id', 'formula', 'standard_inchi', 'standard_inchi_key',
                  'canonical_smiles', 'slogp', 'tpsa', 'amw', 'numrotatablebonds',
                  'numhbd', 'numhba', 'numheavyatoms', 'numrings',)


class NPidinotherdatabaseSerializer(DynamicModelSerializer):
    class Meta:
        model = NPidinotherdatabase
        fields = ('database_id', 'standard_inchi_key', 'chembl_id', 'sn_id',
                  'pubchem_cid', 'np_id')


class NPenglishnamecasSerializer(DynamicModelSerializer):
    class Meta:
        model = NPenglishnamecas
        fields = ('database_id', 'iupac_name', 'pref_name', 'cas')


class NPderivativeassaySerializer(DynamicModelSerializer):
    class Meta:
        model = NPderivativeassay
        fields = ('derivative_id', 'molecule_chembl_id', 'target_id', 'activity_type', 'activity_relation',
                  'activity_value', 'activity_units', 'reference', 'data_source_db')


class NPderivativeidSerializer(DynamicModelSerializer):
    class Meta:
        model = NPderivativeid
        fields = ('database_id', 'derivative_id')


class NPDtargetinfoSerializer(DynamicModelSerializer):
    class Meta:
        model = NPDtargetinfo
        fields = ('target_id', 'target_type', 'pref_name', 'organism', 'target_chembl_id')


class NPassaySerializer(DynamicModelSerializer):
    class Meta:
        model = NPassay
        fields = (
            'database_id', 'target_id', 'activity_type_sub', 'activity_relation', 'activity_value', 'activity_units',
            'reference', 'reference_type', 'data_source_db')


class InfoDrugSerializer(DynamicModelSerializer):
    class Meta:
        model = InfoDrug
        fields = ('id', 'pref_name', 'name', 'standard_inchi_key', 'canonical_smiles', 'chembl_id',
                  'max_phase', 'structure_type', 'molecule_type',
                  'first_approval', 'Target_based_Actions', 'Active_Indications')


# class InfoDrug2Serializer(DynamicModelSerializer):
#     class Meta:
#         model = InfoDrug2
#         fields = ('name', 'pref_name', 'chembl_id', 'max_phase', 'usan_stem_definition',
#                   'indication_class')


class InfoClinicalSerializer(DynamicModelSerializer):
    class Meta:
        model = InfoClinical
        fields = ('title', 'summary', 'status', 'phase', 'condation', 'intervention', 'location')


class InfoClinical2Serializer(DynamicModelSerializer):
    class Meta:
        model = InfoClinical2
        fields = ('title', 'summary', 'status', 'phase', 'condation', 'intervention', 'location')


class TargetDistributionSerializer(DynamicModelSerializer):
    class Meta:
        model = TargetDistribution
        fields = ('active_indications', 'target_based_actions', 'drug_name')


class PhaseDistributionSerializer(DynamicModelSerializer):
    class Meta:
        model = PhaseDistribution
        fields = ('phase', 'condation')


class GenericDrugDataSerializer(DynamicModelSerializer):
    class Meta:
        model = GenericDrugData
        fields = ('serial_number', 'generic_name', 'english_name_or_trade', 'specifications', 'dosage_form', 'remarks1',
                  'remarks2', 'information_sources')


class InactiveIngredientSearchSerializer(DynamicModelSerializer):
    class Meta:
        model = InactiveIngredientSearch
        fields = ('inactive_ingredient', 'route', 'dosage_form', 'cas_number', 'UNII', 'maximum_potency_per_unit_dose')


class FDAdrugSerializer(DynamicModelSerializer):
    class Meta:
        model = FDAdrug
        fields = ('trade_name', 'application_number', 'product_id', 'application_type', 'active_ingredient',
                  'dosage_form_or_route_of_administration', 'specification_or_dosage', 'RLD', 'RS',
                  'application_No_original_or_tentative_approval_date', 'product_number_approval_date', 'applicant',
                  'market_state')


class FDAdrugOrangeBookSerializer(DynamicModelSerializer):
    class Meta:
        model = FDAdrugOrangeBook
        fields = ('trade_name', 'application_number', 'product_id', 'application_type', 'active_ingredient',
                  'dosage_form_or_route_of_administration', 'specification_or_dosage', 'reference_drug_or_not',
                  'bioequivalence_reference_standard_or_not',
                  'treatment_equivalent_code', 'product_batch_date', 'applicant',
                  'market_state')


class ClinicalDataBigSerializer(DynamicModelSerializer):
    class Meta:
        model = ClinicalDataBig
        fields = ('url', 'other_study_id_numbers', 'trial_id', 'title', 'sponsor',
                  'agency_class', 'information_provider', 'brief_summary', 'detailed_description',
                  'recruitment_status', 'phase', 'study_type', 'intervention_model', 'study_design_primary_purpose',
                  'study_design_masking', 'target_disease', 'intervention_type', 'interventions', 'criteria', 'gender',
                  'minimum_age', 'maximum_age', 'healthy_volunteers', 'address', 'measure_outcome', 'study_design')


class FDAPatentSerializer(DynamicModelSerializer):
    class Meta:
        model = FDAPatent
        fields = ('patent_number', 'patent_link', 'patent_expiration_date', 'application_number', 'product_id',
                  'trade_name', 'active_ingredient', 'dosage_form', 'material_patent',
                  'product_patent', 'use_patent', 'detail_link')


class ChemicalIndexSerializer(DynamicModelSerializer):
    class Meta:
        model = ChemicalIndex
        fields = (
            'title', 'CAS_registry_number', 'CAS_name', 'additional_names', 'manufacturers_codes', 'molecular_formula',
            'molecular_weight', 'percent_composition', 'literature_references', 'properties', 'melting_point', 'pKa',
            'optical_rotation', 'logP', 'absorption_maximum', 'therap_cat', 'keywords', 'toxicity_data',
            'derivative_type',
            'derivativeCASRegistryNumber', 'derivativeTrademarks', 'derivativeMolecularFormula',
            'derivativeMolecularWeight', 'derivativePercentComposition')


class ClinicaldetailSerializer(DynamicModelSerializer):
    class Meta:
        model = Clinicaldetail
        fields = (
            'main_id', 'last_refreshed_on', 'secondary_id', 'public_title', 'scientific_title', 'url',
            'study_type', 'study_design', 'phase', 'date_of_registration', 'date_of_first_enrolment',
            'target_sample_size',
            'recruitment_status', 'primary_sponsor', 'secondary_sponsor', 'source_of_monetary_support',
            'countries_of_recruitment', 'health_condition_or_problem_studied',
            'intervention',
            'age_minimum', 'age_maximum', 'gender',
            'key_inclusion_exclusion_criteria', 'primary_outcome', 'secondary_outcome')


class ClinicalbrowseSerializer(DynamicModelSerializer):
    class Meta:
        model = Clinicalbrowse
        fields = (
            'main_id', 'public_title', 'date_of_registration', 'recruitment_status', 'phase')
