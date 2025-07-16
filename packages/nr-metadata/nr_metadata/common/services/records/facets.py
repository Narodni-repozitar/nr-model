"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets import MultilingualFacet
from oarepo_runtime.services.facets.date import DateTimeFacet
from oarepo_runtime.services.facets.nested_facet import NestedLabeledFacet
from oarepo_vocabularies.services.facets import VocabularyFacet

record_status = TermsFacet(field="record_status", label=_("record_status"))

has_draft = TermsFacet(field="has_draft", label=_("has_draft"))

expires_at = DateTimeFacet(field="expires_at", label=_("expires_at.label"))

fork_version_id = TermsFacet(field="fork_version_id", label=_("fork_version_id.label"))

access_embargo_active = TermsFacet(
    field="access.embargo.active", label=_("access/embargo/active.label")
)

access_embargo_until = DateTimeFacet(
    field="access.embargo.until", label=_("access/embargo/until.label")
)

access_files = TermsFacet(field="access.files", label=_("access/files.label"))

access_record = TermsFacet(field="access.record", label=_("access/record.label"))

access_status = TermsFacet(field="access.status", label=_("access/status.label"))

metadata_abstract_cs = TermsFacet(
    field="metadata.abstract_cs.keyword", label=_("metadata/abstract.label")
)

metadata_abstract_en = TermsFacet(
    field="metadata.abstract_en.keyword", label=_("metadata/abstract.label")
)

metadata_abstract = MultilingualFacet(
    lang_facets={"cs": metadata_abstract_cs, "en": metadata_abstract_en},
    label=_("metadata/abstract.label"),
)

metadata_abstract_lang = NestedLabeledFacet(
    path="metadata.abstract",
    nested_facet=TermsFacet(
        field="metadata.abstract.lang", label=_("metadata/abstract/lang.label")
    ),
)

metadata_accessibility_cs = TermsFacet(
    field="metadata.accessibility_cs.keyword", label=_("metadata/accessibility.label")
)

metadata_accessibility_en = TermsFacet(
    field="metadata.accessibility_en.keyword", label=_("metadata/accessibility.label")
)

metadata_accessibility = MultilingualFacet(
    lang_facets={"cs": metadata_accessibility_cs, "en": metadata_accessibility_en},
    label=_("metadata/accessibility.label"),
)

metadata_accessibility_lang = NestedLabeledFacet(
    path="metadata.accessibility",
    nested_facet=TermsFacet(
        field="metadata.accessibility.lang",
        label=_("metadata/accessibility/lang.label"),
    ),
)

metadata_additionalTitles_title_cs = TermsFacet(
    field="metadata.additionalTitles.title_cs.keyword",
    label=_("metadata/additionalTitles/title.label"),
)

metadata_additionalTitles_title_en = TermsFacet(
    field="metadata.additionalTitles.title_en.keyword",
    label=_("metadata/additionalTitles/title.label"),
)

metadata_additionalTitles_title = MultilingualFacet(
    lang_facets={
        "cs": metadata_additionalTitles_title_cs,
        "en": metadata_additionalTitles_title_en,
    },
    label=_("metadata/additionalTitles/title.label"),
)

metadata_additionalTitles_title_lang = NestedLabeledFacet(
    path="metadata.additionalTitles.title",
    nested_facet=TermsFacet(
        field="metadata.additionalTitles.title.lang",
        label=_("metadata/additionalTitles/title/lang.label"),
    ),
)

metadata_additionalTitles_titleType = TermsFacet(
    field="metadata.additionalTitles.titleType",
    label=_("metadata/additionalTitles/titleType.label"),
)

metadata_contributors_affiliations = VocabularyFacet(
    field="metadata.contributors.affiliations",
    label=_("metadata/contributors/affiliations.label"),
    vocabulary="affiliations",
)

metadata_contributors_person_or_org_family_name = TermsFacet(
    field="metadata.contributors.person_or_org.family_name",
    label=_("metadata/contributors/person_or_org/family_name.label"),
)

metadata_contributors_person_or_org_given_name = TermsFacet(
    field="metadata.contributors.person_or_org.given_name",
    label=_("metadata/contributors/person_or_org/given_name.label"),
)

metadata_contributors_person_or_org_identifiers_identifier = TermsFacet(
    field="metadata.contributors.person_or_org.identifiers.identifier",
    label=_("metadata/contributors/person_or_org/identifiers/identifier.label"),
)

metadata_contributors_person_or_org_identifiers_scheme = TermsFacet(
    field="metadata.contributors.person_or_org.identifiers.scheme",
    label=_("metadata/contributors/person_or_org/identifiers/scheme.label"),
)

metadata_contributors_person_or_org_name = TermsFacet(
    field="metadata.contributors.person_or_org.name",
    label=_("metadata/contributors/person_or_org/name.label"),
)

