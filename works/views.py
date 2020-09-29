import django_filters
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic
from dynamic_rest.pagination import DynamicPageNumberPagination
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.response import Response
from rest_framework import mixins, viewsets, request, status, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework_jwt.serializers import User
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

# from apps.works.filters import ServerFilter
from .models import NpDbLocal, NPidinotherdatabase, NPenglishnamecas, NPderivativeassay, NPderivativeid, NPDtargetinfo, \
    NPassay, InfoDrug, InfoClinical, InfoClinical2, TargetDistribution, PhaseDistribution, ChemicalIndex, FDAPatent, \
    ClinicalDataBig, FDAdrugOrangeBook, FDAdrug, InactiveIngredientSearch, GenericDrugData, Clinicaldetail, \
    Clinicalbrowse
from .serializers import NpDbLocalSerializer, NPidinotherdatabaseSerializer, NPenglishnamecasSerializer, \
    NPderivativeassaySerializer, NPderivativeidSerializer, NPDtargetinfoSerializer, NPassaySerializer, \
    InfoDrugSerializer, InfoClinicalSerializer, InfoClinical2Serializer, PhaseDistributionSerializer, \
    TargetDistributionSerializer, ChemicalIndexSerializer, FDAPatentSerializer, ClinicalDataBigSerializer, \
    FDAdrugOrangeBookSerializer, FDAdrugSerializer, InactiveIngredientSearchSerializer, GenericDrugDataSerializer, \
    ClinicaldetailSerializer, ClinicalbrowseSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework


