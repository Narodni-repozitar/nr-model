from oarepo_runtime.services.search import I18nRDMSearchOptions

from . import facets


class DataSearchOptions(I18nRDMSearchOptions):
    """DataRecord search options."""

    facet_groups = {}

    facets = {
        **getattr(I18nRDMSearchOptions, "facets", {}),
        "record_status": facets.record_status,
        "has_draft": facets.has_draft,
        "expires_at": facets.expires_at,
        "fork_version_id": facets.fork_version_id,
        "access_embargo_active": facets.access_embargo_active,
        "access_embargo_until": facets.access_embargo_until,
        "access_files": facets.access_files,
        "access_record": facets.access_record,
        "access_status": facets.access_status,
        "metadata_abstract_cs": facets.metadata_abstract_cs,
        "metadata_abstract_en": facets.metadata_abstract_en,
        "metadata_abstract": facets.metadata_abstract,
        "metadata_abstract_lang": facets.metadata_abstract_lang,
        "metadata_accessibility_cs": facets.metadata_accessibility_cs,
        "metadata_accessibility_en": facets.metadata_accessibility_en,
        "metadata_accessibility": facets.metadata_accessibility,
        "metadata_accessibility_lang": facets.metadata_accessibility_lang,
        "metadata_additionalTitles_title_cs": facets.metadata_additionalTitles_title_cs,
        "metadata_additionalTitles_title_en": facets.metadata_additionalTitles_title_en,
        "metadata_additionalTitles_title": facets.metadata_additionalTitles_title,
        "metadata_additionalTitles_title_lang": (
            facets.metadata_additionalTitles_title_lang
        ),
        "metadata_additionalTitles_titleType": (
            facets.metadata_additionalTitles_titleType
        ),
        "metadata_contributors_affiliations": facets.metadata_contributors_affiliations,
        "metadata_contributors_person_or_org_family_name": (
            facets.metadata_contributors_person_or_org_family_name
        ),
        "metadata_contributors_person_or_org_given_name": (
            facets.metadata_contributors_person_or_org_given_name
        ),
        "metadata_contributors_person_or_org_identifiers_identifier": (
            facets.metadata_contributors_person_or_org_identifiers_identifier
        ),
        "metadata_contributors_person_or_org_identifiers_scheme": (
            facets.metadata_contributors_person_or_org_identifiers_scheme
        ),
        "metadata_contributors_person_or_org_name": (
            facets.metadata_contributors_person_or_org_name
        ),
        "metadata_contributors_person_or_org_type": (
            facets.metadata_contributors_person_or_org_type
        ),
        "metadata_contributors_role": facets.metadata_contributors_role,
        "metadata_creators_affiliations": facets.metadata_creators_affiliations,
        "metadata_creators_person_or_org_family_name": (
            facets.metadata_creators_person_or_org_family_name
        ),
        "metadata_creators_person_or_org_given_name": (
            facets.metadata_creators_person_or_org_given_name
        ),
        "metadata_creators_person_or_org_identifiers_identifier": (
            facets.metadata_creators_person_or_org_identifiers_identifier
        ),
        "metadata_creators_person_or_org_identifiers_scheme": (
            facets.metadata_creators_person_or_org_identifiers_scheme
        ),
        "metadata_creators_person_or_org_name": (
            facets.metadata_creators_person_or_org_name
        ),
        "metadata_creators_person_or_org_type": (
            facets.metadata_creators_person_or_org_type
        ),
        "metadata_creators_role": facets.metadata_creators_role,
        "metadata_dateAvailable": facets.metadata_dateAvailable,
        "metadata_dateIssued": facets.metadata_dateIssued,
        "metadata_dateValidTo": facets.metadata_dateValidTo,
        "metadata_dateWithdrawn_dateInformation": (
            facets.metadata_dateWithdrawn_dateInformation
        ),
        "metadata_dateWithdrawn_type": facets.metadata_dateWithdrawn_type,
        "metadata_events_eventLocation_country": (
            facets.metadata_events_eventLocation_country
        ),
        "metadata_events_eventLocation_place": (
            facets.metadata_events_eventLocation_place
        ),
        "metadata_funders_award": facets.metadata_funders_award,
        "metadata_funders_funder": facets.metadata_funders_funder,
        "metadata_geoLocations_geoLocationPlace": (
            facets.metadata_geoLocations_geoLocationPlace
        ),
        "metadata_geoLocations_geoLocationPoint_pointLatitude": (
            facets.metadata_geoLocations_geoLocationPoint_pointLatitude
        ),
        "metadata_geoLocations_geoLocationPoint_pointLongitude": (
            facets.metadata_geoLocations_geoLocationPoint_pointLongitude
        ),
        "metadata_languages": facets.metadata_languages,
        "metadata_methods_cs": facets.metadata_methods_cs,
        "metadata_methods_en": facets.metadata_methods_en,
        "metadata_methods": facets.metadata_methods,
        "metadata_methods_lang": facets.metadata_methods_lang,
        "metadata_objectIdentifiers_identifier": (
            facets.metadata_objectIdentifiers_identifier
        ),
        "metadata_objectIdentifiers_scheme": facets.metadata_objectIdentifiers_scheme,
        "metadata_originalRecord": facets.metadata_originalRecord,
        "metadata_publishers": facets.metadata_publishers,
        "metadata_relatedItems_itemContributors_affiliations": (
            facets.metadata_relatedItems_itemContributors_affiliations
        ),
        "metadata_relatedItems_itemContributors_person_or_org_family_name": (
            facets.metadata_relatedItems_itemContributors_person_or_org_family_name
        ),
        "metadata_relatedItems_itemContributors_person_or_org_given_name": (
            facets.metadata_relatedItems_itemContributors_person_or_org_given_name
        ),
        "metadata_relatedItems_itemContributors_person_or_org_identifiers_identifier": (
            facets.metadata_relatedItems_itemContributors_person_or_org_identifiers_identifier
        ),
        "metadata_relatedItems_itemContributors_person_or_org_identifiers_scheme": (
            facets.metadata_relatedItems_itemContributors_person_or_org_identifiers_scheme
        ),
        "metadata_relatedItems_itemContributors_person_or_org_name": (
            facets.metadata_relatedItems_itemContributors_person_or_org_name
        ),
        "metadata_relatedItems_itemContributors_person_or_org_type": (
            facets.metadata_relatedItems_itemContributors_person_or_org_type
        ),
        "metadata_relatedItems_itemContributors_role": (
            facets.metadata_relatedItems_itemContributors_role
        ),
        "metadata_relatedItems_itemCreators_affiliations": (
            facets.metadata_relatedItems_itemCreators_affiliations
        ),
        "metadata_relatedItems_itemCreators_person_or_org_family_name": (
            facets.metadata_relatedItems_itemCreators_person_or_org_family_name
        ),
        "metadata_relatedItems_itemCreators_person_or_org_given_name": (
            facets.metadata_relatedItems_itemCreators_person_or_org_given_name
        ),
        "metadata_relatedItems_itemCreators_person_or_org_identifiers_identifier": (
            facets.metadata_relatedItems_itemCreators_person_or_org_identifiers_identifier
        ),
        "metadata_relatedItems_itemCreators_person_or_org_identifiers_scheme": (
            facets.metadata_relatedItems_itemCreators_person_or_org_identifiers_scheme
        ),
        "metadata_relatedItems_itemCreators_person_or_org_name": (
            facets.metadata_relatedItems_itemCreators_person_or_org_name
        ),
        "metadata_relatedItems_itemCreators_person_or_org_type": (
            facets.metadata_relatedItems_itemCreators_person_or_org_type
        ),
        "metadata_relatedItems_itemCreators_role": (
            facets.metadata_relatedItems_itemCreators_role
        ),
        "metadata_relatedItems_itemEndPage": facets.metadata_relatedItems_itemEndPage,
        "metadata_relatedItems_itemIssue": facets.metadata_relatedItems_itemIssue,
        "metadata_relatedItems_itemPIDs_identifier": (
            facets.metadata_relatedItems_itemPIDs_identifier
        ),
        "metadata_relatedItems_itemPIDs_scheme": (
            facets.metadata_relatedItems_itemPIDs_scheme
        ),
        "metadata_relatedItems_itemPublisher": (
            facets.metadata_relatedItems_itemPublisher
        ),
        "metadata_relatedItems_itemRelationType": (
            facets.metadata_relatedItems_itemRelationType
        ),
        "metadata_relatedItems_itemResourceType": (
            facets.metadata_relatedItems_itemResourceType
        ),
        "metadata_relatedItems_itemStartPage": (
            facets.metadata_relatedItems_itemStartPage
        ),
        "metadata_relatedItems_itemURL": facets.metadata_relatedItems_itemURL,
        "metadata_relatedItems_itemVolume": facets.metadata_relatedItems_itemVolume,
        "metadata_relatedItems_itemYear": facets.metadata_relatedItems_itemYear,
        "metadata_resourceType": facets.metadata_resourceType,
        "metadata_rights": facets.metadata_rights,
        "metadata_series_seriesTitle": facets.metadata_series_seriesTitle,
        "metadata_series_seriesVolume": facets.metadata_series_seriesVolume,
        "metadata_subjectCategories": facets.metadata_subjectCategories,
        "metadata_subjects_classificationCode": (
            facets.metadata_subjects_classificationCode
        ),
        "metadata_subjects_subject_cs": facets.metadata_subjects_subject_cs,
        "metadata_subjects_subject_en": facets.metadata_subjects_subject_en,
        "metadata_subjects_subject": facets.metadata_subjects_subject,
        "metadata_subjects_subject_lang": facets.metadata_subjects_subject_lang,
        "metadata_subjects_subjectScheme": facets.metadata_subjects_subjectScheme,
        "metadata_subjects_valueURI": facets.metadata_subjects_valueURI,
        "metadata_systemIdentifiers_identifier": (
            facets.metadata_systemIdentifiers_identifier
        ),
        "metadata_systemIdentifiers_scheme": facets.metadata_systemIdentifiers_scheme,
        "metadata_technicalInfo_cs": facets.metadata_technicalInfo_cs,
        "metadata_technicalInfo_en": facets.metadata_technicalInfo_en,
        "metadata_technicalInfo": facets.metadata_technicalInfo,
        "metadata_technicalInfo_lang": facets.metadata_technicalInfo_lang,
        "metadata_version": facets.metadata_version,
        "state": facets.state,
        "state_timestamp": facets.state_timestamp,
    }