metadata_contributors_person_or_org_type = TermsFacet(
    field="metadata.contributors.person_or_org.type",
    label=_("metadata/contributors/person_or_org/type.label"),
)

metadata_contributors_role = VocabularyFacet(
    field="metadata.contributors.role",
    label=_("metadata/contributors/role.label"),
    vocabulary="contributor-types",
)

metadata_creators_affiliations = VocabularyFacet(
    field="metadata.creators.affiliations",
    label=_("metadata/creators/affiliations.label"),
    vocabulary="affiliations",
)

metadata_creators_person_or_org_family_name = TermsFacet(
    field="metadata.creators.person_or_org.family_name",
    label=_("metadata/creators/person_or_org/family_name.label"),
)

metadata_creators_person_or_org_given_name = TermsFacet(
    field="metadata.creators.person_or_org.given_name",
    label=_("metadata/creators/person_or_org/given_name.label"),
)

metadata_creators_person_or_org_identifiers_identifier = TermsFacet(
    field="metadata.creators.person_or_org.identifiers.identifier",
    label=_("metadata/creators/person_or_org/identifiers/identifier.label"),
)

metadata_creators_person_or_org_identifiers_scheme = TermsFacet(
    field="metadata.creators.person_or_org.identifiers.scheme",
    label=_("metadata/creators/person_or_org/identifiers/scheme.label"),
)

metadata_creators_person_or_org_name = TermsFacet(
    field="metadata.creators.person_or_org.name",
    label=_("metadata/creators/person_or_org/name.label"),
)

metadata_creators_person_or_org_type = TermsFacet(
    field="metadata.creators.person_or_org.type",
    label=_("metadata/creators/person_or_org/type.label"),
)

metadata_creators_role = VocabularyFacet(
    field="metadata.creators.role",
    label=_("metadata/creators/role.label"),
    vocabulary="contributor-types",
)

metadata_dateAvailable = DateTimeFacet(
    field="metadata.dateAvailable", label=_("metadata/dateAvailable.label")
)

metadata_dateIssued = DateTimeFacet(
    field="metadata.dateIssued", label=_("metadata/dateIssued.label")
)

metadata_events_eventLocation_country = VocabularyFacet(
    field="metadata.events.eventLocation.country",
    label=_("metadata/events/eventLocation/country.label"),
    vocabulary="countries",
)

metadata_events_eventLocation_place = TermsFacet(
    field="metadata.events.eventLocation.place",
    label=_("metadata/events/eventLocation/place.label"),
)

metadata_funders_award = VocabularyFacet(
    field="metadata.funders.award",
    label=_("metadata/funders/award.label"),
    vocabulary="awards",
)

metadata_funders_funder = VocabularyFacet(
    field="metadata.funders.funder",
    label=_("metadata/funders/funder.label"),
    vocabulary="funders",
)

metadata_geoLocations_geoLocationPlace = TermsFacet(
    field="metadata.geoLocations.geoLocationPlace",
    label=_("metadata/geoLocations/geoLocationPlace.label"),
)

metadata_geoLocations_geoLocationPoint_pointLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPoint.pointLatitude",
    label=_("metadata/geoLocations/geoLocationPoint/pointLatitude.label"),
)

metadata_geoLocations_geoLocationPoint_pointLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPoint.pointLongitude",
    label=_("metadata/geoLocations/geoLocationPoint/pointLongitude.label"),
)

metadata_languages = VocabularyFacet(
    field="metadata.languages",
    label=_("metadata/languages.label"),
    vocabulary="languages",
)

metadata_methods_cs = TermsFacet(
    field="metadata.methods_cs.keyword", label=_("metadata/methods.label")
)

metadata_methods_en = TermsFacet(
    field="metadata.methods_en.keyword", label=_("metadata/methods.label")
)

metadata_methods = MultilingualFacet(
    lang_facets={"cs": metadata_methods_cs, "en": metadata_methods_en},
    label=_("metadata/methods.label"),
)

metadata_methods_lang = NestedLabeledFacet(
    path="metadata.methods",
    nested_facet=TermsFacet(
        field="metadata.methods.lang", label=_("metadata/methods/lang.label")
    ),
)

metadata_objectIdentifiers_identifier = TermsFacet(
    field="metadata.objectIdentifiers.identifier",
    label=_("metadata/objectIdentifiers/identifier.label"),
)

metadata_objectIdentifiers_scheme = TermsFacet(
    field="metadata.objectIdentifiers.scheme",
    label=_("metadata/objectIdentifiers/scheme.label"),
)

metadata_originalRecord = TermsFacet(
    field="metadata.originalRecord", label=_("metadata/originalRecord.label")
)

metadata_relatedItems_itemContributors_affiliations = VocabularyFacet(
    field="metadata.relatedItems.itemContributors.affiliations",
    label=_("metadata/relatedItems/itemContributors/affiliations.label"),
    vocabulary="affiliations",
)

