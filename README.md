# mailslurp-client
MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more. 

## Resources
- [Homepage](https://www.mailslurp.com)
- Get an [API KEY](https://app.mailslurp.com/sign-up/)
- Generated [SDK Clients](https://www.mailslurp.com/docs/)
- [Examples](https://github.com/mailslurp/examples) repository


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: d1659dc1567a5b62f65d0612107a50aace03e085
- Package version: 7.0.8
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import mailslurp_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mailslurp_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mailslurp_client
from mailslurp_client.rest import ApiException
from pprint import pprint

configuration = mailslurp_client.Configuration()
# Configure API key authorization: API_KEY
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Defining host is optional and default to https://api.mailslurp.com
configuration.host = "https://api.mailslurp.com"
# Enter a context with an instance of the API client
with mailslurp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailslurp_client.AliasControllerApi(api_client)
    create_owned_alias_options = mailslurp_client.CreateOwnedAliasOptions() # CreateOwnedAliasOptions | createOwnedAliasOptions

    try:
        # Create an email alias
        api_instance.create_alias(create_owned_alias_options)
    except ApiException as e:
        print("Exception when calling AliasControllerApi->create_alias: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.mailslurp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AliasControllerApi* | [**create_alias**](docs/AliasControllerApi.md#create_alias) | **POST** /aliases | Create an email alias
*AliasControllerApi* | [**create_anonymous_alias**](docs/AliasControllerApi.md#create_anonymous_alias) | **POST** /aliases/anonymous | Create an anonymous email alias
*AliasControllerApi* | [**delete_alias**](docs/AliasControllerApi.md#delete_alias) | **DELETE** /aliases/{aliasId} | Delete an owned alias
*AliasControllerApi* | [**get_alias**](docs/AliasControllerApi.md#get_alias) | **GET** /aliases/{aliasId} | Get an email alias
*AliasControllerApi* | [**get_aliases**](docs/AliasControllerApi.md#get_aliases) | **GET** /aliases | Get all email aliases
*AliasControllerApi* | [**update_alias**](docs/AliasControllerApi.md#update_alias) | **PUT** /aliases/{aliasId} | Update an owned alias
*AttachmentControllerApi* | [**upload_attachment**](docs/AttachmentControllerApi.md#upload_attachment) | **POST** /attachments | Upload an attachment for sending
*AttachmentControllerApi* | [**upload_multipart_form**](docs/AttachmentControllerApi.md#upload_multipart_form) | **POST** /attachments/multipart | Upload an attachment for sending using Multipart Form
*BulkActionsControllerApi* | [**bulk_create_inboxes**](docs/BulkActionsControllerApi.md#bulk_create_inboxes) | **POST** /bulk/inboxes | Bulk create Inboxes (email addresses)
*BulkActionsControllerApi* | [**bulk_delete_inboxes**](docs/BulkActionsControllerApi.md#bulk_delete_inboxes) | **DELETE** /bulk/inboxes | Bulk Delete Inboxes
*BulkActionsControllerApi* | [**bulk_send_emails**](docs/BulkActionsControllerApi.md#bulk_send_emails) | **POST** /bulk/send | Bulk Send Emails
*CommonActionsControllerApi* | [**create_new_email_address**](docs/CommonActionsControllerApi.md#create_new_email_address) | **POST** /createInbox | Create new random inbox
*CommonActionsControllerApi* | [**create_new_email_address1**](docs/CommonActionsControllerApi.md#create_new_email_address1) | **POST** /newEmailAddress | Create new random inbox
*CommonActionsControllerApi* | [**empty_inbox**](docs/CommonActionsControllerApi.md#empty_inbox) | **DELETE** /emptyInbox | Delete all emails in an inbox
*CommonActionsControllerApi* | [**send_email_simple**](docs/CommonActionsControllerApi.md#send_email_simple) | **POST** /sendEmail | Send an email
*ContactControllerApi* | [**create_contact**](docs/ContactControllerApi.md#create_contact) | **POST** /contacts | Create a contact
*ContactControllerApi* | [**delete_contact**](docs/ContactControllerApi.md#delete_contact) | **DELETE** /contacts/{contactId} | Delete contact
*ContactControllerApi* | [**get_all_contacts**](docs/ContactControllerApi.md#get_all_contacts) | **GET** /contacts/paginated | Get all contacts
*ContactControllerApi* | [**get_contact**](docs/ContactControllerApi.md#get_contact) | **GET** /contacts/{contactId} | Get contact
*ContactControllerApi* | [**get_contacts**](docs/ContactControllerApi.md#get_contacts) | **GET** /contacts | Get all contacts
*DomainControllerApi* | [**create_domain**](docs/DomainControllerApi.md#create_domain) | **POST** /domains | Create Domain
*DomainControllerApi* | [**delete_domain**](docs/DomainControllerApi.md#delete_domain) | **DELETE** /domains/{id} | Delete a domain
*DomainControllerApi* | [**get_domain**](docs/DomainControllerApi.md#get_domain) | **GET** /domains/{id} | Get a domain
*DomainControllerApi* | [**get_domains**](docs/DomainControllerApi.md#get_domains) | **GET** /domains | Get domains
*EmailControllerApi* | [**delete_all_emails**](docs/EmailControllerApi.md#delete_all_emails) | **DELETE** /emails | Delete all emails
*EmailControllerApi* | [**delete_email**](docs/EmailControllerApi.md#delete_email) | **DELETE** /emails/{emailId} | Delete an email
*EmailControllerApi* | [**download_attachment**](docs/EmailControllerApi.md#download_attachment) | **GET** /emails/{emailId}/attachments/{attachmentId} | Get email attachment bytes
*EmailControllerApi* | [**forward_email**](docs/EmailControllerApi.md#forward_email) | **POST** /emails/{emailId}/forward | Forward email
*EmailControllerApi* | [**get_attachment_meta_data**](docs/EmailControllerApi.md#get_attachment_meta_data) | **GET** /emails/{emailId}/attachments/{attachmentId}/metadata | Get email attachment metadata
*EmailControllerApi* | [**get_attachments**](docs/EmailControllerApi.md#get_attachments) | **GET** /emails/{emailId}/attachments | Get all email attachment metadata
*EmailControllerApi* | [**get_email**](docs/EmailControllerApi.md#get_email) | **GET** /emails/{emailId} | Get email content
*EmailControllerApi* | [**get_email_html**](docs/EmailControllerApi.md#get_email_html) | **GET** /emails/{emailId}/html | Get email content as HTML
*EmailControllerApi* | [**get_emails_paginated**](docs/EmailControllerApi.md#get_emails_paginated) | **GET** /emails | Get all emails
*EmailControllerApi* | [**get_raw_email_contents**](docs/EmailControllerApi.md#get_raw_email_contents) | **GET** /emails/{emailId}/raw | Get raw email string
*EmailControllerApi* | [**get_raw_email_json**](docs/EmailControllerApi.md#get_raw_email_json) | **GET** /emails/{emailId}/raw/json | Get raw email in JSON
*EmailControllerApi* | [**get_unread_email_count**](docs/EmailControllerApi.md#get_unread_email_count) | **GET** /emails/unreadCount | Get unread email count
*EmailControllerApi* | [**validate_email**](docs/EmailControllerApi.md#validate_email) | **POST** /emails/{emailId}/validate | Validate email
*FormControllerApi* | [**submit_form**](docs/FormControllerApi.md#submit_form) | **POST** /forms | Submit a form to be parsed and sent as an email to an address determined by the form fields
*GroupControllerApi* | [**add_contacts_to_group**](docs/GroupControllerApi.md#add_contacts_to_group) | **PUT** /groups/{groupId}/contacts | Add contacts to a group
*GroupControllerApi* | [**create_group**](docs/GroupControllerApi.md#create_group) | **POST** /groups | Create a group
*GroupControllerApi* | [**delete_group**](docs/GroupControllerApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete group
*GroupControllerApi* | [**get_all_groups**](docs/GroupControllerApi.md#get_all_groups) | **GET** /groups/paginated | Get all Contact Groups in paginated format
*GroupControllerApi* | [**get_group**](docs/GroupControllerApi.md#get_group) | **GET** /groups/{groupId} | Get group
*GroupControllerApi* | [**get_group_with_contacts**](docs/GroupControllerApi.md#get_group_with_contacts) | **GET** /groups/{groupId}/contacts | Get group and contacts belonging to it
*GroupControllerApi* | [**get_groups**](docs/GroupControllerApi.md#get_groups) | **GET** /groups | Get all groups
*GroupControllerApi* | [**remove_contacts_from_group**](docs/GroupControllerApi.md#remove_contacts_from_group) | **DELETE** /groups/{groupId}/contacts | Remove contacts from a group
*InboxControllerApi* | [**create_inbox**](docs/InboxControllerApi.md#create_inbox) | **POST** /inboxes | Create an Inbox (email address)
*InboxControllerApi* | [**delete_all_inboxes**](docs/InboxControllerApi.md#delete_all_inboxes) | **DELETE** /inboxes | Delete all inboxes
*InboxControllerApi* | [**delete_inbox**](docs/InboxControllerApi.md#delete_inbox) | **DELETE** /inboxes/{inboxId} | Delete inbox
*InboxControllerApi* | [**get_all_inboxes**](docs/InboxControllerApi.md#get_all_inboxes) | **GET** /inboxes/paginated | List Inboxes Paginated
*InboxControllerApi* | [**get_emails**](docs/InboxControllerApi.md#get_emails) | **GET** /inboxes/{inboxId}/emails | Get emails in an Inbox
*InboxControllerApi* | [**get_inbox**](docs/InboxControllerApi.md#get_inbox) | **GET** /inboxes/{inboxId} | Get Inbox
*InboxControllerApi* | [**get_inbox_emails_paginated**](docs/InboxControllerApi.md#get_inbox_emails_paginated) | **GET** /inboxes/{inboxId}/emails/paginated | Get inbox emails paginated
*InboxControllerApi* | [**get_inbox_tags**](docs/InboxControllerApi.md#get_inbox_tags) | **GET** /inboxes/tags | Get inbox tags
*InboxControllerApi* | [**get_inboxes**](docs/InboxControllerApi.md#get_inboxes) | **GET** /inboxes | List Inboxes / Email Addresses
*InboxControllerApi* | [**send_email**](docs/InboxControllerApi.md#send_email) | **POST** /inboxes/{inboxId} | Send Email
*InboxControllerApi* | [**set_inbox_favourited**](docs/InboxControllerApi.md#set_inbox_favourited) | **PUT** /inboxes/{inboxId}/favourite | Set inbox favourited state
*InboxControllerApi* | [**update_inbox**](docs/InboxControllerApi.md#update_inbox) | **PATCH** /inboxes/{inboxId} | Update Inbox
*TemplateControllerApi* | [**create_template**](docs/TemplateControllerApi.md#create_template) | **POST** /templates | Create a Template
*TemplateControllerApi* | [**delete_template**](docs/TemplateControllerApi.md#delete_template) | **DELETE** /templates/{TemplateId} | Delete Template
*TemplateControllerApi* | [**get_all_templates**](docs/TemplateControllerApi.md#get_all_templates) | **GET** /templates/paginated | Get all Templates in paginated format
*TemplateControllerApi* | [**get_template**](docs/TemplateControllerApi.md#get_template) | **GET** /templates/{TemplateId} | Get Template
*TemplateControllerApi* | [**get_templates**](docs/TemplateControllerApi.md#get_templates) | **GET** /templates | Get all Templates
*WaitForControllerApi* | [**wait_for**](docs/WaitForControllerApi.md#wait_for) | **POST** /waitFor | Wait for conditions to be met
*WaitForControllerApi* | [**wait_for_email_count**](docs/WaitForControllerApi.md#wait_for_email_count) | **GET** /waitForEmailCount | Wait for and return count number of emails 
*WaitForControllerApi* | [**wait_for_latest_email**](docs/WaitForControllerApi.md#wait_for_latest_email) | **GET** /waitForLatestEmail | Fetch inbox&#39;s latest email or if empty wait for an email to arrive
*WaitForControllerApi* | [**wait_for_matching_email**](docs/WaitForControllerApi.md#wait_for_matching_email) | **POST** /waitForMatchingEmails | Wait or return list of emails that match simple matching patterns
*WaitForControllerApi* | [**wait_for_nth_email**](docs/WaitForControllerApi.md#wait_for_nth_email) | **GET** /waitForNthEmail | Wait for or fetch the email with a given index in the inbox specified
*WebhookControllerApi* | [**create_webhook**](docs/WebhookControllerApi.md#create_webhook) | **POST** /inboxes/{inboxId}/webhooks | Attach a WebHook URL to an inbox
*WebhookControllerApi* | [**delete_webhook**](docs/WebhookControllerApi.md#delete_webhook) | **DELETE** /inboxes/{inboxId}/webhooks/{webhookId} | Delete and disable a Webhook for an Inbox
*WebhookControllerApi* | [**get_all_webhooks**](docs/WebhookControllerApi.md#get_all_webhooks) | **GET** /webhooks/paginated | List Webhooks Paginated
*WebhookControllerApi* | [**get_webhook**](docs/WebhookControllerApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Get a webhook for an Inbox
*WebhookControllerApi* | [**get_webhooks**](docs/WebhookControllerApi.md#get_webhooks) | **GET** /inboxes/{inboxId}/webhooks | Get all Webhooks for an Inbox
*WebhookControllerApi* | [**send_test_data**](docs/WebhookControllerApi.md#send_test_data) | **POST** /webhooks/{webhookId}/test | Send webhook test data


## Documentation For Models

 - [Alias](docs/Alias.md)
 - [AttachmentMetaData](docs/AttachmentMetaData.md)
 - [BasicAuthOptions](docs/BasicAuthOptions.md)
 - [BulkSendEmailOptions](docs/BulkSendEmailOptions.md)
 - [ContactDto](docs/ContactDto.md)
 - [ContactProjection](docs/ContactProjection.md)
 - [CreateAnonymousAliasOptions](docs/CreateAnonymousAliasOptions.md)
 - [CreateContactOptions](docs/CreateContactOptions.md)
 - [CreateDomainOptions](docs/CreateDomainOptions.md)
 - [CreateGroupOptions](docs/CreateGroupOptions.md)
 - [CreateOwnedAliasOptions](docs/CreateOwnedAliasOptions.md)
 - [CreateTemplateOptions](docs/CreateTemplateOptions.md)
 - [CreateWebhookOptions](docs/CreateWebhookOptions.md)
 - [DomainDto](docs/DomainDto.md)
 - [DomainPreview](docs/DomainPreview.md)
 - [Email](docs/Email.md)
 - [EmailAnalysis](docs/EmailAnalysis.md)
 - [EmailPreview](docs/EmailPreview.md)
 - [EmailProjection](docs/EmailProjection.md)
 - [ForwardEmailOptions](docs/ForwardEmailOptions.md)
 - [GroupContactsDto](docs/GroupContactsDto.md)
 - [GroupDto](docs/GroupDto.md)
 - [GroupProjection](docs/GroupProjection.md)
 - [HTMLValidationResult](docs/HTMLValidationResult.md)
 - [Inbox](docs/Inbox.md)
 - [InboxProjection](docs/InboxProjection.md)
 - [JsonNode](docs/JsonNode.md)
 - [MatchOption](docs/MatchOption.md)
 - [MatchOptions](docs/MatchOptions.md)
 - [PageAlias](docs/PageAlias.md)
 - [PageContactProjection](docs/PageContactProjection.md)
 - [PageEmailPreview](docs/PageEmailPreview.md)
 - [PageEmailProjection](docs/PageEmailProjection.md)
 - [PageGroupProjection](docs/PageGroupProjection.md)
 - [PageInboxProjection](docs/PageInboxProjection.md)
 - [PageTemplateProjection](docs/PageTemplateProjection.md)
 - [PageWebhookProjection](docs/PageWebhookProjection.md)
 - [Pageable](docs/Pageable.md)
 - [RawEmailJson](docs/RawEmailJson.md)
 - [SendEmailOptions](docs/SendEmailOptions.md)
 - [SetInboxFavouritedOptions](docs/SetInboxFavouritedOptions.md)
 - [SimpleSendEmailOptions](docs/SimpleSendEmailOptions.md)
 - [Sort](docs/Sort.md)
 - [TemplateDto](docs/TemplateDto.md)
 - [TemplateProjection](docs/TemplateProjection.md)
 - [TemplateVariable](docs/TemplateVariable.md)
 - [UnreadCount](docs/UnreadCount.md)
 - [UpdateGroupContacts](docs/UpdateGroupContacts.md)
 - [UpdateInboxOptions](docs/UpdateInboxOptions.md)
 - [UploadAttachmentOptions](docs/UploadAttachmentOptions.md)
 - [ValidationDto](docs/ValidationDto.md)
 - [ValidationMessage](docs/ValidationMessage.md)
 - [WaitForConditions](docs/WaitForConditions.md)
 - [WebhookDto](docs/WebhookDto.md)
 - [WebhookProjection](docs/WebhookProjection.md)
 - [WebhookTestRequest](docs/WebhookTestRequest.md)
 - [WebhookTestResponse](docs/WebhookTestResponse.md)
 - [WebhookTestResult](docs/WebhookTestResult.md)


## Documentation For Authorization


## API_KEY

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author




