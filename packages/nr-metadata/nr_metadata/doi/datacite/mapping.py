class DataCiteMappingNRDocs:

    def metadata_check(data, errors=[]):
        if "publishers" not in data:
            errors.append("Publisher must be defined")
        elif len(data["publishers"]) > 1:
            errors.append("One primary publisher that will be written within the DataCite definition must be specified")

        return errors

    def create_datacite_payload(self, data):
        # mandatory
        creators = creatibutor(data, "creators")
        titles = title(data)
        publishers = publisher(data)
        dc_resource_type = resource_type(data)

        payload = {
            "data": {
                "type": "dois",
                "attributes": {
                }
            }
        }
        payload["data"]["attributes"]["creators"] = creators
        payload["data"]["attributes"]["titles"] = titles
        payload["data"]["attributes"]["publisher"] = publishers
        payload["data"]["attributes"]["types"] = {}
        payload["data"]["attributes"]["types"]["resourceTypeGeneral"] = dc_resource_type
        # optional
        if "subjects" in data:
            dc_subjects = subjects(data)
            payload["data"]["attributes"]["subjects"] = dc_subjects
        if "contributors" in data:
            dc_contributors = creatibutor(data, "contributors")
            payload["data"]["attributes"]["contributors"] = dc_contributors

        dc_dates = []

        if "dateAvailable" in data:
            dc_dates.append({"date": data["dateAvailable"], "dateType": "Available"})
        if "dateModified" in data:
            dc_dates.append({"date": data["dateModified"], "dateType": "Updated"})
        if "dateIssued" in data:
            dc_dates.append({"date": data["dateIssued"], "dateType": "Issued"})
        if len(dc_dates) > 0:
            payload["data"]["attributes"]["dates"] = dc_dates

        if "rights" in data:
            dc_rights = []
            for right in data["rights"]:
                dc_rights.append({"rights": right["title"], "rightsIdentifier": right["id"]})
            if len(dc_rights) > 0:
                payload["data"]["attributes"]["rightsList"] = dc_rights
        if "abstract" in data:
            dc_descriptions = []
            for abstr in data["abstract"]:
                dc_descriptions.append(
                    {"lang": abstr["lang"], "description": abstr["value"], "descriptionType": "Abstract"})
            if len(dc_descriptions) > 0:
                payload["data"]["attributes"]["descriptions"] = dc_descriptions

        if "fundingReferences" in data:
            payload["data"]["attributes"]["FundingReference"] = funder(data)
            # todo check metadata - funder name mandatory, not in our scheme (project id is manddatory in nr docs)
        if "relatedItems" in data:
            payload["data"]["attributes"]["relatedItems"] = related_items(data)

        # todo languages - we have array, dc has one value

    def add_doi(self, data,  doi_value):
        doi = {"scheme": "DOI", "identifier": doi_value}

        if "objectIdentifiers" in data["metadata"]:
            data["metadata"]["objectIdentifiers"].append(doi)
        else:
            data["metadata"]["objectIdentifiers"] = [doi]

        return data

def publisher(data):
    if "publishers" in data:
        return data["publishers"][0]

def resource_type_mapping(rs_type):
    title_mapping = {
        "Book": "Book",
        "Book chapter": "BookChapter",
        "Article": "JournalArticle",
        "Review": "Text",
        "Dataset": "Dataset",
        "Conference paper": "ConferencePaper",
        "Conference proceeding": "ConferenceProceedings",
        "Conference programme": "Event",
        "Conference poster": "Other",
        "Data paper": "DataPaper",
        "Data management plan": "OutputManagementPlan",
        "Software": "Software",
        "Software paper": "Text",
        "Interactive resource": "InteractiveResource",
        "Model": "Model",
        "Physical object": "PhysicalObject",
        "Bachelor thesis": "Dissertation",
        "Master thesis": "Dissertation",
        "Rigorous thesis": "Dissertation",
        "Doctoral thesis": "Dissertation",
        "Post-doctoral thesis": "Dissertation",
        "Certified methodology": "Workflow",
        "Methodology without certification": "Workflow",
        "Heritage procedure": "Workflow",
        "Treatment procedure": "Workflow",
        "Annual report": "Report",
        "Research report": "Report",
        "Project report": "Report",
        "Statistical or status report": "Report",
        "Conservation report": "Report",
        "Field report": "Report",
        "Business trip report": "Report",
        "Press release": "Report",
        "Trade literature": "Text",
        "Studies and analyses": "Text",
        "Specialized map": "Other",
        "Educational material": "Text",
        "Exhibition catalogue or guide": "Text",
        "Other": "Other",
        "Cartographic material": "Other",
        "Patent": "Text",
        "Standard": "Standard",
        "Journal": "Journal",
    }
    return title_mapping.get(rs_type, "")

def resource_type(data):
    if "resourceType" in data:
        return resource_type_mapping(data["resourceType"]["title"])