metadata_relatedItems_itemContributors_person_or_org_family_name = TermsFacet(
    field="metadata.relatedItems.itemContributors.person_or_org.family_name",
    label=_("metadata/relatedItems/itemContributors/person_or_org/family_name.label"),
)

metadata_relatedItems_itemContributors_person_or_org_given_name = TermsFacet(
    field="metadata.relatedItems.itemContributors.person_or_org.given_name",
    label=_("metadata/relatedItems/itemContributors/person_or_org/given_name.label"),
)

metadata_relatedItems_itemContributors_person_or_org_identifiers_identifier = TermsFacet(
    field="metadata.relatedItems.itemContributors.person_or_org.identifiers.identifier",
    label=_(
        "metadata/relatedItems/itemContributors/person_or_org/identifiers/identifier.label"
    ),
)

metadata_relatedItems_itemContributors_person_or_org_identifiers_scheme = TermsFacet(
    field="metadata.relatedItems.itemContributors.person_or_org.identifiers.scheme",
    label=_(
        "metadata/relatedItems/itemContributors/person_or_org/identifiers/scheme.label"
    ),
)

metadata_relatedItems_itemContributors_person_or_org_name = TermsFacet(
    field="metadata.relatedItems.itemContributors.person_or_org.name",
    label=_("metadata/relatedItems/itemContributors/person_or_org/name.label"),
)

metadata_relatedItems_itemContributors_person_or_org_type = TermsFacet(
    field="metadata.relatedItems.itemContributors.person_or_org.type",
    label=_("metadata/relatedItems/itemContributors/person_or_org/type.label"),
)

metadata_relatedItems_itemContributors_role = VocabularyFacet(
    field="metadata.relatedItems.itemContributors.role",
    label=_("metadata/relatedItems/itemContributors/role.label"),
    vocabulary="contributor-types",
)

metadata_relatedItems_itemCreators_affiliations = VocabularyFacet(
    field="metadata.relatedItems.itemCreators.affiliations",
    label=_("metadata/relatedItems/itemCreators/affiliations.label"),
    vocabulary="affiliations",
)

metadata_relatedItems_itemCreators_person_or_org_family_name = TermsFacet(
    field="metadata.relatedItems.itemCreators.person_or_org.family_name",
    label=_("metadata/relatedItems/itemCreators/person_or_org/family_name.label"),
)

metadata_relatedItems_itemCreators_person_or_org_given_name = TermsFacet(
    field="metadata.relatedItems.itemCreators.person_or_org.given_name",
    label=_("metadata/relatedItems/itemCreators/person_or_org/given_name.label"),
)

metadata_relatedItems_itemCreators_person_or_org_identifiers_identifier = TermsFacet(
    field="metadata.relatedItems.itemCreators.person_or_org.identifiers.identifier",
    label=_(
        "metadata/relatedItems/itemCreators/person_or_org/identifiers/identifier.label"
    ),
)

metadata_relatedItems_itemCreators_person_or_org_identifiers_scheme = TermsFacet(
    field="metadata.relatedItems.itemCreators.person_or_org.identifiers.scheme",
    label=_(
        "metadata/relatedItems/itemCreators/person_or_org/identifiers/scheme.label"
    ),
)

metadata_relatedItems_itemCreators_person_or_org_name = TermsFacet(
    field="metadata.relatedItems.itemCreators.person_or_org.name",
    label=_("metadata/relatedItems/itemCreators/person_or_org/name.label"),
)

metadata_relatedItems_itemCreators_person_or_org_type = TermsFacet(
    field="metadata.relatedItems.itemCreators.person_or_org.type",
    label=_("metadata/relatedItems/itemCreators/person_or_org/type.label"),
)

metadata_relatedItems_itemCreators_role = VocabularyFacet(
    field="metadata.relatedItems.itemCreators.role",
    label=_("metadata/relatedItems/itemCreators/role.label"),
    vocabulary="contributor-types",
)

metadata_relatedItems_itemEndPage = TermsFacet(
    field="metadata.relatedItems.itemEndPage",
    label=_("metadata/relatedItems/itemEndPage.label"),
)

metadata_relatedItems_itemIssue = TermsFacet(
    field="metadata.relatedItems.itemIssue",
    label=_("metadata/relatedItems/itemIssue.label"),
)

metadata_relatedItems_itemPIDs_identifier = TermsFacet(
    field="metadata.relatedItems.itemPIDs.identifier",
    label=_("metadata/relatedItems/itemPIDs/identifier.label"),
)

metadata_relatedItems_itemPIDs_scheme = TermsFacet(
    field="metadata.relatedItems.itemPIDs.scheme",
    label=_("metadata/relatedItems/itemPIDs/scheme.label"),
)

