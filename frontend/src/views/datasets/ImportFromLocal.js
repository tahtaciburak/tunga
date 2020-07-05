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

class ImportFromLocal extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <>
        <div className="card">
          <div className="card-header">
            {translate.translate("datasets.import_from_local")}
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
                    <CInput id="datasetName" placeholder={translate.translate("retrieval.import_from_local.dataset_name_placeholder")} />
                  </CFormGroup>
                  <CFormGroup>
                    <CLabel htmlFor="datasetDescription">{translate.translate("retrieval.import_from_local.dataset_description")}</CLabel>
                    <CInput id="datasetDescription" placeholder={translate.translate("retrieval.import_from_local.dataset_description_placeholder")} />
                  </CFormGroup>

                </CCardBody>
              </CCard>

              <CCard>
                <CCardHeader>
                  {translate.translate("retrieval.import_from_local.file_upload")}
                </CCardHeader>
                <CCardBody>
                  <CFormGroup row>
                    <CLabel col md={3}>{translate.translate("retrieval.import_from_local.choose_dataset_file")}</CLabel>
                    <CCol xs="12" md="9">
                      <CInputFile custom id="custom-file-input" />
                      <CLabel htmlFor="custom-file-input" variant="custom-file">
                        {translate.translate("retrieval.import_from_local.choose_file")}
                      </CLabel>
                    </CCol>
                    <CCol xs="12" md="12">
                      <CButton color="success">{translate.translate("retrieval.import_from_local.upload")}</CButton>
                      <CButton style={{ marginLeft: 10 }} color="success">{translate.translate("retrieval.import_from_local.upload_and_analyze")}</CButton>

                    </CCol>
                  </CFormGroup>
                </CCardBody>
              </CCard>
              <CAlert color="success">
                {translate.translate("retrieval.import_from_local.file_upload_success")}
              </CAlert>
              <CAlert color="danger">
                {translate.translate("retrieval.import_from_local.file_upload_fail")}
              </CAlert>

              <CCard>
                <CCardHeader>
                  {translate.translate("retrieval.import_from_local.analysis")}
                </CCardHeader>
                <CCardBody>
                  <CRow>
                    <CCol sm="6" md="2">
                      <CWidgetProgressIcon
                        header="87.500"
                        text={translate.translate("retrieval.import_from_local.total_row_count")}
                        color="gradient-info"
                        inverse
                      >
                        <CIcon name="cil-people" height="36" />
                      </CWidgetProgressIcon>
                    </CCol>
                    <CCol sm="6" md="2">
                      <CWidgetProgressIcon
                        header="385"
                        text={translate.translate("retrieval.import_from_local.total_field_count")}
                        color="gradient-success"
                        inverse
                      >
                        <CIcon name="cil-userFollow" height="36" />
                      </CWidgetProgressIcon>
                    </CCol>
                    <CCol sm="6" md="2">
                      <CWidgetProgressIcon
                        header="1238"
                        text={translate.translate("retrieval.import_from_local.total_word_count")}
                        color="gradient-warning"
                        inverse
                      >
                        <CIcon name="cil-basket" height="36" />
                      </CWidgetProgressIcon>
                    </CCol>
                    <CCol sm="6" md="2">
                      <CWidgetProgressIcon
                        header="28%"
                        text={translate.translate("retrieval.import_from_local.total_distinct_word_count")}
                        color="gradient-primary"
                        inverse
                      >
                        <CIcon name="cil-chartPie" height="36" />
                      </CWidgetProgressIcon>
                    </CCol>
                    <CCol sm="6" md="2">
                      <CWidgetProgressIcon
                        header="0"
                        text={translate.translate("retrieval.import_from_local.total_missing_values")}
                        color="gradient-danger"
                        inverse
                      >
                        <CIcon name="cil-speedometer" height="36" />
                      </CWidgetProgressIcon>
                    </CCol>
                    <CCol sm="6" md="2">
                      <CWidgetProgressIcon
                        header="0"
                        text="comments"
                        color="gradient-info"
                        inverse
                      >
                        <CIcon name="cil-speech" height="36" />
                      </CWidgetProgressIcon>
                    </CCol>
                  </CRow>

                </CCardBody>
              </CCard>

            </CCol>
          </div>
        </div>
      </>
    )
  }
}

export default ImportFromLocal

/**
 *
 *
 *             <CCard>
            <CCardHeader>
              Yukleme
            </CCardHeader>
            <CCardBody>
              <CForm>
                <CInputGroup className="mb-3">
                  <CInputGroupPrepend>
                    <CInputGroupText>
                    </CInputGroupText>
                  </CInputGroupPrepend>
                  <CInput type="text" placeholder="Email" autoComplete="email" />
                  <CFormGroup row>
                  <CLabel col md={3}>Custom file input</CLabel>
                  <CCol xs="12" md="9">
                    <CInputFile custom id="custom-file-input"/>
                    <CLabel htmlFor="custom-file-input" variant="custom-file">
                      Choose file...
                    </CLabel>
                  </CCol>
                </CFormGroup>
                </CInputGroup>

              </CForm>
            </CCardBody>
          </CCard>

 */