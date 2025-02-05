"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets.date import DateTimeFacet
from oarepo_runtime.services.facets.nested_facet import NestedLabeledFacet
from oarepo_runtime.services.facets.year_histogram import YearAutoHistogramFacet
from oarepo_vocabularies.services.facets import (
    HierarchyVocabularyFacet,
    VocabularyFacet,
)

from nr_metadata.services.records.facets import KeywordsFacet

metadata_abstract_cs = TermsFacet(
    field="metadata.abstract.cs.keyword", label=_("metadata/abstract.label")
)

metadata_abstract_en = TermsFacet(
    field="metadata.abstract.en.keyword", label=_("metadata/abstract.label")
)

metadata_abstract_lang = NestedLabeledFacet(
    path="metadata.abstract",
    nested_facet=TermsFacet(
        field="metadata.abstract.lang", label=_("metadata/abstract/lang.label")
    ),
)

metadata_accessRights = VocabularyFacet(
    field="metadata.accessRights",
    label=_("metadata/accessRights.label"),
    vocabulary="access-rights",
)

metadata_accessibility_cs = TermsFacet(
    field="metadata.accessibility.cs.keyword", label=_("metadata/accessibility.label")
)

metadata_accessibility_en = TermsFacet(
    field="metadata.accessibility.en.keyword", label=_("metadata/accessibility.label")
)

metadata_accessibility_lang = NestedLabeledFacet(
    path="metadata.accessibility",
    nested_facet=TermsFacet(
        field="metadata.accessibility.lang",
        label=_("metadata/accessibility/lang.label"),
    ),
)

metadata_additionalTitles_title_cs = TermsFacet(
    field="metadata.additionalTitles.title.cs.keyword",
    label=_("metadata/additionalTitles/title.label"),
)

metadata_additionalTitles_title_en = TermsFacet(
    field="metadata.additionalTitles.title.en.keyword",
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

metadata_contributors_affiliations = HierarchyVocabularyFacet(
    field="metadata.contributors.affiliations",
    label=_("metadata/contributors/affiliations.label"),
    vocabulary="institutions",
)

metadata_contributors_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.contributors.authorityIdentifiers.identifier",
    label=_("metadata/contributors/authorityIdentifiers/identifier.label"),
)

metadata_contributors_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.contributors.authorityIdentifiers.scheme",
    label=_("metadata/contributors/authorityIdentifiers/scheme.label"),
)

metadata_contributors_contributorType = VocabularyFacet(
    field="metadata.contributors.contributorType",
    label=_("metadata/contributors/contributorType.label"),
    vocabulary="contributor-types",
)

metadata_contributors_familyName = TermsFacet(
    field="metadata.contributors.familyName",
    label=_("metadata/contributors/familyName.label"),
)

metadata_contributors_fullName = TermsFacet(
    field="metadata.contributors.fullName",
    label=_("metadata/contributors/fullName.label"),
)

metadata_contributors_givenName = TermsFacet(
    field="metadata.contributors.givenName",
    label=_("metadata/contributors/givenName.label"),
)

metadata_contributors_nameType = TermsFacet(
    field="metadata.contributors.nameType",
    label=_("metadata/contributors/nameType.label"),
)

metadata_creators_affiliations = HierarchyVocabularyFacet(
    field="metadata.creators.affiliations",
    label=_("metadata/creators/affiliations.label"),
    vocabulary="institutions",
)

metadata_creators_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.creators.authorityIdentifiers.identifier",
    label=_("metadata/creators/authorityIdentifiers/identifier.label"),
)

metadata_creators_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.creators.authorityIdentifiers.scheme",
    label=_("metadata/creators/authorityIdentifiers/scheme.label"),
)

metadata_creators_familyName = TermsFacet(
    field="metadata.creators.familyName", label=_("metadata/creators/familyName.label")
)

metadata_creators_fullName = TermsFacet(
    field="metadata.creators.fullName", label=_("metadata/creators/fullName.label")
)

metadata_creators_givenName = TermsFacet(
    field="metadata.creators.givenName", label=_("metadata/creators/givenName.label")
)

metadata_creators_nameType = TermsFacet(
    field="metadata.creators.nameType", label=_("metadata/creators/nameType.label")
)

metadata_dateAvailable = DateTimeFacet(
    field="metadata.dateAvailable", label=_("metadata/dateAvailable.label")
)

metadata_dateIssued = DateTimeFacet(
    field="metadata.dateIssued", label=_("metadata/dateIssued.label")
)

metadata_dateModified = DateTimeFacet(
    field="metadata.dateModified", label=_("metadata/dateModified.label")
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

metadata_externalLocation_externalLocationURL = TermsFacet(
    field="metadata.externalLocation.externalLocationURL",
    label=_("metadata/externalLocation/externalLocationURL.label"),
)

metadata_fundingReferences_funder = VocabularyFacet(
    field="metadata.fundingReferences.funder",
    label=_("metadata/fundingReferences/funder.label"),
    vocabulary="funders",
)

metadata_fundingReferences_projectID = TermsFacet(
    field="metadata.fundingReferences.projectID",
    label=_("metadata/fundingReferences/projectID.label"),
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
    field="metadata.methods.cs.keyword", label=_("metadata/methods.label")
)

metadata_methods_en = TermsFacet(
    field="metadata.methods.en.keyword", label=_("metadata/methods.label")
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

metadata_relatedItems_itemContributors_affiliations = HierarchyVocabularyFacet(
    field="metadata.relatedItems.itemContributors.affiliations",
    label=_("metadata/relatedItems/itemContributors/affiliations.label"),
    vocabulary="institutions",
)

metadata_relatedItems_itemContributors_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.relatedItems.itemContributors.authorityIdentifiers.identifier",
    label=_(
        "metadata/relatedItems/itemContributors/authorityIdentifiers/identifier.label"
    ),
)

metadata_relatedItems_itemContributors_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.relatedItems.itemContributors.authorityIdentifiers.scheme",
    label=_("metadata/relatedItems/itemContributors/authorityIdentifiers/scheme.label"),
)