metadata_relatedItems_itemPublisher = TermsFacet(
    field="metadata.relatedItems.itemPublisher",
    label=_("metadata/relatedItems/itemPublisher.label"),
)

metadata_relatedItems_itemRelationType = VocabularyFacet(
    field="metadata.relatedItems.itemRelationType",
    label=_("metadata/relatedItems/itemRelationType.label"),
    vocabulary="item-relation-types",
)

metadata_relatedItems_itemResourceType = VocabularyFacet(
    field="metadata.relatedItems.itemResourceType",
    label=_("metadata/relatedItems/itemResourceType.label"),
    vocabulary="resource-types",
)

metadata_relatedItems_itemStartPage = TermsFacet(
    field="metadata.relatedItems.itemStartPage",
    label=_("metadata/relatedItems/itemStartPage.label"),
)

metadata_relatedItems_itemURL = TermsFacet(
    field="metadata.relatedItems.itemURL",
    label=_("metadata/relatedItems/itemURL.label"),
)

metadata_relatedItems_itemVolume = TermsFacet(
    field="metadata.relatedItems.itemVolume",
    label=_("metadata/relatedItems/itemVolume.label"),
)

metadata_relatedItems_itemYear = TermsFacet(
    field="metadata.relatedItems.itemYear",
    label=_("metadata/relatedItems/itemYear.label"),
)

metadata_resourceType = VocabularyFacet(
    field="metadata.resourceType",
    label=_("metadata/resourceType.label"),
    vocabulary="resource-types",
)

metadata_rights = VocabularyFacet(
    field="metadata.rights", label=_("metadata/rights.label"), vocabulary="rights"
)

metadata_series_seriesTitle = TermsFacet(
    field="metadata.series.seriesTitle", label=_("metadata/series/seriesTitle.label")
)

metadata_series_seriesVolume = TermsFacet(
    field="metadata.series.seriesVolume", label=_("metadata/series/seriesVolume.label")
)

metadata_subjectCategories = VocabularyFacet(
    field="metadata.subjectCategories",
    label=_("metadata/subjectCategories.label"),
    vocabulary="subject-categories",
)

metadata_subjects_classificationCode = TermsFacet(
    field="metadata.subjects.classificationCode",
    label=_("metadata/subjects/classificationCode.label"),
)

metadata_subjects_subject_cs = TermsFacet(
    field="metadata.subjects.subject_cs.keyword",
    label=_("metadata/subjects/subject.label"),
)

metadata_subjects_subject_en = TermsFacet(
    field="metadata.subjects.subject_en.keyword",
    label=_("metadata/subjects/subject.label"),
)

metadata_subjects_subject = MultilingualFacet(
    lang_facets={
        "cs": metadata_subjects_subject_cs,
        "en": metadata_subjects_subject_en,
    },
    label=_("metadata/subjects/subject.label"),
)

metadata_subjects_subject_lang = NestedLabeledFacet(
    path="metadata.subjects.subject",
    nested_facet=TermsFacet(
        field="metadata.subjects.subject.lang",
        label=_("metadata/subjects/subject/lang.label"),
    ),
)

metadata_subjects_subjectScheme = TermsFacet(
    field="metadata.subjects.subjectScheme",
    label=_("metadata/subjects/subjectScheme.label"),
)

metadata_subjects_valueURI = TermsFacet(
    field="metadata.subjects.valueURI", label=_("metadata/subjects/valueURI.label")
)

metadata_systemIdentifiers_identifier = TermsFacet(
    field="metadata.systemIdentifiers.identifier",
    label=_("metadata/systemIdentifiers/identifier.label"),
)

metadata_systemIdentifiers_scheme = TermsFacet(
    field="metadata.systemIdentifiers.scheme",
    label=_("metadata/systemIdentifiers/scheme.label"),
)

metadata_technicalInfo_cs = TermsFacet(
    field="metadata.technicalInfo_cs.keyword", label=_("metadata/technicalInfo.label")
)

metadata_technicalInfo_en = TermsFacet(
    field="metadata.technicalInfo_en.keyword", label=_("metadata/technicalInfo.label")
)

metadata_technicalInfo = MultilingualFacet(
    lang_facets={"cs": metadata_technicalInfo_cs, "en": metadata_technicalInfo_en},
    label=_("metadata/technicalInfo.label"),
)

metadata_technicalInfo_lang = NestedLabeledFacet(
    path="metadata.technicalInfo",
    nested_facet=TermsFacet(
        field="metadata.technicalInfo.lang",
        label=_("metadata/technicalInfo/lang.label"),
    ),
)

metadata_version = TermsFacet(
    field="metadata.version", label=_("metadata/version.label")
)

state = TermsFacet(field="state", label=_("state.label"))

state_timestamp = DateTimeFacet(
    field="state_timestamp", label=_("state_timestamp.label")
)
