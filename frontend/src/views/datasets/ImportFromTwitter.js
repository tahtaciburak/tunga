import React, { } from 'react'
import {
  CCol, CCard,
  CCardBody,
  CCardHeader,
  CWidgetProgressIcon,
  CButton,
  CFormGroup,
  CInput,
  CInputFile,
  CLabel,
  CRow,
  CAlert
} from '@coreui/react'

import CIcon from '@coreui/icons-react'

import translate from '../../services/i18n/Translate';

import APIService from '../../services/APIService'
import AlertService from '../../services/AlertService'

class ImportFromTwitter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      is_configured: true,
      dataset_name: "",
      dataset_description: "",
      is_show_result_alert: false,
      is_upload_successful: false,
      file: null,
      upload_file_name: translate.translate("retrieval.import_from_local.choose_file")
    }
    this.handleDatasetNameChange = this.handleDatasetNameChange.bind(this);
    this.handleDatasetDescriptionChange = this.handleDatasetDescriptionChange.bind(this);
    this.handleFileUploadChange = this.handleFileUploadChange.bind(this);

    this.handleSubmitButtonClick = this.handleSubmitButtonClick.bind(this);
    this.handleRefreshClick = this.handleRefreshClick.bind(this);

  }

  handleDatasetNameChange(event) {
    this.setState({ dataset_name: event.target.value });
  }

  handleDatasetDescriptionChange(event) {
    this.setState({ dataset_description: event.target.value });
  }

  handleFileUploadChange(event) {
    this.setState({ file: event.target.files[0] });
    this.setState({ upload_file_name: event.target.files[0].name })
  }

  handleRefreshClick(event) {
    this.setState({
      dataset_name: "",
      dataset_description: "",
      is_show_result_alert: false,
      is_upload_successful: false,
      file: null,
      upload_file_name: translate.translate("retrieval.import_from_local.choose_file")
    })
  }

  handleSubmitButtonClick(e) {
    let formData = new FormData();
    formData.append("file", this.state.file);
    formData.append("dataset_name", this.state.dataset_name);
    formData.append("dataset_description", this.state.dataset_description);

    e.preventDefault();
    APIService.requests
      .post('dataset/local', formData)
      .then(data => {
        console.log(data);
        this.setState({ is_show_result_alert: true })
        this.setState({ is_upload_successful: true })

      })
      .catch(data => {
        alert("hata")
        AlertService.Add({
          type: 'alert',
          //message: translate.getText('error.' + data.response.body.error.code),
          level: 'error',
          autoDismiss: 5
        });
      });

  }

  render() {
    if (!this.state.is_configured) {
      return (
        <>
          <CAlert color="danger">{translate.translate("retrieval.import_from_twitter.apikey_not_found")}</CAlert>
        </>
      )

    }
    else {
      return (
        <>
          <div className="card">
            <div className="card-header">
              {translate.translate("datasets.import_from_twitter")}
            </div>
            <div className="card-body">
              <CCol xs="12" lg="12">
                <CCard>
                  <CCardHeader>
                    {translate.translate("retrieval.import_from_local.file_metadata")}
                  </CCardHeader>
                  <CCardBody>
                    <CFormGroup>
                      <CLabel htmlFor="datasetName">{translate.translate("retrieval.import_from_local.dataset_name")}</CLabel>
                      <CInput onChange={this.handleDatasetNameChange} id="datasetName" placeholder={translate.translate("retrieval.import_from_local.dataset_name_placeholder")} />
                    </CFormGroup>
                    <CFormGroup>
                      <CLabel htmlFor="datasetDescription">{translate.translate("retrieval.import_from_local.dataset_description")}</CLabel>
                      <CInput onChange={this.handleDatasetDescriptionChange} id="datasetDescription" placeholder={translate.translate("retrieval.import_from_local.dataset_description_placeholder")} />
                    </CFormGroup>

                  </CCardBody>
                </CCard>

                <CCard>
                  <CCardHeader>
                    {translate.translate("retrieval.import_from_twitter.fetch_data_from_user")}
                  </CCardHeader>
                  <CCardBody>
                    <CFormGroup>
                      <CLabel htmlFor="twitterUsername">{translate.translate("retrieval.import_from_twitter.twitter_username")}</CLabel>
                      <CInput onChange={this.handleDatasetDescriptionChange} id="twitterUsername" placeholder={translate.translate("retrieval.import_from_twitter.twitter_username_placeholder")} />
                    </CFormGroup>

                    <CFormGroup row>

                      <CCol xs="12" md="12">
                        <CButton onClick={this.handleSubmitButtonClick} color="success">{translate.translate("retrieval.import_from_twitter.fetch_from_user")}</CButton>
                      </CCol>
                    </CFormGroup>
                  </CCardBody>
                  <CCol hidden={!this.state.is_show_result_alert}>
                    <CAlert hidden={!this.state.is_upload_successful} color="success">
                      {translate.translate("retrieval.import_from_local.file_upload_success")}
                    </CAlert>
                    <CAlert hidden={this.state.is_upload_successful} color="danger">
                      {translate.translate("retrieval.import_from_local.file_upload_fail")}
                    </CAlert>
                    <CButton onClick={this.handleRefreshClick} color="primary">{translate.translate("retrieval.import_from_twitter.fetch_data_from_user")}</CButton>
                  </CCol>
                </CCard>

                <CCard>
                  <CCardHeader>
                    {translate.translate("retrieval.import_from_twitter.fetch_data_from_hashtag")}
                  </CCardHeader>
                  <CCardBody>
                    <CFormGroup>
                      <CLabel htmlFor="hashtag">{translate.translate("retrieval.import_from_twitter.fetch_data_from_hashtag")}</CLabel>
                      <CInput onChange={this.handleDatasetDescriptionChange} id="hashtag" placeholder={translate.translate("retrieval.import_from_twitter.fetch_data_from_hashtag_placeholder")} />
                    </CFormGroup>

                    <CFormGroup row>

                      <CCol xs="12" md="12">
                        <CButton onClick={this.handleSubmitButtonClick} color="success">{translate.translate("retrieval.import_from_twitter.fetch_data_from_hashtag")}</CButton>
                      </CCol>
                    </CFormGroup>
                  </CCardBody>
                  <CCol hidden={!this.state.is_show_result_alert}>
                    <CAlert hidden={!this.state.is_upload_successful} color="success">
                      {translate.translate("retrieval.import_from_local.file_upload_success")}
                    </CAlert>
                    <CAlert hidden={this.state.is_upload_successful} color="danger">
                      {translate.translate("retrieval.import_from_local.file_upload_fail")}
                    </CAlert>
                    <CButton onClick={this.handleRefreshClick} color="primary">{translate.translate("retrieval.import_from_local.upload_new_file")}</CButton>
                  </CCol>
                </CCard>
              </CCol>
            </div>
          </div>
        </>
      )

    }
  }
}

export default ImportFromTwitter