metadata_relatedItems_itemContributors_contributorType = VocabularyFacet(
    field="metadata.relatedItems.itemContributors.contributorType",
    label=_("metadata/relatedItems/itemContributors/contributorType.label"),
    vocabulary="contributor-types",
)

metadata_relatedItems_itemContributors_familyName = TermsFacet(
    field="metadata.relatedItems.itemContributors.familyName",
    label=_("metadata/relatedItems/itemContributors/familyName.label"),
)

metadata_relatedItems_itemContributors_fullName = TermsFacet(
    field="metadata.relatedItems.itemContributors.fullName",
    label=_("metadata/relatedItems/itemContributors/fullName.label"),
)

metadata_relatedItems_itemContributors_givenName = TermsFacet(
    field="metadata.relatedItems.itemContributors.givenName",
    label=_("metadata/relatedItems/itemContributors/givenName.label"),
)

metadata_relatedItems_itemContributors_nameType = TermsFacet(
    field="metadata.relatedItems.itemContributors.nameType",
    label=_("metadata/relatedItems/itemContributors/nameType.label"),
)

metadata_relatedItems_itemCreators_affiliations = HierarchyVocabularyFacet(
    field="metadata.relatedItems.itemCreators.affiliations",
    label=_("metadata/relatedItems/itemCreators/affiliations.label"),
    vocabulary="institutions",
)

metadata_relatedItems_itemCreators_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.relatedItems.itemCreators.authorityIdentifiers.identifier",
    label=_("metadata/relatedItems/itemCreators/authorityIdentifiers/identifier.label"),
)

metadata_relatedItems_itemCreators_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.relatedItems.itemCreators.authorityIdentifiers.scheme",
    label=_("metadata/relatedItems/itemCreators/authorityIdentifiers/scheme.label"),
)

metadata_relatedItems_itemCreators_familyName = TermsFacet(
    field="metadata.relatedItems.itemCreators.familyName",
    label=_("metadata/relatedItems/itemCreators/familyName.label"),
)

metadata_relatedItems_itemCreators_fullName = TermsFacet(
    field="metadata.relatedItems.itemCreators.fullName",
    label=_("metadata/relatedItems/itemCreators/fullName.label"),
)

metadata_relatedItems_itemCreators_givenName = TermsFacet(
    field="metadata.relatedItems.itemCreators.givenName",
    label=_("metadata/relatedItems/itemCreators/givenName.label"),
)

metadata_relatedItems_itemCreators_nameType = TermsFacet(
    field="metadata.relatedItems.itemCreators.nameType",
    label=_("metadata/relatedItems/itemCreators/nameType.label"),
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
    field="metadata.subjects.subject.cs.keyword",
    label=_("metadata/subjects/subject.label"),
)

metadata_subjects_subject_en = TermsFacet(
    field="metadata.subjects.subject.en.keyword",
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
    field="metadata.technicalInfo.cs.keyword", label=_("metadata/technicalInfo.label")
)

metadata_technicalInfo_en = TermsFacet(
    field="metadata.technicalInfo.en.keyword", label=_("metadata/technicalInfo.label")
)

metadata_technicalInfo_lang = NestedLabeledFacet(
    path="metadata.technicalInfo",
    nested_facet=TermsFacet(
        field="metadata.technicalInfo.lang",
        label=_("metadata/technicalInfo/lang.label"),
    ),
)

metadata_thesis_dateDefended = DateTimeFacet(
    field="metadata.thesis.dateDefended", label=_("metadata/thesis/dateDefended.label")
)

metadata_thesis_defended = TermsFacet(
    field="metadata.thesis.defended", label=_("metadata/thesis/defended.label")
)

metadata_thesis_degreeGrantors = HierarchyVocabularyFacet(
    field="metadata.thesis.degreeGrantors",
    label=_("metadata/thesis/degreeGrantors.label"),
    vocabulary="institutions",
)

metadata_thesis_studyFields = TermsFacet(
    field="metadata.thesis.studyFields", label=_("metadata/thesis/studyFields.label")
)

metadata_version = TermsFacet(
    field="metadata.version", label=_("metadata/version.label")
)

syntheticFields_date = DateTimeFacet(
    field="syntheticFields.date", label=_("syntheticFields/date.label")
)

syntheticFields_defenseYear = YearAutoHistogramFacet(
    field="syntheticFields.defenseYear", label=_("syntheticFields/defenseYear.label")
)

syntheticFields_keywords = KeywordsFacet(
    field="syntheticFields.keywords", label=_("syntheticFields/keywords.label")
)

syntheticFields_organizations = TermsFacet(
    field="syntheticFields.organizations",
    label=_("syntheticFields/organizations.label"),
)

syntheticFields_people = TermsFacet(
    field="syntheticFields.people", label=_("syntheticFields/people.label")
)

syntheticFields_year = YearAutoHistogramFacet(
    field="syntheticFields.year", label=_("syntheticFields/year.label")
)