class StandardResultsSetPagination(DynamicPageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # page_query_param = 'page'
    max_page_size = 10


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10  # 默认两个
    max_page_size = 10  # 一页显示最大5个
    page_query_param = 'page'  # 页码


class NpDbLocalViewSet(DynamicModelViewSet):
    queryset = NpDbLocal.objects.all()
    serializer_class = NpDbLocalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('database_id', 'formula', 'standard_inchi', 'standard_inchi_key',
                     'canonical_smiles',
                     'slogp', 'tpsa', 'amw', 'numrotatablebonds',
                     'numhbd', 'numhba', 'numheavyatoms', 'numrings',
                     )
    filter_fields = ('database_id', 'formula', 'standard_inchi', 'standard_inchi_key',
                     'canonical_smiles',
                     'slogp', 'tpsa', 'amw', 'numrotatablebonds',
                     'numhbd', 'numhba', 'numheavyatoms', 'numrings',
                     )


class NPidinotherdatabaseViewSet(DynamicModelViewSet):
    queryset = NPidinotherdatabase.objects.all()
    serializer_class = NPidinotherdatabaseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('database_id', 'standard_inchi_key', 'chembl_id', 'sn_id',
                     'pubchem_cid', 'np_id')
    filter_fields = ('database_id', 'standard_inchi_key', 'chembl_id', 'sn_id',
                     'pubchem_cid', 'np_id')


class NPenglishnamecasViewSet(DynamicModelViewSet):
    queryset = NPenglishnamecas.objects.all()
    serializer_class = NPenglishnamecasSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('database_id', 'iupac_name', 'pref_name', 'cas')
    filter_fields = ('database_id', 'iupac_name', 'pref_name', 'cas')


class NPderivativeassayViewSet(DynamicModelViewSet):
    queryset = NPderivativeassay.objects.all()
    serializer_class = NPderivativeassaySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('derivative_id', 'molecule_chembl_id', 'target_id', 'activity_type', 'activity_relation',
                     'activity_value', 'activity_units', 'reference', 'data_source_db')
    filter_fields = ('derivative_id', 'molecule_chembl_id', 'target_id', 'activity_type', 'activity_relation',
                     'activity_value', 'activity_units', 'reference', 'data_source_db')


class NPderivativeidViewSet(DynamicModelViewSet):
    queryset = NPderivativeid.objects.all()
    serializer_class = NPderivativeidSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('database_id', 'derivative_id')
    filter_fields = ('database_id', 'derivative_id')


class NPDtargetinfoViewSet(DynamicModelViewSet):
    queryset = NPDtargetinfo.objects.all()
    serializer_class = NPDtargetinfoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('target_id', 'target_type', 'pref_name', 'organism', 'target_chembl_id')
    filter_fields = ('target_id', 'target_type', 'pref_name', 'organism', 'target_chembl_id')


class NPassayViewSet(DynamicModelViewSet):
    queryset = NPassay.objects.all()
    serializer_class = NPassaySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = (
        'database_id', 'target_id', 'activity_type_sub', 'activity_relation', 'activity_value', 'activity_units',
        'reference', 'reference_type', 'data_source_db')
    filter_fields = (
        'database_id', 'target_id', 'activity_type_sub', 'activity_relation', 'activity_value', 'activity_units',
        'reference', 'reference_type', 'data_source_db')


class InfoDrugViewSet(DynamicModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = InfoDrug.objects.all()
    serializer_class = InfoDrugSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = ('id', 'pref_name', 'name', 'standard_inchi_key', 'canonical_smiles', 'chembl_id',
                     'max_phase', 'structure_type', 'molecule_type',
                     'first_approval', 'Target_based_Actions', 'Active_Indications')
    search_fields = ('id', 'pref_name', 'name', 'standard_inchi_key', 'canonical_smiles', 'chembl_id',
                     'max_phase', 'structure_type', 'molecule_type',
                     'first_approval', 'Target_based_Actions', 'Active_Indications')


# class InfoDrug2ViewSet(DynamicModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = InfoDrug2.objects.all()
#     serializer_class = InfoDrug2Serializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class = StandardResultsSetPagination
#     filter_backends = (SearchFilter, DjangoFilterBackend)
#     filter_fields = ('name', 'pref_name', 'chembl_id', 'max_phase', 'usan_stem_definition',
#                      'indication_class')
#     search_fields = ('name', 'pref_name', 'chembl_id', 'max_phase', 'usan_stem_definition',
#                      'indication_class')


class InfoClinicalViewSet(DynamicModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = InfoClinical.objects.all()
    serializer_class = InfoClinicalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = (
        'title',
        'summary',
        'status',
        'phase',
        'condation',
        'intervention',
        'location')
    search_fields = (
        'title',
        'summary',
        'status',
        'phase',
        'condation',
        'intervention',
        'location')


class PhaseDistributionView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        if pk is not None:  # 如果参数不为空
            # 执行filter()方法
            queryset = PhaseDistribution.objects.filter(condation__icontains=pk).values('phase', 'drug').distinct()
            phases = [i['phase'] for i in queryset.values()]
            phases_uni = list(set(phases))
            phase_drug_dict = {}
            for phase in phases_uni:
                phase_drug_dict[phase] = []
            for i in queryset.values():
                phase = i['phase']
                phase_drug_dict[phase].append(i['drug'])
            phase_drug_count_dict = {}
            for k, v in phase_drug_dict.items():
                phase_drug_count_dict[k] = len(list(set(v)))
            a = sorted(phase_drug_count_dict.items(), key=lambda x: x[-1], reverse=True)
            return Response(a)
        else:
            pg = MyPageNumberPagination()
            queryset = PhaseDistribution.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = PhaseDistributionSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class InfoClinical2View(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk1 = self.request.GET.get('pk1')
        pk2 = self.request.GET.get('pk2')
        if pk1 is not None:  # 如果参数不为空
            pg = MyPageNumberPagination()
            # 执行filter()方法
            queryset = Clinicaldetail.objects.filter(
                health_condition_or_problem_studied__icontains=pk1).filter(phase__icontains=pk2).order_by(
                '-date_of_registration').distinct()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = ClinicaldetailSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            # 执行filter()方法
            queryset = Clinicaldetail.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = ClinicaldetailSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class TargetDistributionView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        if pk is not None:  # 如果参数不为空
            queryset = TargetDistribution.objects.filter(active_indications__icontains=pk).values(
                'target_based_actions',
                'drug_name').distinct()
            targets = [i['target_based_actions'] for i in queryset.values()]
            targets_uni = list(set(targets))
            target_drug_dict = {}
            for target in targets_uni:
                target_drug_dict[target] = []
            for i in queryset.values():
                target = i['target_based_actions']
                target_drug_dict[target].append(i['drug_name'])
            target_drug_count_dict = {}
            for k, v in target_drug_dict.items():
                target_drug_count_dict[k] = len(list(set(v)))
            a = sorted(target_drug_count_dict.items(), key=lambda x: x[-1], reverse=True)
            L = []
            for i, j in a:
                d = {}
                d['value'] = j
                d['name'] = i
                L.append(d)
            return Response(L)
        else:
            pg = MyPageNumberPagination()
            queryset = TargetDistribution.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = TargetDistributionSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class GenericDrugDataView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        pk1 = self.request.GET.get('pk1')
        if pk:
            pg = MyPageNumberPagination()
            queryset = GenericDrugData.objects.filter(
                Q(serial_number__icontains=pk) | Q(generic_name__icontains=pk) | Q(
                    english_name_or_trade__icontains=pk) | Q(
                    specifications__icontains=pk) | Q(dosage_form__icontains=pk) | Q(
                    holder__icontains=pk) | Q(
                    remarks1__icontains=pk) | Q(remarks2__icontains=pk) | Q(
                    information_sources__icontains=pk))
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = GenericDrugDataSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        if pk1:
            pk2 = self.request.GET.get('pk2')
            pk1 = pk1.split('*')
            pk2 = pk2.split('*')
            print(pk1, pk2)
            s = ''
            for j in range(len(pk1)):
                a = '.filter(%s__icontains="%s")' % (pk1[j], pk2[j])
                s += a
            print(s)
            pg = MyPageNumberPagination()
            queryset = eval('GenericDrugData.objects%s' % s)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = GenericDrugDataSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            queryset = GenericDrugData.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = GenericDrugDataSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class InactiveIngredientSearchView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        pk1 = self.request.GET.get('pk1')
        if pk:
            pg = MyPageNumberPagination()
            queryset = InactiveIngredientSearch.objects.filter(
                Q(inactive_ingredient__icontains=pk) | Q(route__icontains=pk) | Q(
                    dosage_form__icontains=pk) | Q(
                    cas_number__icontains=pk) | Q(UNII__icontains=pk) | Q(
                    maximum_potency_per_unit_dose__icontains=pk))
            # | Q(
            #     record_updated__icontains=pk))
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = InactiveIngredientSearchSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        if pk1:
            pk2 = self.request.GET.get('pk2')
            pk1 = pk1.split('*')
            pk2 = pk2.split('*')
            print(pk1, pk2)
            s = ''
            for j in range(len(pk1)):
                a = '.filter(%s__icontains="%s")' % (pk1[j], pk2[j])
                s += a
            print(s)
            pg = MyPageNumberPagination()
            queryset = eval('InactiveIngredientSearch.objects%s' % s)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = InactiveIngredientSearchSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            queryset = InactiveIngredientSearch.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = InactiveIngredientSearchSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class FDAdrugView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        pk1 = self.request.GET.get('pk1')
        if pk:
            pg = MyPageNumberPagination()
            queryset = FDAdrug.objects.filter(
                Q(trade_name__icontains=pk) | Q(application_number__icontains=pk) | Q(
                    product_id__icontains=pk) | Q(
                    application_type__icontains=pk) | Q(active_ingredient__icontains=pk) | Q(
                    dosage_form_or_route_of_administration__icontains=pk) | Q(
                    specification_or_dosage__icontains=pk) | Q(RLD__icontains=pk) | Q(
                    RS__icontains=pk) | Q(application_No_original_or_tentative_approval_date__icontains=pk) | Q(
                    product_number_approval_date__icontains=pk) | Q(applicant__icontains=pk) | Q(
                    market_state__icontains=pk))
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAdrugSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        if pk1:
            pk2 = self.request.GET.get('pk2')
            pk1 = pk1.split('*')
            pk2 = pk2.split('*')
            print(pk1, pk2)
            s = ''
            for j in range(len(pk1)):
                a = '.filter(%s__icontains="%s")' % (pk1[j], pk2[j])
                s += a
            print(s)
            pg = MyPageNumberPagination()
            queryset = eval('FDAdrug.objects%s' % s)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAdrugSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            queryset = FDAdrug.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAdrugSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class FDAdrugOrangeBookView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        pk1 = self.request.GET.get('pk1')
        if pk:
            pg = MyPageNumberPagination()
            queryset = FDAdrugOrangeBook.objects.filter(
                Q(trade_name__icontains=pk) | Q(application_number__icontains=pk) | Q(
                    product_id__icontains=pk) | Q(
                    application_type__icontains=pk) | Q(active_ingredient__icontains=pk) | Q(
                    dosage_form_or_route_of_administration__icontains=pk) | Q(
                    specification_or_dosage__icontains=pk) | Q(reference_drug_or_not__icontains=pk) | Q(
                    bioequivalence_reference_standard_or_not__icontains=pk) | Q(
                    treatment_equivalent_code__icontains=pk) | Q(
                    product_batch_date__icontains=pk) | Q(applicant__icontains=pk) | Q(market_state__icontains=pk))
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAdrugOrangeBookSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        if pk1:
            pk2 = self.request.GET.get('pk2')
            pk1 = pk1.split('*')
            pk2 = pk2.split('*')
            print(pk1, pk2)
            s = ''
            for j in range(len(pk1)):
                a = '.filter(%s__icontains="%s")' % (pk1[j], pk2[j])
                s += a
            print(s)
            pg = MyPageNumberPagination()
            queryset = eval('FDAdrugOrangeBook.objects%s' % s)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAdrugOrangeBookSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            queryset = FDAdrugOrangeBook.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAdrugOrangeBookSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class ClinicalDataBigViewSet(DynamicModelViewSet):
    queryset = ClinicalDataBig.objects.all()
    serializer_class = ClinicalDataBigSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('url', 'other_study_id_numbers', 'trial_id', 'title', 'sponsor',
                     'agency_class', 'information_provider', 'brief_summary', 'detailed_description',
                     'recruitment_status', 'phase', 'study_type', 'intervention_model', 'study_design_primary_purpose',
                     'study_design_masking', 'target_disease', 'intervention_type', 'interventions', 'criteria',
                     'gender',
                     'minimum_age', 'maximum_age', 'healthy_volunteers', 'address', 'measure_outcome', 'study_design')
    filter_fields = ('url', 'other_study_id_numbers', 'trial_id', 'title', 'sponsor',
                     'agency_class', 'information_provider', 'brief_summary', 'detailed_description',
                     'recruitment_status', 'phase', 'study_type', 'intervention_model', 'study_design_primary_purpose',
                     'study_design_masking', 'target_disease', 'intervention_type', 'interventions', 'criteria',
                     'gender',
                     'minimum_age', 'maximum_age', 'healthy_volunteers', 'address', 'measure_outcome', 'study_design')
    ordering_fields = ('url', 'other_study_id_numbers', 'trial_id', 'title', 'sponsor',
                       'agency_class', 'information_provider', 'brief_summary', 'detailed_description',
                       'recruitment_status', 'phase', 'study_type', 'intervention_model',
                       'study_design_primary_purpose',
                       'study_design_masking', 'target_disease', 'intervention_type', 'interventions', 'criteria',
                       'gender',
                       'minimum_age', 'maximum_age', 'healthy_volunteers', 'address', 'measure_outcome', 'study_design')


class ClinicaldetailViewSet(DynamicModelViewSet):
    queryset = Clinicaldetail.objects.all().order_by('-date_of_registration')
    serializer_class = ClinicaldetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = (
        'main_id', 'last_refreshed_on', 'secondary_id', 'public_title', 'scientific_title', 'url',
        'study_type', 'study_design', 'phase', 'date_of_registration', 'date_of_first_enrolment',
        'target_sample_size',
        'recruitment_status', 'primary_sponsor', 'secondary_sponsor', 'source_of_monetary_support',
        'countries_of_recruitment', 'health_condition_or_problem_studied',
        'intervention',
        'age_minimum', 'age_maximum', 'gender',
        'key_inclusion_exclusion_criteria', 'primary_outcome', 'secondary_outcome')
    filter_fields = (
        'main_id', 'last_refreshed_on', 'secondary_id', 'public_title', 'scientific_title', 'url',
        'study_type', 'study_design', 'phase', 'date_of_registration', 'date_of_first_enrolment',
        'target_sample_size',
        'recruitment_status', 'primary_sponsor', 'secondary_sponsor', 'source_of_monetary_support',
        'countries_of_recruitment', 'health_condition_or_problem_studied',
        'intervention',
        'age_minimum', 'age_maximum', 'gender',
        'key_inclusion_exclusion_criteria', 'primary_outcome', 'secondary_outcome')
    ordering_fields = (
        'date_of_registration')


class ClinicalbrowseViewSet(DynamicModelViewSet):
    queryset = Clinicalbrowse.objects.all().order_by('-date_of_registration')
    serializer_class = ClinicalbrowseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = (
        'main_id', 'public_title', 'date_of_registration', 'recruitment_status')
    filter_fields = (
        'main_id', 'public_title', 'date_of_registration', 'recruitment_status')
    ordering_fields = (
        'date_of_registration')


class FDAPatentView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        print(pk)
        pk1 = self.request.GET.get('pk1')
        if pk:
            pg = MyPageNumberPagination()
            queryset = FDAPatent.objects.filter(
                Q(patent_number__icontains=pk) | Q(patent_link__icontains=pk) | Q(
                    patent_expiration_date__icontains=pk) | Q(
                    application_number__icontains=pk) | Q(product_id__icontains=pk) | Q(
                    trade_name__icontains=pk) | Q(
                    active_ingredient__icontains=pk) | Q(dosage_form__icontains=pk) | Q(
                    material_patent__icontains=pk) | Q(product_patent__icontains=pk) | Q(
                    use_patent__icontains=pk) | Q(detail_link__icontains=pk))
            print(queryset)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAPatentSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        if pk1:
            pk2 = self.request.GET.get('pk2')
            pk1 = pk1.split('*')
            pk2 = pk2.split('*')
            print(pk1, pk2)
            s = ''
            for j in range(len(pk1)):
                a = '.filter(%s__icontains="%s")' % (pk1[j], pk2[j])
                s += a
            print(s)
            pg = MyPageNumberPagination()
            queryset = eval('FDAPatent.objects%s' % s)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAPatentSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            queryset = FDAPatent.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = FDAPatentSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class ChemicalIndexView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        pk = self.request.GET.get('pk')
        print(pk)
        pk1 = self.request.GET.get('pk1')
        if pk:
            pg = MyPageNumberPagination()
            queryset = ChemicalIndex.objects.filter(
                Q(title__icontains=pk) | Q(CAS_registry_number__icontains=pk) | Q(
                    CAS_name__icontains=pk) | Q(
                    additional_names__icontains=pk) | Q(manufacturers_codes__icontains=pk) | Q(
                    molecular_formula__icontains=pk) | Q(
                    molecular_weight__icontains=pk) | Q(percent_composition__icontains=pk) | Q(
                    literature_references__icontains=pk) | Q(properties__icontains=pk) | Q(
                    melting_point__icontains=pk) | Q(pKa__icontains=pk) | Q(optical_rotation__icontains=pk) | Q(
                    logP__icontains=pk) | Q(absorption_maximum__icontains=pk) | Q(therap_cat__icontains=pk) | Q(
                    keywords__icontains=pk) | Q(toxicity_data__icontains=pk) | Q(derivative_type__icontains=pk) | Q(
                    derivativeCASRegistryNumber__icontains=pk) | Q(derivativeTrademarks__icontains=pk) | Q(
                    derivativeMolecularFormula__icontains=pk) | Q(derivativeMolecularWeight__icontains=pk) | Q(
                    derivativePercentComposition__icontains=pk))
            print(queryset)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = ChemicalIndexSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        if pk1:
            pk2 = self.request.GET.get('pk2')
            pk1 = pk1.split('*')
            pk2 = pk2.split('*')
            print(pk1, pk2)
            s = ''
            for j in range(len(pk1)):
                a = '.filter(%s__icontains="%s")' % (pk1[j], pk2[j])
                s += a
            print(s)
            pg = MyPageNumberPagination()
            queryset = eval('ChemicalIndex.objects%s' % s)
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = ChemicalIndexSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
        else:
            pg = MyPageNumberPagination()
            queryset = ChemicalIndex.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = ChemicalIndexSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