def subjects(data):
    dc_subjects = []
    for sub in data["subjects"]:
        dc_sub = {}
        if "subject" in sub:
            dc_sub["subject"] = sub["subject"]["value"]
        if "subjectScheme" in sub:
            dc_sub["subjectScheme"] = sub["subjectScheme"]
        if dc_sub != {}:
            dc_subjects.append(dc_sub)
    return dc_subjects

    pass

def title(data):
    datacite_titles = []
    if "title" in data:
        title_def = data["title"]
        datacite_titles.append({"title": title_def})
    if "additionalTitles" in data:
        for add_title in data["additionalTitles"]:
            additional_datacite_title = {}
            if "title" in add_title:
                additional_datacite_title["lang"] = add_title["title"]["lang"]
                additional_datacite_title["title"] = add_title["title"]["value"]
            if "titleType" in add_title:
                additional_datacite_title["titleType"] = add_title["titleType"][0].upper() + add_title["titleType"][1:]
            if additional_datacite_title != {}:
                datacite_titles.append(additional_datacite_title)

    return datacite_titles

def contributor_role(title):
    title_mapping = {
        "contact-person": "ContactPerson",
        "data-collector": "DataCollector",
        "data-curator": "DataCurator",
        "data-manager": "DataManager",
        "distributor": "Distributor",
        "editor": "Editor",
        "producer": "Producer",
        "project-leader": "ProjectLeader",
        "project-manager": "ProjectManager",
        "project-member": "ProjectMember",
        "researcher": "Researcher",
        "research-group": "ResearchGroup",
        "rights-holder": "RightsHolder",
        "supervisor": "Supervisor",
        "referee": "Other",
        "advisor": "Other",
        "illustrator": "Other",
        "exhibition-curator": "Other",
        "moderator": "Other",
        "translator": "Other",
        "photographer": "Other",
        "reviewer": "Other",
        "collaborator": "Other",
        "artist": "Other",
        "interviewee": "Other",
        "interviewer": "Other",
        "organizer": "Other",
        "speaker": "Other",
        "panelist": "Other",
        "publisher": "Other",
        "proofreader": "Other",
        "owner": "Other",
        "former-owner": "Other",
        "respondent": "Other",
    }

    return title_mapping.get(title, "")
def creatibutor(data, type):
    creatibutor_def = data[type]
    datacite_creatibutors = []
    for creatibutor in creatibutor_def:
        datacite_creatibutor = {}
        if "fullName" in creatibutor: #required
            datacite_creatibutor["name"] = creatibutor["fullName"]
        if "nameType" in creatibutor:
            datacite_creatibutor["nameType"] = creatibutor["nameType"]
        if "role" in creatibutor:
            datacite_creatibutor["contributorType"] = contributor_role(creatibutor["role"]["id"])
        if "authorityIdentifiers" in creatibutor:
            creatibutors_ids = []
            for id in creatibutor["authorityIdentifiers"]:
                creatibutor_id = {}
                if "scheme" in id: #required
                    creatibutor_id["nameIdentifierScheme"] = id["scheme"]
                if "identifier" in id:
                    creatibutor_id["nameIdentifier"] = id["identifier"]
                if creatibutor_id != {}:
                    creatibutors_ids.append(creatibutor_id)
            if len(creatibutors_ids) > 0:
                datacite_creatibutor["nameIdentifiers"] = creatibutors_ids
        datacite_creatibutors.append(datacite_creatibutor)
    return datacite_creatibutors
        #TODO not the same affiliation identifier as in datacite


def funder(data):
    funders_def = data["fundingReferences"]
    dc_funders = []
    for f in funders_def:
        dc_funder = {}
        if "funder" in f: #todo funderIdentifier ?
            dc_funder["funderName"] = f["funder"]
        dc_funders.append(dc_funder)
    return dc_funders

def related_items(data):
    dc_related_items = []
    related_items_def = data["relatedItems"]
    for rel in related_items_def:
        dc_rel = {}
        if "itemContributors" in rel:
            dc_rel["contributors"] = creatibutor(rel, "itemContributors")
        if "itemCreators" in rel:
            dc_rel["creators"] = creatibutor(rel, "itemCreators")
        if "itemRelationType" in rel:
            dc_rel["relationType"] = rel["itemRelationType"]["title"][0].upper() + rel["itemRelationType"]["title"][1:]
        if "itemResourceType" in rel:
            dc_rel["relatedItemType"] = resource_type_mapping(rel["itemResourceType"]["title"])
        if "itemStartPage" in rel:
            dc_rel["firstPage"] = rel["itemStartPage"]
        if "itemEndPage" in rel:
            dc_rel["lastPage"] = rel["itemEndPage"]
        if "itemIssue" in rel:
            dc_rel["issue"] = rel["itemIssue"]
        if "itemTitle" in rel:
            dc_rel["Title"] = {"title" : rel["itemTitle"]}
        if "itemVolume" in rel:
            dc_rel["volume "] = rel["itemVolume"]
        if "itemYear" in rel:
            dc_rel["PublicationYear"] = rel["itemYear"]

        if dc_rel != {}:
            dc_related_items.append(dc_rel)
    return dc_related_items

